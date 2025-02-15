import os
import subprocess
import sys

def run_command(command):
    """Run a shell command and return the exit code."""
    result = subprocess.run(command, shell=True)
    return result.returncode

def run_linter():
    print("Running linter (flake8)...")
    exit_code = run_command("flake8 app tests")
    if exit_code != 0:
        print("Linting failed!")
        sys.exit(exit_code)
    print("Linting passed ✅")

def run_tests():
    print("Running tests...")
    exit_code = run_command("python -m unittest discover tests")
    if exit_code != 0:
        print("Tests failed!")
        sys.exit(exit_code)
    print("All tests passed ✅")

if __name__ == "__main__":
    print("Starting Continuous Integration Pipeline...\n")
    run_linter()
    run_tests()
    print("\nCI Pipeline Completed Successfully 🎉")
