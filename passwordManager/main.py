from cryptography.fernet import Fernet

# Function to write the key to a file
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the encryption key from a file
def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

# Uncomment to generate and store a new key (only needed once)
# write_key()

# Load the existing encryption key
key = load_key()
f = Fernet(key)

# Function to view stored passwords
def view_pass():
    try:
        with open("passwords.txt", "r") as file:
            if file.readable():
                for line in file.readlines():
                    data = line.strip()
                    user, encrypted_pass = data.split("|")
                    decrypted_pass = f.decrypt(encrypted_pass.encode()).decode()  # Decrypt the password
                    print(f"Username: {user.strip().ljust(20)} Password: {decrypted_pass.strip()}")
            else:
                print("No users found. Please add a user.")
    except FileNotFoundError:
        print("No passwords stored yet.")
    except Exception as e:
        print(f"Error: {e}")

# Function to add new passwords
def add_pass():
    name = input("Account name: ")
    password = input("Enter password: ")
    encrypted_pass = f.encrypt(password.encode()).decode()  # Encrypt the password
    with open("passwords.txt", "a") as file:
        file.write(f"{name} | {encrypted_pass}\n")

# Main loop
while True:
    mode = input("Would you like to add a new password or view existing (view, add, q to quit): ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view_pass()
    elif mode == "add":
        add_pass()
    else:
        print("Invalid mode. Please choose view, add, or q.")
