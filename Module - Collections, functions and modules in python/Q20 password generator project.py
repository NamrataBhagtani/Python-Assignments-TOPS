''' Make a program to generate a strong password using the input given by the user. To generate a password, randomly take some words from the user input and then include numbers, special characters and capital letters to generate the password. Also, keep a check that password length is more than 8 characters.
Note: Include Exception handling wherever required. Also, make a ‘User’ class and store the details like user id, name and password of each user as a tuple. '''

import random
import string

class User:
    def __init__(self, user_id, name, password):
        self.user_id = user_id
        self.name = name
        self.password = password

    def get_details(self):
        return (self.user_id, self.name, self.password)

def generate_strong_password(user_input):
    words = user_input.split()
    
    if len(words) < 2:
        raise ValueError("Input should contain at least two words to generate a strong password.")
    
    random_words = random.sample(words, min(len(words), 3))
    password = ''.join(random_words)
    
    if len(password) < 8:
        additional_chars = 8 - len(password)
        password += ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=additional_chars))
    
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    if not any(char.isdigit() for char in password):
        password += random.choice(string.digits)
    if not any(char.isupper() for char in password):
        password += random.choice(string.ascii_uppercase)
    if not any(char in string.punctuation for char in password):
        password += random.choice(string.punctuation)
    
    while len(password) < 8:
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    
    password = ''.join(random.sample(password, len(password)))
    
    return password

def main():
    try:
        user_id = input("Enter user ID: ")
        name = input("Enter your name: ")
        user_input = input("Enter some words to generate a password: ")
        
        password = generate_strong_password(user_input)
        
        user = User(user_id, name, password)
        
        print("User created successfully!")
        print(f"User Details: {user.get_details()}")
        
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
