# SET VARIABLE user_prompt TO TRUE
user_prompt = True

# PUT BEGINNING OF WHILE LOOP HERE - SHOULD LOOP WHILE user_prompt IS TRUE
while user_prompt:
    age = input("What is your age? ")
# PUT IF STATEMENT HERE TO CHECK IF age IS ALL DIGITS
    if age.isdigit():
        age = int(age)
# SET user_prompt TO FALSE
        if age <= 117:
            user_prompt = False
# ADD ELSE STATEMENT HERE
        else:
            print("Your age is too high", age)

# TELL USER THE PROBLEM WITH THEIR INPUT
    else:
        print("enter a valid age")

print(f"Your age is {age}")