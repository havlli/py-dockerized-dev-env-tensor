import transformers
import sys

print(f"--- Hugging Face Transformers Installation Test ---")
print(f"Python version: {sys.version}")
print(f"Transformers version: {transformers.__version__}")

print("\nAttempting to load a default pipeline (sentiment-analysis)...")
print("(This might download a small model if run for the first time)")

try:
    # Load a default pipeline (usually lightweight)
    pipe = transformers.pipeline("sentiment-analysis")
    print(f"[SUCCESS] Successfully loaded pipeline: {pipe.model.__class__.__name__}")

    # Optional: Test the pipeline
    # result = pipe("This is a test sentence.")
    # print(f" Pipeline test result: {result}")

except Exception as e:
    print(f"[ERROR] Failed to load transformers pipeline: {e}")