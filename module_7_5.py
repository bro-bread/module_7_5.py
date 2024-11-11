import os

directory = os.path.join(".")
for i in os.walk(directory):
    print(i)
print(" ")
print(os.path.getmtime(directory))
print(" ")
print(os.path.getsize(directory))
print(" ")
print(os.path.dirname(directory))
