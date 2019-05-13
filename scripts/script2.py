import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates
import random
import numpy
import math

x = range(0, 500)

print(math.ceil(4.2))
z = [int(math.ceil(numpy.random.exponential(0.4))) for _ in x]
y = [int(math.ceil(numpy.random.exponential(0.3))) for _ in x]
w = [int(math.ceil(numpy.random.exponential(0.2))) for _ in x]

print(z)

base = datetime.datetime.today()
date_list = [base - datetime.timedelta(days=x) for x in range(0, len(z))]

plt.plot(date_list, z, label="Paddoc 1")
plt.plot(date_list, y, label="Paddoc 2")
plt.plot(date_list, w, label="Paddoc 3")
plt.legend()

# Set the locator
locator = mdates.MonthLocator()  # every month
# Specify the format - %b gives us Jan, Feb...
fmt = mdates.DateFormatter('%b')
X = plt.gca().xaxis

X.set_major_locator(locator)
# Specify formatter
X.set_major_formatter(fmt)

plt.ylabel('Cattle insidents')
plt.xlabel('Months')
plt.show()