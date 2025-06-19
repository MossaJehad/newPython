
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

def calculate_tax(price, tax):
    return (price * (tax/100))

def apply_discount(price, disc):
    if(price > 100):
        return (price / disc)
    return 0

def final_price(price):
    disc = apply_discount(price, 10)
    tax = calculate_tax(price, 12)
    return ((price - disc) + tax)


def user_input():
    print("==============================================================================")
    print("  Welcome to our store please enter the index of the product you want to buy  ")
    print("==============================================================================")
    
    for prod, price in onlineStore.items():
        if (type(price) == dict):
            for subProd, subPrice in price.items():
                print(f" • Product: {subProd} --- Price: ${subPrice}")
        else:
            print(f"Product: {prod} --- Price: ${price}")

    prodIndex = input("Please choose the index: ")
    keys = list(onlineStore.keys())
    values = list(onlineStore.values())

    try:
        prodIndex = int(prodIndex)
    except ValueError: 
        print("Please enter a valid number")
        exit()
    if (prodIndex < 1 or prodIndex > len(onlineStore)):
        print("Please enter a valid number")
        exit()

    if(prodIndex == len(onlineStore)):
        price = values[prodIndex - 1]
        for subProd, subPrice in price.items():
            print(f"Product: {subProd} --- Price: ${subPrice}")
        keys = list(price.keys())
        values = list(price.values())
        total = sum(values)
        print(f"Products    Combined Price: ${total}")

        tax = calculate_tax(total, 12)
        discount = apply_discount(total, 10)
        final = final_price(total)

    else:
        total = values[prodIndex - 1]
        print(f"""
Product: {keys[prodIndex - 1]}
Original Price: {total}""")

    tax = calculate_tax(total, 12)
    discount = apply_discount(total, 10)
    final = final_price(total)

    print(f"""Tax: ${tax} 
Discount: ${discount} 
Final Price: ${final}
""")

user_input()

