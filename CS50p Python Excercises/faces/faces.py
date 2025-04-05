def convert():
    user_input = input("Enter text: ")
    user_input = user_input.replace(":)", "🙂")
    user_input = user_input.replace(":(", "🙁")
    print(user_input)
convert()
