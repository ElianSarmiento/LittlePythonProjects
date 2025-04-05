def main():
    fruit_prices = {"Apple": 1.50, "Banana": 0.75, "Orange": 1.25}
    fruit = input("Enter a fruit: ")
    item(fruit_prices, fruit)

def item(fruit_prices, fruit):
    if fruit in fruit_prices:
        print(f"The price of {fruit} is ${fruit_prices[fruit]:.2f}")
    else:
        print("Sorry we don't have that fruit")





main()
