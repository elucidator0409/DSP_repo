# How to run deploy the container image on ECR

## Steps
Step 1: Build the image with the name hello-lambda
```
docker build -t movie-recommender-image .
```

Step 2: Test run the image
```
docker run -p 9000:8080 movie-recommender-image
```

Step 2.1: Call the function using
```
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{ "queryStringParameters": { "query": "Girl got her revenge" } }'  
```

Step 3: Authenticate Docker CLI
```
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <AWS ACCOUNT ID>.dkr.ecr.<REGION>.amazonaws.com 
```
For instance
```
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 192384646739.dkr.ecr.us-east-1.amazonaws.com
``` 

Step 4: Create repository
```
aws ecr create-repository -—repository-name movie-recommender
```

Step 5: Create tag name for image
```
docker tag  hello-lambda:latest <AWS ACCOUNT ID>.dkr.ecr.<REGION>.amazonaws.com/hello-lambda:latest
```
AWS ACCOUNT ID: 935267206350
REGION: us-east-1
For instance
```
docker tag  movie-recommender-image:latest 192384646739.dkr.ecr.us-east-1.amazonaws.com/movie-recommender:latest
```

Step 6: Push repository
```
docker push 192384646739.dkr.ecr.us-east-1.amazonaws.com/movie-recommender-image:latest
```

Step 7: Create lambda function and attach repository

AWS Access key: AKIASZSYEXZJ24G3RILM
AWS Secret key: 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