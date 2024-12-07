import random
import string

def generate_password(length):
    # Define the characters that can be used in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly choose characters to create the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    print("Password Generator")
    
    # Get the desired password length from the user
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 6:
            print("Password length should be at least 6 characters for better security.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    
    # Generate and display the password
    password = generate_password(length)
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
