person = {
    "Name": "John Doe",
    "age": 17,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "postal_code": "12345"
    },
    "contact": [
        {
            "type": "email",
            "value": "johndoe@example.com"
        },
        {
            "type": "phone",
            "value": "555-123-4567"
        }
    ]
}

print(person["name"])
print(person["age"])
print(person["address"]["city"])
print(person["contact"][1]["value"])
print(person["contact"][1]["value"][0])