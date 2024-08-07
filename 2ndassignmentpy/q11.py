# Get a List def get_user_input():
    values = []
    while True:
        user_input = input("Enter a value: ")
        if user_input == "":
            break
        values.append(user_input)
    print("Here's the list:", values)

# Run function
get_user_input()
