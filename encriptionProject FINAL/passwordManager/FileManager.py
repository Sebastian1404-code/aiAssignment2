import os

class FileManager:
    """
    Manages file operations for storing and retrieving user data.
    """

    def __init__(self, filename="passwords.txt"):
        # Convert filename to absolute path
        self.filename = os.path.abspath(filename)

    def read_users(self):
        """
        Reads the username and encrypted password pairs from the file.
        Returns a dictionary with {username: encrypted_password}.
        """
        users = {}
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    # Validate that each line has a single ":"
                    if ":" in line:
                        username, encrypted_password = line.strip().split(":", 1)
                        users[username] = encrypted_password
                    else:
                        print(f"Skipping malformed line: {line.strip()}")
        except FileNotFoundError:
            pass  # If file doesn't exist, return an empty dictionary
        except Exception as e:
            print(f"Error reading file: {e}")
        return users

    def write_users(self, users):
        """
        Writes the username and encrypted password pairs to the file.
        """
        try:
            with open(self.filename, "w") as file:
                for username, encrypted_password in users.items():
                    file.write(f"{username}:{encrypted_password}\n")
        except Exception as e:
            print(f"Error writing to file: {e}")
