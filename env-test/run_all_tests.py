import subprocess
import sys
import os

# Define the directory where test scripts are located
TEST_DIR = os.path.dirname(__file__)

# List of test scripts to run (ensure names are correct)
TEST_SCRIPTS = [
    "tensor_test.py",
    "torch_test.py",
    "tvision_test.py",
    "transformers_test.py",
]

print("--- Running All Environment Checks ---")
all_passed = True

for script_name in TEST_SCRIPTS:
    script_path = os.path.join(TEST_DIR, script_name)
    print(f"\n{'='*10} Starting Test: {script_name} {'='*10}")
    print(f"Executing: python {script_path}")

    try:
        # Use subprocess.run to execute the script
        # check=True will raise CalledProcessError if the script exits with non-zero code
        # capture_output=True redirects stdout/stderr
        # text=True decodes stdout/stderr as text
        result = subprocess.run(
            [sys.executable, script_path], # Use sys.executable to ensure the correct python interpreter
            check=True,
            capture_output=True,
            text=True,
            cwd=TEST_DIR # Run script from its directory if needed, though not strictly necessary here
        )
        # Print the script's output
        print(result.stdout.strip())
        print(f"[SUCCESS] {script_name} completed successfully.")

    except subprocess.CalledProcessError as e:
        # Print error output if the script failed
        print("--- Test Output START (Error) ---")
        print(e.stdout.strip())
        print(e.stderr.strip()) # Print standard error as well
        print(f"[FAILURE] {script_name} failed with exit code {e.returncode}.")
        all_passed = False
        # Optional: break here if you want to stop on the first failure
        # break
    except FileNotFoundError:
        print(f"[FAILURE] Could not find test script: {script_path}")
        all_passed = False
        # Optional: break here
        # break
    except Exception as e:
        # Catch any other unexpected errors during subprocess execution
        print(f"[FAILURE] An unexpected error occurred while running {script_name}: {e}")
        all_passed = False
        # Optional: break here
        # break
    print(f"{'='*10} Finished Test: {script_name} {'='*10}")

print("\n--- All Checks Complete ---")

if all_passed:
    print("[OVERALL SUCCESS] All environment checks passed.")
    sys.exit(0) # Exit with success code
else:
    print("[OVERALL FAILURE] One or more environment checks failed.")
    sys.exit(1) # Exit with failure code
