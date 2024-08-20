import random
import string

def generate_password(length):
    """Generate a random password of a specified length."""
    
    # Define the possible characters to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password using random choices from the characters
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Password Generator")
    
    try:
        # Prompt the user to enter the desired password length
        length = int(input("Enter the desired length of the password: "))
        
        if length <= 0:
            print("Password length must be greater than 0.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
