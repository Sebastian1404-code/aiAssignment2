from FileManager import FileManager
from encription import EncryptionManager
from Usermanager import UserManager

def menu():
    # Initialize the managers
    file_manager = FileManager("passwords.txt")
    encryption_manager = EncryptionManager()
    user_manager = UserManager(file_manager, encryption_manager)

    while True:
        print("\nPassword Manager")
        print("1. Register")
        print("2. View Password")
        print("3. Change Password")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_manager.register(username, password)
        elif choice == "2":
            username = input("Enter username: ")
            password = user_manager.view_password(username)
            if password:
                print(f"Your password is: {password}")
        elif choice == "3":
            username = input("Enter username: ")
            old_password = input("Enter old password: ")
            new_password = input("Enter new password: ")
            user_manager.change_password(username, old_password, new_password)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
if __name__ == "__main__":
    menu()
