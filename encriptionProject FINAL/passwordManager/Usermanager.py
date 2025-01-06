from encription import validate_logic_with_prover9

class UserManager:
    """
    Handles user registration, password viewing, and password changes.
    """

    def __init__(self, file_manager, encryption_manager):
        self.file_manager = file_manager
        self.encryption_manager = encryption_manager

    def register(self, username, password):
        """
        Registers a new user by encrypting their password and storing it.
        Validates encryption-decryption logic with Prover9.
        """
        users = self.file_manager.read_users()
        if username in users:
            print("Username already exists! Choose another.")
            return

        # Validate encryption-decryption logic with Prover9
        if not validate_logic_with_prover9(password):
            print("Encryption-decryption logic validation failed. Registration aborted.")
            return

        encrypted_password = self.encryption_manager.encrypt(password)
        users[username] = encrypted_password
        self.file_manager.write_users(users)
        print("User registered successfully!")

    def view_password(self, username):
        """
        Retrieves and decrypts the password for a given username.
        """
        users = self.file_manager.read_users()
        if username in users:
            encrypted_password = users[username]
            return self.encryption_manager.decrypt(encrypted_password)
        else:
            print("Username not found!")
            return None

    def change_password(self, username, old_password, new_password):
        """
        Changes the user's password after verifying the old password.
        Validates encryption-decryption logic with Prover9.
        """
        users = self.file_manager.read_users()
        if username not in users:
            print("Username not found!")
            return

        encrypted_password = users[username]
        if self.encryption_manager.decrypt(encrypted_password) == old_password:
            # Validate encryption-decryption logic for the new password
            if not validate_logic_with_prover9(new_password):
                print("Encryption-decryption logic validation failed. Password change aborted.")
                return

            new_encrypted_password = self.encryption_manager.encrypt(new_password)
            users[username] = new_encrypted_password
            self.file_manager.write_users(users)
            print("Password updated successfully!")
        else:
            print("Old password is incorrect!")
