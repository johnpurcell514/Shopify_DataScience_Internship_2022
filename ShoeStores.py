import pandas as pd
from statistics import median
from statistics import mean
from statistics import mode
from pprint import pprint

df = pd.read_csv(r'/Users/johnpurcell/Desktop/2019 Winter Data Science Intern Challenge Data Set.csv')

# Part A: Think about what could be going wrong with our calculation.
Headers = list(df)
print("List of Headers")
print("---------------")
print(Headers)
print()

# Checking the AOV
AvgOrderValue = mean(df.order_amount)
print("Average Order Value")
print("-------------------")
print(AvgOrderValue)
print()
# By sorting the list reversed we can get a look at the upper results of the sales data
df.sort_values(by="order_amount", ascending=False, inplace=True)
# Create a list and show the top results
OrderAmounts = list(df.order_amount)
print("List of 50 Highest Order Amounts")
print("--------------------------------")
count = 0
while count < len(OrderAmounts[:50]):
    print(OrderAmounts[count], OrderAmounts[count +1 ], OrderAmounts[count +2],
          OrderAmounts[count + 3], OrderAmounts[count + 4])
    count += 5
print()

# Part B: What metric would you report for this dataset?
#  We will use Median and Mode. See documentation for explanation.

# Part C: Calculate these values (Median and Mode)

ModeOrderValue = mode(OrderAmounts)
MedianOrderValue = median(OrderAmounts)
print("Mode Order Value")
print("-------------------")
print(ModeOrderValue)
print()
print("Median Order Value")
print("-------------------")
print(MedianOrderValue)
print()




