import random
import string

def generate_password(length, complexity):
   
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = ""
    if "uppercase" in complexity:
        all_characters += uppercase_letters
    if "lowercase" in complexity:
        all_characters += lowercase_letters
    if "digits" in complexity:
        all_characters += digits
    if "special" in complexity:
        all_characters += special_characters

    password = "".join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter desired password length: "))
        complexity = input("Enter desired complexity:").split()
        password = generate_password(length, complexity)
        print(f"Generated password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid password length (integer).")

if __name__ == "__main__":
    main()
