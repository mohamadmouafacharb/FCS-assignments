Names = ["Maria", "Hala", "Ghady", "Ehsan", "Joe", "Zoe"]

while True:
    inserted_letter = input("Enter letter:")
    for name in Names:
        if inserted_letter.lower() in name.lower():
            print(name)
    user_response = input("Do you want to enter another letter? (yes/no):")
    if user_response.lower() == "yes":
        continue  
    if user_response.lower() == "no":
        break 
    else:
        print("Invalid response")