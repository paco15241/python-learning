#!/usr/bin/env python

from datetime import datetime
from datetime import timedelta

def shorter_break():
    pass
def longer_break():
    pass

job_num = 0
while True:
    job = input("Input Job name: ")
    time = input("Input time in minutes: ")
    
    print(job)
    print(time)

    shorter_break()
    job_num += 1

    if job_num % 4 == 0:
        longer_break()

