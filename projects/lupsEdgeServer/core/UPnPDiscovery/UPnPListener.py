import socket
import struct
import threading
from simpletr64.devicetr64 import DeviceTR64
from simpletr64.discover import Discover

# UPnP group + port
class UPnPListener(object):
    def __init__(self, UPNP_GROUP="239.255.255.250", UPNP_PORT=1900):
        # Build a multicast socket
        # See http://wiki.python.org/moin/UdpCommunication#Multicasting.3F
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('', UPNP_PORT))
        mreq = struct.pack("=4sl", socket.inet_aton(UPNP_GROUP), socket.INADDR_ANY)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

        # Store it
        self.sock = sock

        # Create device storage
        self.devices = {}
        self.devicesFound = []

    # Internally used method to read a notification
    def listen_notification(self, data):
        upnp_header, upnp_body = data.split("\r\n\r\n")

        # Get header by line -- as fragments
        upnp_hfrags = upnp_header.split("\r\n") # Get lines

        # Ditch "NOTIFY * HTTP/1.1" ;)"
        upnp_hfrags.pop(0)

        # Storage
        header = {}

        # Fill storage
        for frag in upnp_hfrags:
            # Standards are helpful!
            splitpoint = frag.find(": ")
            header[frag[:splitpoint]] = frag[splitpoint+2:]

        # I don't need it, so I'll clear it here
        # -- I run this on a RaspberryPi, this is overkill elsewhere
        del upnp_header

        # Get the UUID
        if("USN" in header):
            uuid_base = header["USN"].find("uuid:") + 5
            uuid = header["USN"][uuid_base:uuid_base+36]
            nt_base = header["NT"].split(":")
            location = header["LOCATION"]
            if(len(nt_base)==5 and nt_base[1] == "schemas-upnp-org"):
                if(uuid in self.devices and uuid not in self.devicesFound):
                    device = DeviceTR64(...)
                    results = device.createFromUrl(location)

                    results.loadDeviceDefinitions(location)
                    results.deviceInformations
                    self.devicesFound.append(uuid)
                    print("UUID Match: %s" % uuid)
                    print(header)
                    print("--------------------------------------------")

    # Start listening
    def _listen(self):
        self.listening = True

        # Hint: this should be on a thread ;)
        while self.listening:
            # Grab a large wad of data
            upnp_data = self.sock.recv(10240).decode('utf-8')

            # Filter by type (we only care about NOTIFY for now)
            if(upnp_data[0:6] == "NOTIFY"):
                self.listen_notification(upnp_data)

    def listen(self):
        return threading.Thread(target=self._listen).start()

    # Register the uuid to a name -- as an example ... I put a handler here ;)
    def registerDevice(self, name="", uuid=""):
        if(name == "" or uuid == ""):
            print("Error registering device, check your name and uuid")
            return

        # Store uuid to name for quick search
        self.devices[uuid] = name


if __name__ == "__main__":
    # Create a default UPnP socket
    L = UPnPListener()
    L.registerDevice("RXV3900", "35c0c38e-4516-b17d-ffff-ffffbc092421")
    L.listen()