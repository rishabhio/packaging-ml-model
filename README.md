# packaging-ml-model
Learn how to package a machine learning model into a container



# Steps to use the repository

1. Clone the repository 
2. Create a virtual environment ( to isolate the dependencies ) 
3. Install the requirements with the following command: 

```

pip install -r requirements.txt 
```

# Build the model file 
1. Execute the following command to build the model 

```
python model.py 

```

- This will build the model and serialize it into a file called 
as model.joblib, this is what we'll load into memory when we 
build our inference API via fastAPI 

# Build a fastAPI based app

- The source code for this is available in the app.py file 
- You can check whether it's working by executing the following 
    command: 

```
uvicorn main:app --reload

```

# Generate a Docker file 

Generate Dockerfile in the same directory as the app and add the 
following contents to it: 

```

# Use Python base image
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy requirements.txt to container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI app files to the container
COPY app /app

# Expose port 80 for FastAPI app
EXPOSE 80

# Command to start the FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

```

# Build the Docker Image from the instructions given in the Dockerfile 

```
docker build -t packaged-model-001 .
```

# Build the container out of the image 
```
docker run -p 8000:80 packaged-model-001
```


# Verify whether the container is running 

- Use postman to call the post end-point available at localhost:8000/predict 

```

{
    "sepal_length": 2,
    "sepal_width": 3.0,
    "petal_length": 4.0,
    "petal_width": 1.5
}

```


# push the image to docker registry 

1. Login to Docker 

```

docker login

```

- The above command should show text like the following: 

```
Log in with your Docker ID or email address to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com/ to create one.
You can log in with your password or a Personal Access Token (PAT). Using a limited-scope PAT grants better security and is required for organizations using SSO. Learn more at https://docs.docker.com/go/access-tokens/

Username: 
```

- Use the PAT as the password 
** Note: You can also use your password but the use of PAT with minimal access is recommended. 


# Create a repository on DockerHub 

```
1. Go to Dockerhub ( search on Google ) 

2. Create an Account if not already existing

3. Create a new Repository 

```


# Tag your local image 

```

docker tag packaged-model-001:latest riio/packaged-model-001:latest

```


## Push the image to DockerHub 

```
docker push riio/packaged-model-001:latest
```


## Sample Output: 

```

(venv) username@machine packaging-ml-model % docker push riio/packaged-model-001:latest
The push refers to repository [docker.io/riio/packaged-model-001]
fd749012a9d2: Pushed 
963141bae3f4: Pushing  253.5MB
4f83a3ffc58c: Pushed 
7b34bc82ecfd: Pushed 
b958f60e4e67: Pushed 
f02ce41627b1: Pushed 
eeac00a5e55e: Pushed 
34e7752745be: Pushed 
8560597d922c: Pushing  100.2MB
```


## Congratulations.

- You just packaged your machine learning model and made it available to the world with the power of containers. 

## How anybody can use your packaged model? 

It's simple

```
docker pull riio/packaged-model-001:latest 

```


## How to run the container ? 

```

docker run -p 8000:80 riio/packaged-model-001:latest
```

