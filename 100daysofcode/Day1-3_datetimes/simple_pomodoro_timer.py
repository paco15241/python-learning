#!/usr/bin/env python

from datetime import datetime
from datetime import timedelta

def get_break(now, break_time=5):
    course = timedelta(minutes=int(break_time))
    print("a little break {} minutes. {} to {}".format(break_time, str(now), str(now+course)))
    return now + course


def main():
    job_count = 0
    now = ""
    while True:
        job_name = input("Input Job name: ")
        job_time = input("Input time in minutes: ")
        
        course = timedelta(minutes=int(job_time))
        now = now if now else datetime.now()
        print("{} starts at {}".format(job_name, str(now)))
        now += course
        print("{} should end at {}".format(job_name, str(now)))

        job_count += 1
        now = get_break(now, break_time=5)

        if job_num % 4 == 0:
            get_break(now, break_time=30)

if __name__ == '__main__':
    main()
