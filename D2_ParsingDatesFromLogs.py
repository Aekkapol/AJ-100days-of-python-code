'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime
from datetime import date
from datetime import timedelta
import os, re
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()

# for row in loglines:
#     print(row)


# for you to code:
def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
    num_lst = re.findall(r'\d+', line)
    extract_number = datetime(*map(int, num_lst))
    print(extract_number)
    return extract_number
    pass

def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the
       timedelta between the first and last one.
       Return this datetime.timedelta object.'''

    n = 1
    time_dict = {}
    for row in loglines:
        if SHUTDOWN_EVENT in row:
            key = 't' + str(n)
            time_dict[key] = convert_to_datetime(row)
            n += 1
    print(time_dict)
    time_diff = time_dict['t2'] - time_dict['t1']
    print("Timedelta between the first and the last shutdown:", time_diff)
    return time_diff
    pass

time_between_shutdowns(loglines)
