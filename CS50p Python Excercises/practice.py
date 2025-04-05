def main():
    favorite_color = {"Alice": "Blue", "Elian": "Red"}
    name = input("Enter a name: ")
    person(favorite_color, name)

def person(favorite_color, name):
    if name in favorite_color:
        print(f"{name}'s favorite color is {favorite_color[name]}")
    else:
        print("Sorry, I don't know their favorite color. ")




main()
