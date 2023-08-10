# Dockerized Machine Learning Model

Context, I am a complete noob and don't really use docker that much so here is a tiny project. 

## Prerequisites

- Docker
- Git

## Getting Started

1. **Clone the repository**:
   ```
   git clone https://github.com/mianni1/ml_docker_project.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd ml_docker_project
   ```

3. **Build the Docker image**:
   ```bash
   docker build -t ml_docker_project .
   ```

4. **Run the Docker container**:
   ```bash
   docker run -it ml_docker_project
   ```

   You should see an output like:
   ```
   Accuracy: 1.0
   ````

## Project Structure

- `Dockerfile`: Defines the Docker container and how to build it.
- `train_model.py`: Contains the code for training the machine learning model.
- `predict.py`: Contains the code for making predictions with the trained model.
- `README.md`: This file, explaining the project.
