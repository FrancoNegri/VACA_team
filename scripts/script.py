import numpy
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates
import random

x = range(0, 500)
z = [numpy.exp(-0.027*_) + 10 + random.uniform(0, 0.5) for _ in x]
y = [numpy.exp(0.0027*_) + 5 + random.uniform(0, 0.2) for _ in x]
w = [numpy.exp(0.0030*_) + random.uniform(0, 0.3)for _ in x]

print(z)

base = datetime.datetime.today()
date_list = [base - datetime.timedelta(days=x) for x in range(0, len(z))]

plt.plot(date_list, w, label="Paddoc 1")
plt.plot(date_list, y, label="Paddoc 2")
plt.plot(date_list, z, label="Paddoc 3")
plt.legend()

# Set the locator
locator = mdates.MonthLocator()  # every month
# Specify the format - %b gives us Jan, Feb...
fmt = mdates.DateFormatter('%b')
X = plt.gca().xaxis

X.set_major_locator(locator)
# Specify formatter
X.set_major_formatter(fmt)

plt.ylabel('Grass Quality')
plt.xlabel('Months')
plt.show()