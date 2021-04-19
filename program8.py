import csv
from collections import Counter

file1 = open("Starter-Python/Class-8/data.csv","r")
object1 = csv.reader(file1)
data = list(object1)
data.pop(0)

#calculate the mean
height = []
for i in data:
    value = float(i[1])
    height.append(value)

n = len(height)
x = 0
for i in height:
    x = x + i

mean = x/n
print("Mean: ", mean)

#calculate the median
height.sort()

median = 0
if(n%2 == 0):
    median1 = float(height[n//2])
    median2 = float(height[n//2 -1])

    median = (median1 + median2)//2
else:
    median = float(height[n//2])

print("Median: ", median)

#calculate the mode
mode_range = {
    "50-60": 0, 
    "60-70": 0,
    "70-80": 0,
}

counter = Counter(height)
for i, occurence in counter.items():
    if(50 < float(i) < 60):
        mode_range["50-60"] = mode_range["50-60"] + occurence
    elif(60 < float(i) < 70):
        mode_range["60-70"] = mode_range["60-70"] + occurence
    elif(70 < float(i) < 80): 
        mode_range["70-80"] = mode_range["70-80"] + occurence

mode, mode_info = 0, 0
for i, occurence in mode_range.items():
    if(occurence > mode_info):
        mode, mode_info = [int(i.split("-")[0]), int(i.split("-")[1])], occurence

print("Mode: ", mode)