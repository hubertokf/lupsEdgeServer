from scheduler import  *
import time
if __name__ == '__main__':

    test_sched = SchedulerEdge()

    test_sched.add_job('{ "modo": "cron", "info": {"second": "*/5", "minute": "*", "hour": "*", "day": "*", "week": "*", "month": "*", "year": "*"	}, "id_sensor": "18", "event": "gathering"}')
    #test_sched.add_job('{ "modo": "interval", "info": {"second": "30", "minute": "0", "hour": "0", "day": "0", "week": "0", "month": "0", "year": "0"	}, "id_sensor_virtual": "21231214", "id_sensor": "18", "event": "publish"}')

    #test_sched.verifica_sensores()
