import json

# String to dictonary
x = '{"id": 10, "name": "Amit", "city": "Sangli"}'
y = json.loads(x)
print(y)
print(y['name'])


# Dictionary to JSON
z = {
        "id": 10, 
        "name": "Amit Patil", 
        "city": [
            "Sangli", "Pune"
        ], 
        "Percentage": 66.00, 
        "status": True
}

w = json.dumps(z)
print(w)