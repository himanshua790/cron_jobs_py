import datetime
import json
import signal
import sys
import time

import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

import utils

# Read Cron Details from cron.json
with open("cron.json") as f:
        jobs = json.load(f)
        print(jobs)


# Create a new Scheduler instance
scheduler = BlockingScheduler()

# Add Cron Jobs to the scheduler
for schedule, tasks in jobs.items():
    print(1, schedule, tasks)
    for task, data in tasks.items():
        print(2,task,data)
        if task == 'url':
            for url in data:
                print(CronTrigger.from_crontab(schedule))
                scheduler.add_job(utils.fetch, CronTrigger.from_crontab(schedule), args=[url])
    
# Define a signal handler function to gracefully shutdown the scheduler
def signal_handler():
    print('Stopping scheduler...')
    scheduler.shutdown()
    sys.exit(0)

# Register the signal handler function to the SIGINT signal (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)

scheduler.start()

# To keep main thread alive 
while True:
    time.sleep(1)