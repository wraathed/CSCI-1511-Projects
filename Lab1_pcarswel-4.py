'''
Program: Lab 1 option 4
Name: Tyson Fitzgerald
Desc: To demonstrate f strings to show amount of items in list (the car in the scenario) based on the list of strings, and to print in reverse order.
'''

items = [f"tent", "sleepingbag", "flashlight", "water", "knife", "fishingpole"]
numItems = len(items)
items.reverse()
reverseList = items

print(numItems)
print(reverseList)