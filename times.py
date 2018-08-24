# Let's find out when the most articles are submitted. One easy way to reframe this is to look at what hour articles are submitted.

# The submission_time column contains timestamps like this: 2011-11-09T21:56:22Z. These times are expressed in UTC.

# To get hour from a timestamp, I will use datetime and the dateutil library. The parser module in dateutil contains the parse function, which can take in a timestamp, and return a datetime object. Here's a link to the documentation: https://dateutil.readthedocs.io/en/latest/parser.html


# This is the code:

from dateutil.parser import parse
import read
import datetime

df = read.load_data()



def extract_hour(timestamp):
    hour = parse(timestamp)
    return hour.hour


df['hour_submission_time'] = df['submission_time'].apply(extract_hour)
#print(df['hour_submission_time'])
print(df['hour_submission_time'].value_counts())
#this will give let us know what time of the day the most articles are submitted!
