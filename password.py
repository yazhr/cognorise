import random
import string

def generate_password(length):
    # Define characters to choose from for generating the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def get_valid_length():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        length = get_valid_length()

        # Generate the password
        password = generate_password(length)

        # Display the generated password
        print("Generated Password:", password)

        # Ask user if they want to generate another password
        choice = input("Do you want to generate another password? (Yes/No): ").lower()
        if choice != "yes":
            break

    print("Thank you for using the Password Generator!")

if _name_ == "_main_":
    main()
