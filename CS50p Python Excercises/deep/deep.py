def main():
    user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything?" )
    if answer(user_input):
        print("Yes")
    else:
         print("No")

def answer(a):
    a = a.strip().lower().replace(" ", "-")

    if a == "42" or a == "forty-two":
            return True
    else:
         return False
main()
