def reverse_string(input_str):
    return input_str[::-1]


while True:
    user_input = input("Enter a string: ")

    if not user_input.isdigit():
        reversed_str = reverse_string(user_input)
        print("Output:", reversed_str)
        break

    print("Error Reported! Enter text only.")