#!/usr/bin python3

import re
import csv
import operator

logs = open("syslog.log","r").readlines()
for log in logs:
    print("This is a log: {}".format(log))

