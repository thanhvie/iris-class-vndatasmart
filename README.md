# iris-class-vndatasmart

<p>An Python application with full CI/CD pipeline</p>

# Run the app

## Run on local environment
```
python3 server.py
```
## Run with docker

### Step 1: Build docker image
```
docker image build -t <your-image-name> .
```
### Step 2: Run the container
```
docker run -p 5000:5000 -d <your-image-name>
```

## Run with docker-compose
```
docker-compose up
```

## You can also check in the app at link below
https://iris-class-vndatasmart.herokuapp.com/

## Setup for Amazon Lightsail

### Create service
```
aws lightsail create-container-service --service-name <your-service-name> --power small --scale 1
```

### Push container image
```
aws lightsail push-container-image --service-name <your-service-name> --label iris-container --image <your-image-name>
```

### Deployment
```
aws lightsail create-container-service-deployment --service-name <your-service-name> --containers file://containers.json --public-endpoint file://public-endpoint.json
```

### Get container information

```
aws lightsail get-container-services --service-name <your-service-name>
```