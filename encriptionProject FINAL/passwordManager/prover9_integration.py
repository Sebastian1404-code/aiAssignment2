# prover9_integration.py
import subprocess

def run_prover9(input_file="encryption_logic.in"):
    """
    Runs Prover9 with the given input file and captures its output.
    """
    try:
        result = subprocess.run(
            ["/mnt/d/UTCN/an3sem1/AI/LADR-2009-11A/bin/prover9", "-f", input_file],  #modify with your prover9's path
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if result.returncode == 0:
            print("Prover9 executed successfully!")
            return result.stdout
        else:
            print("Prover9 encountered an error!")
            print("Error:", result.stderr)
            return None
    except FileNotFoundError:
        print("Prover9 is not installed or not in PATH!")
        return None

def validate_logic(password):
    """
    Validates the encryption logic for a given password using Prover9.
    """
    from encription import generate_prover9_input

    # Generate the Prover9 input file
    generate_prover9_input(password)

    # Run Prover9 and check the output
    output = run_prover9()
    if output and "THEOREM PROVED" in output:
        print("Encryption logic validated successfully!")
        return True
    else:
        print("Failed to validate encryption logic!")
        return False
