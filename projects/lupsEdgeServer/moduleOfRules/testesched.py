from schedulerEdge import  SchedulerEdge
if __name__ == '__main__':
    #scheduler = BackgroundScheduler()
    #scheduler.add_job(tick, 'cron', second = '5,10',minute = '40' , id = "12")
    #scheduler.start()
    #while True:
    #    time.sleep(1)
    test_sched = SchedulerEdge()
    test_sched.add_job('interval-3')
