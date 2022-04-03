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