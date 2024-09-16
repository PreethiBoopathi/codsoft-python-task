import random
import string

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    if length < 8:
        print("Password length should be at least 8 characters.")
        return None
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

def main():
    while True:
        print("\n1. Generate Password")
        print("2. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            length = int(input("Enter the desired length of the password: "))
            password = generate_password(length)
            if password:
                print("Generated Password : ", password)
        elif choice == "2":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()



