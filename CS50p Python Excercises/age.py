def main():
    name = input("What's your name? ")
    hobby1 = input("What's one of your favorite hobbies? ")
    hobby2 = input("What's another hobby you enjoy? ")
    greet(name, hobby1, hobby2)

def greet(name, hobby1, hobby2):
    hobby_message = hobby1 + " and " + hobby2 + " sound like fun hobbies!"
    if hobby1 == hobby2:
        print(f"Wow, you must really love {hobby1}!")
    else:
        print(f"Nice to meet you, {name}! {hobby_message}")
main()
