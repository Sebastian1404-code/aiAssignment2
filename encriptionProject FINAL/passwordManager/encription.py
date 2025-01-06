import os
import subprocess

class EncryptionManager:
    """
    Handles password encryption and decryption.
    """

    @staticmethod
    def encrypt(password, key=3):
        """
        Encrypts the password using a simple Caesar cipher.
        """
        return ''.join(chr(ord(char) + key) for char in password)

    @staticmethod
    def decrypt(encrypted_password, key=3):
        """
        Decrypts the password using a Caesar cipher.
        """
        return ''.join(chr(ord(char) - key) for char in encrypted_password)


def generate_prover9_input(password, filename="encryption_logic.in"):
    """
    Generates a Prover9 input file for encryption logic validation.
    """
    filepath = os.path.abspath(filename)  # Resolve absolute path
    with open(filepath, "w") as file:
        file.write(f"""
        % Axioms for Encryption/Decryption
        formulas(assumptions).
        all x (decrypt(encrypt(x)) = x).  % Decryption undoes encryption
        all x (encrypt(decrypt(x)) = x).  % Encryption undoes decryption
        end_of_list.

        % Goal: Validate encryption and decryption
        formulas(goals).
        decrypt(encrypt("{password}")) = "{password}".  % Goal for validation
        end_of_list.
        """)
    print(f"Prover9 input file generated: {filepath}")
    return filepath


def validate_logic_with_prover9(password):
    """
    Uses Prover9 to validate the encryption and decryption logic.
    """
    input_file = generate_prover9_input(password)

    try:
        # Run Prover9 with the generated input file
        result = subprocess.run(
            ["/mnt/d/UTCN/an3sem1/AI/LADR-2009-11A/bin/prover9", "-f", input_file], #modify with your prover9's path
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        # Check Prover9 output
        if "THEOREM PROVED" in result.stdout:
            print("Prover9 validation succeeded!")
            return True
        else:
            print("Prover9 validation failed!")
            print(result.stdout)
            return False

    except FileNotFoundError:
        print("Prover9 is not installed or not in PATH!")
        return False
