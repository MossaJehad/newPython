
onlineStore = {
    "Mouse": 25,
    "Laptop": 500,
    "Headphones": 80,
    "Keyboard": 45,
    "NewItems": {
        "MotherBoard": 55,
        "PowerSupply": 22
    }
}


# In dictonaries you can add a dictonary inside another

print(onlineStore["Mouse"])

for prod, price in onlineStore.items():
    if (type(price) == dict):
        for subProd, subPrice in price.items():
             print(f" • Product: {subProd} --- Price: ${subPrice}")
    else:
        print(f"Product: {prod} --- Price: ${price}")
