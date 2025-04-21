import torch
import sys

print(f"--- PyTorch Installation Test ---")
print(f"Python version: {sys.version}")
print(f"PyTorch version: {torch.__version__}")

print("\nChecking for CUDA (GPU support)...")

if torch.cuda.is_available():
    print("[SUCCESS] CUDA is available!")
    print(f"CUDA version detected by PyTorch: {torch.version.cuda}")
    device_count = torch.cuda.device_count()
    print(f"Number of GPUs available: {device_count}")
    if device_count > 0:
        current_device = torch.cuda.current_device()
        print(f"Current GPU index: {current_device}")
        print(f"GPU Name: {torch.cuda.get_device_name(current_device)}")

        # Perform a simple GPU tensor operation
        try:
            print("\nAttempting a simple tensor operation on GPU...")
            # Create tensors on the GPU
            a = torch.tensor([1.0, 2.0], device='cuda')
            b = torch.tensor([3.0, 4.0], device='cuda')
            c = a + b
            print(f" Tensor a (GPU): {a}")
            print(f" Tensor b (GPU): {b}")
            print(f" Result c=a+b (GPU): {c}")
            print("[SUCCESS] Simple GPU tensor operation successful.")
        except Exception as e:
            print(f"[ERROR] GPU tensor operation failed: {e}")
    else:
        print("[INFO] No GPUs reported by CUDA, cannot perform GPU test.")
else:
    print("[INFO] CUDA is not available. PyTorch will run on CPU.")
    # Perform a simple CPU tensor operation
    try:
        print("\nAttempting a simple tensor operation on CPU...")
        a = torch.tensor([1.0, 2.0])
        b = torch.tensor([3.0, 4.0])
        c = a + b
        print(f" Tensor a (CPU): {a}")
        print(f" Tensor b (CPU): {b}")
        print(f" Result c=a+b (CPU): {c}")
        print("[SUCCESS] Simple CPU tensor operation successful.")
    except Exception as e:
        print(f"[ERROR] CPU tensor operation failed: {e}")
