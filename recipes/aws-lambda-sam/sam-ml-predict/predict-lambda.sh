#!/usr/bin/env bash

# POST method predict.  Put your lambda function here
curl -d '{  
   "Weight":200
}'\
     -H "Content-Type: application/json" \
     -X POST https://agdarbaa12.execute-api.us-east-1.amazonaws.com/Prod/predict