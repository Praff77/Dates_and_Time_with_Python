#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))

# print today's date
now = datetime.now()
print(now)


# print today's date one year from now
print("one year from now will be " +str(now+timedelta(days=365, hours=5, minutes=1)))

# create a timedelta that uses more than one argument
print("int 2 days and 3 weeks :" + str(now+timedelta(days=2, weeks =3)))


# calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d %Y")
print(s)

### How many days until April Fools' Day?
today = date.today()
afd = date(today.year, 4 ,1)


# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
    print("toolate %d" % ((today-afd).days))
    afd = afd.replace(year = today.year+1)



# Now calculate the amount of time until April Fool's Day  

timetp = afd - today
print("its just away", timetp.days )