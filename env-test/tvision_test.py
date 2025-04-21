import torchvision
import torch
import sys

print(f"--- Torchvision Installation Test ---")
print(f"Python version: {sys.version}")
print(f"PyTorch version: {torch.__version__}")
print(f"Torchvision version: {torchvision.__version__}")

print("\nAttempting to load a standard model architecture (ResNet18)...")

try:
    # Load the ResNet18 model architecture (weights not required for this test)
    model = torchvision.models.resnet18(weights=None)
    print(f"[SUCCESS] Successfully accessed torchvision.models.resnet18")
    # You could optionally print model structure here if needed:
    # print(model)
except Exception as e:
    print(f"[ERROR] Failed to access torchvision models: {e}")