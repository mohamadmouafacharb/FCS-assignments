Numbers = [-12, 4, 12, 25, 67]

while Numbers != -99:
    user_input = int(input("Enter number:"))
    if user_input == -99:
        break
    Numbers.append(user_input)
    Numbers.sort()
    print(Numbers)