import tensorflow as tf
import sys

print(f"--- TensorFlow Installation Test ---")
print(f"Python version: {sys.version}")
print(f"TensorFlow version: {tf.__version__}")

print("\nChecking for GPU devices...")
gpu_devices = tf.config.list_physical_devices('GPU')

if gpu_devices:
    print(f"[SUCCESS] Found {len(gpu_devices)} GPU device(s):")
    for device in gpu_devices:
        print(f"  {device.name} - Type: {device.device_type}")

    # Perform a simple GPU tensor operation
    try:
        print("\nAttempting a simple tensor operation on GPU...")
        with tf.device('/GPU:0'):
            a = tf.constant([[1.0, 2.0], [3.0, 4.0]], dtype=tf.float32)
            b = tf.constant([[1.0, 1.0], [0.0, 1.0]], dtype=tf.float32)
            c = tf.matmul(a, b)
        print(f" Tensor a (GPU):\n{a}")
        print(f" Tensor b (GPU):\n{b}")
        print(f" Result c=a*b (GPU):\n{c}")
        print("[SUCCESS] Simple GPU tensor operation successful.")
    except Exception as e:
        print(f"[ERROR] GPU tensor operation failed: {e}")
else:
    print("[INFO] No GPU devices found by TensorFlow. TensorFlow will run on CPU.")
    # Perform a simple CPU tensor operation
    try:
        print("\nAttempting a simple tensor operation on CPU...")
        a = tf.constant([[1.0, 2.0], [3.0, 4.0]], dtype=tf.float32)
        b = tf.constant([[1.0, 1.0], [0.0, 1.0]], dtype=tf.float32)
        c = tf.matmul(a, b)
        print(f" Tensor a (CPU):\n{a}")
        print(f" Tensor b (CPU):\n{b}")
        print(f" Result c=a*b (CPU):\n{c}")
        print("[SUCCESS] Simple CPU tensor operation successful.")
    except Exception as e:
        print(f"[ERROR] CPU tensor operation failed: {e}") 