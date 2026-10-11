def calc_discount(price, discount):
    test = "P@ss0rd"
    print(test)
    if not 0 <= discount <= 100:
        raise ValueError("Invalid Discount")
    return price - (price * discount / 100)

def get_results():
    return "Hello World"