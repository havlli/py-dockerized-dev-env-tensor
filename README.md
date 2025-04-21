# Dockerized ML Development Environment (TensorFlow Base + PyTorch & Hugging Face)

This project provides a reproducible and GPU-accelerated development environment for Machine Learning tasks, orchestrated using Docker Compose. It leverages the official TensorFlow GPU image as a base and adds key libraries like PyTorch and Hugging Face Transformers, making it suitable for multi-framework development.

## Purpose

The main goal is to offer a consistent, containerized environment with essential ML tools pre-installed and configured, eliminating the need for manual setup on different machines. It's designed for developers working with TensorFlow, PyTorch, and the Hugging Face ecosystem, providing seamless access to GPU resources.

## Core Components & Features

*   🐳 **Base Image:** Official `tensorflow/tensorflow:latest-gpu` with CUDA pre-configured.
*   🧱 **Multi-Framework:** Includes PyTorch, Hugging Face suite, and TensorFlow.
*   📊 **Essential Libraries:** Includes `pandas`, `scikit-learn`, `matplotlib`, `seaborn`.
*   🚀 **GPU Acceleration:** Configured for NVIDIA GPU usage.
*   📓 **Jupyter Notebook:** Interactive development via JupyterLab/Notebook.
*   💡 **Optimized TensorBoard:** Runs in a separate lightweight container for efficiency.
*   ✅ **Startup Checks:** Verifies core libraries (TF, PyTorch, etc.) on container start.
*   ⚙️ **Docker Compose Orchestration:** Manages `dev` and `tensorboard` services.

## Prerequisites

*   **Docker Engine:** [Install Docker](https://docs.docker.com/engine/install/)
*   **Docker Compose:** Typically included with Docker Desktop, otherwise [Install Compose](https://docs.docker.com/compose/install/).
*   **NVIDIA GPU:** A CUDA-compatible NVIDIA graphics card.
*   **NVIDIA Drivers:** Appropriate NVIDIA drivers installed on the host machine.
*   **GPU Passthrough Setup:**
    *   **Linux:** [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) installed.
    *   **Windows:** WSL 2 backend enabled in Docker Desktop with compatible NVIDIA drivers (supporting WSL 2) installed.

## Project Structure

```
.
├── Dockerfile            # Defines the main ML development image (FROM tensorflow:latest-gpu)
├── Dockerfile.tensorboard # Defines the lightweight image for the TensorBoard service
├── docker-compose.yml    # Orchestrates the 'dev' and 'tensorboard' services
├── requirements.txt      # Lists *additional* Python packages installed on top of the base TF image
├── env-test/             # Contains scripts to verify the environment setup
│   ├── run_all_tests.py  # Script to execute all checks (run on startup)
│   ├── tensor_test.py    # TensorFlow check script
│   ├── torch_test.py     # PyTorch check script
│   ├── tvision_test.py   # Torchvision check script
│   └── transformers_test.py # Hugging Face Transformers check script
├── src/                    # Example directory for your project source code
├── notebooks/             # Example directory for your Jupyter notebooks
├── data/                  # Example directory for datasets
└── logs/                  # Directory for storing training logs (used by TensorBoard)
```

## Getting Started

1.  **Clone the Repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```
2.  **Build and Start Services:**
    Run the following command from the project root directory:
    ```bash
    docker-compose up --build -d
    ```
    *   `--build`: Ensures the images are built (or rebuilt if changes were made).
    *   `-d`: Runs the containers in detached mode (in the background).

3.  **Startup Checks:** When the `dev-environment` container starts, it will automatically execute the scripts in `env-test/` via `run_all_tests.py`. Check the logs to ensure all tests pass:
    ```bash
    docker-compose logs -f dev-environment
    ```
    Look for `[OVERALL SUCCESS] All environment checks passed.` before the Jupyter startup messages.

4.  **Access Services:**
    *   **Jupyter Notebook:** Open your web browser to `http://localhost:8888`
    *   **TensorBoard:** Open your web browser to `http://localhost:6006`

## Development Workflow

*   **Primary Container:** Most development happens within the `dev-environment` container, accessed via Jupyter or `docker-compose exec`.

### Using VSCode based IDE with Dev Containers (Recommended)

For a fully integrated IDE experience where VS Code base IDE runs directly against the container's environment (seeing all installed libraries, Python interpreter, etc.), you can use the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):

1.  **Install Extension:** Make sure you have the "Dev Containers" extension installed in VS Code.
2.  **Ensure Container is Running:** Start your services if they aren't running: `docker-compose up -d`.
3.  **Attach to Container:**
    *   Open the Command Palette (usually `Ctrl+Shift+P` or `Cmd+Shift+P`).
    *   Type and select "**Dev Containers: Attach to Running Container...**".
    *   Choose the running `dev-environment` container from the list.
4.  **Develop:** VS Code will open a new window connected to the container. The integrated terminal, debugger, Python interpreter selection, and language features will all operate *inside* the container, providing direct access to all installed tools and libraries.

*   **Executing Commands:** To run commands inside the main development container:
    ```bash
    docker-compose exec dev-environment <your_command>
    # Example: Run the environment checks manually
    docker-compose exec dev-environment python /app/env-test/run_all_tests.py
    # Example: Get an interactive shell
    docker-compose exec dev-environment bash
    ```
*   **Adding Python Dependencies:**
    1.  Add the required package(s) to `requirements.txt`.
    2.  Rebuild the `dev` service image: `docker-compose build dev-environment` or simply run `docker-compose up --build -d` again.
*   **Adding System Dependencies:** If you need tools installable via `apt-get`:
    1.  Modify the `Dockerfile` to include the necessary `apt-get install` commands (remember `apt-get update` first and potentially cleanup afterwards).
    2.  Rebuild the image: `docker-compose build dev-environment` or `docker-compose up --build -d`.
*   **Stopping Services:**
    ```bash
    docker-compose down
    ```
    Use `docker-compose down -v` to also remove the volumes (if any were defined as named volumes, which is not the case here).

## GPU Support

GPU access is enabled through:
1.  Using the `tensorflow/tensorflow:latest-gpu` base image which includes CUDA libraries.
2.  The `deploy` section within the `dev` service definition in `docker-compose.yml`, which requests GPU resources from Docker.
3.  Proper configuration of NVIDIA drivers and the NVIDIA Container Toolkit / WSL 2 setup on the host machine.

The environment test scripts (`tensor_test.py`, `torch_test.py`) include checks for GPU availability and perform simple operations to verify access.

## TensorBoard Service

The `tensorboard` service runs in a separate, minimal container defined by `Dockerfile.tensorboard`. It mounts the same project directory (`.:/app`) as the `dev` service, allowing it to read log files written to the `/app/logs` directory (corresponding to the `logs/` folder on your host) by your training scripts running in the `dev` container.

## License

This project template is available under the MIT License. 