[![Python application test with Github Actions](https://github.com/noahgift/Python-MLOps-Cookbook/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/noahgift/Python-MLOps-Cookbook/actions/workflows/pythonapp.yml)


# Python MLOps Cookbook 
This is an example of a Containerized Flask Application the can be the core ingrediant in many "recipies", i.e. deploy targets.

![9781098103002](https://user-images.githubusercontent.com/58792/111000927-eb1b7680-8350-11eb-8e24-d41064590fc1.jpeg)


## Assets in repo

* `Makefile`:  [View Makefile](https://github.com/noahgift/Python-MLOps-Cookbook/blob/main/Makefile)
* `requirements.txt`:  [View requirements.txt](https://github.com/noahgift/Python-MLOps-Cookbook/blob/main/requirements.txt)
* `cli.py`: [View cli.py](https://github.com/noahgift/Python-MLOps-Cookbook/blob/main/cli.py)
* `utilscli.py`: [View utilscli.py](https://github.com/noahgift/Python-MLOps-Cookbook/blob/main/utilscli.py)
* `app.py`:  [View app.py](https://github.com/noahgift/Python-MLOps-Cookbook/blob/main/app.py)
* `mlib.py`:  Model Handling Library
* `htwtmlb.csv`: [View CSV](https://github.com/noahgift/Python-MLOps-Cookbook/blob/main/htwtmlb.csv) Useful for input scaling
* `model.joblib`: [View model.joblib](https://github.com/noahgift/Python-MLOps-Cookbook/raw/781053e4d45ebeeb64ecdf2dc1b896b338530aab/model.joblib)
* `Dockerfile`:  [View Dockerfile](https://github.com/noahgift/Python-MLOps-Cookbook/blob/main/Dockerfile)
*  `Baseball_Predictions_Export_Model.ipynb`:  [Baseball_Predictions_Export_Model.ipynb](https://github.com/noahgift/Python-MLOps-Cookbook/blob/main/Baseball_Predictions_Export_Model.ipynb)

![Course2-Duke-Flask-Containerized](https://user-images.githubusercontent.com/58792/110816231-289cd880-8259-11eb-8ab7-45c4ef5190ad.png)

### CLI Tools

There are two cli tools.  First, the main `cli.py` is the endpoint that serves out predictions.
To predict the height of an MLB player you use the following: ` ./cli.py --weight 180`

![predict-height-weight](https://user-images.githubusercontent.com/58792/110970118-6c5e1380-8327-11eb-95b2-aeba679c0270.png)

The second cli tool is `utilscli.py` and this perform model retraining, and could serve as the entry point to do more things.
For example, this version doesn't change the default `model_name`, but you could add that as an option by forking this repo.

`./utilscli.py retrain --tsize 0.4`

Here is an example retraining the model.
![model-retraining](https://user-images.githubusercontent.com/58792/110986838-31b2a600-833c-11eb-977f-13143d4471c7.png)

### Flask Microservice

The Flask ML Microservice can be run many ways.

#### Containerized Flask Microservice Locally

You can run the Flask Microservice as follows with the commmand: `python app.py`.

```
(.venv) ec2-user:~/environment/Python-MLOps-Cookbook (main) $ python app.py 
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
INFO:werkzeug: * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
INFO:werkzeug: * Restarting with stat
WARNING:werkzeug: * Debugger is active!
INFO:werkzeug: * Debugger PIN: 251-481-511
```

To serve a prediction against the application, run the `predict.sh`.


```
(.venv) ec2-user:~/environment/Python-MLOps-Cookbook (main) $ ./predict.sh                             
Port: 8080
{
  "prediction": {
    "height_human_readable": "6 foot, 2 inches", 
    "height_inches": 73.61
  }
}
```


#### Containerized Flask Microservice

Here is an example of how to build the container and run it locally, this is the contents of [predict.sh](https://github.com/noahgift/Python-MLOps-Cookbook/blob/main/predict.sh)

```
#!/usr/bin/env bash

# Build image
#change tag for new container registery, gcr.io/bob
docker build --tag=noahgift/mlops-cookbook . 

# List docker images
docker image ls

# Run flask app
docker run -p 127.0.0.1:8080:8080 noahgift/mlops-cookbook
```

#### Automatically Build Container via Github Actions and Push to Container Registery

To setup the container build process do the following.  This is also covered by Alfredo Deza in Practical MLOps book in greater detail.

```
  build-container:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Loging to Github registry
      uses: docker/login-action@v1
      with:
        registry: ghcr.io
        username: ${{ github.repository_owner }}
        password: ${{ secrets.BUILDCONTAINERS }}
    - name: build flask app
      uses: docker/build-push-action@v2
      with:
        context: ./
        #tags: alfredodeza/flask-roberta:latest
        tags: ghcr.io/noahgift/python-mlops-cookbook:latest
        push: true 
    
```

![container-registry](https://user-images.githubusercontent.com/58792/111001486-d8ee0800-8351-11eb-984a-967558023cc8.png)




## DataScience Workflow

![mlb-ht-wt](https://user-images.githubusercontent.com/58792/110829008-a7980e00-8265-11eb-883d-4a87fe6f0a84.png)

This repository is focused on MLOps.  To see more about Data Storytelling, you can go to this [Github repo on Data Story Telling](https://github.com/noahgift/data-story-telling)
