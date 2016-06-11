from scheduler import  *
import time
if __name__ == '__main__':
    #scheduler = BackgroundScheduler()
    #scheduler.add_job(tick, 'cron', second = '5,10',minute = '40' , id = "12")
    #scheduler.start()
    #while True:
    #    time.sleep(1)
    test_sched = SchedulerEdge()
    #test_sched.add_job(3)
    test_sched.add_job('{ "modo": "cron", "info": {"second": "*/5", "minute": "*", "hour": "*", "day": "*", "week": "*", "month": "*", "year": "*"	}, "id_sensor_virtual": "21231214", "id_sensor": "18", "event": "publish"}')
    #test_sched.add_job('interval-12')
    #test_sched.add_job('interval-45')
    #time.sleep(2)
    #test_sched.remove_job('interval-45')
