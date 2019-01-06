import datetime
import json

f = open("/home/user/Desktop/demofile.txt", "r")
print(f.read())

f = open("/home/user/Desktop/demofile.txt", "r")
print(f.read(5))

f = open("/home/user/Desktop/demofile.txt", "r")
print(f.readline())

f = open("/home/user/Desktop/demofile.txt", "r")
for x in f:
	print(x)

f = open("/home/user/Desktop/demofile.txt", "a")
f.write("Now the file has one more line!")

f = open("/home/user/Desktop/newFile.txt", "x")
f = open("/home/user/Desktop/newFile.txt", "w")
f.write("Woops! I have deleted the content!")

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

# JSON to Python:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])

#Python to JSON
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)
