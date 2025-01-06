from encription import EncryptionManager, validate_logic_with_prover9
from FileManager import FileManager

def register(file_manager):
    """
    Registers a new user by encrypting their password and storing it.
    Validates the encryption logic with Prover9.
    """
    users = file_manager.read_users()
    username = input("Enter username: ")
    if username in users:
        print("Username already exists! Choose another.")
        return

    password = input("Enter password: ")

    # Validate encryption-decryption logic using Prover9
    if not validate_logic_with_prover9(password):
        print("Encryption-decryption logic validation failed. Registration aborted.")
        return

    encrypted_password = EncryptionManager.encrypt(password)
    users[username] = encrypted_password
    file_manager.write_users(users)
    print("User registered successfully!")


def validate_password(file_manager, username, old_password):
    """
    Validates the old password for a user.
    """
    users = file_manager.read_users()
    if username in users:
        encrypted_password = users[username]
        return EncryptionManager.decrypt(encrypted_password) == old_password
    return False


def change_password(file_manager, username, old_password, new_password):
    """
    Changes the user's password if the old password is correct.
    """
    if validate_password(file_manager, username, old_password):
        if validate_logic_with_prover9(new_password):  # Validate encryption logic for the new password
            encrypted_new = EncryptionManager.encrypt(new_password)
            users = file_manager.read_users()
            users[username] = encrypted_new
            file_manager.write_users(users)
            print("Password updated successfully!")
        else:
            print("Failed to validate encryption logic for the new password.")
    else:
        print("Old password does not match.")


def view_password(file_manager, username):
    """
    Retrieves and decrypts the password for a given user.
    """
    users = file_manager.read_users()
    if username in users:
        encrypted_password = users[username]
        return EncryptionManager.decrypt(encrypted_password)
    print("Username not found!")
    return None
