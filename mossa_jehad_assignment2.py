# customer counter is outside the function

customer_counter = 0

def add_cutomer():
    # here we use global to access and make changes to the variable
    global customer_counter
    customer_counter += 1;
    print(f"The current number of customers: ", customer_counter)

# called 2 times, so the output is 1, 2 customer respectively
add_cutomer()
add_cutomer()
