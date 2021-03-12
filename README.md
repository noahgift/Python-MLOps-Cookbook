[![Python application test with Github Actions](https://github.com/noahgift/Python-MLOps-Cookbook/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/noahgift/Python-MLOps-Cookbook/actions/workflows/pythonapp.yml)


# Python MLOps Cookbook 
This is an example of a Containerized Flask Application the can be the core ingrediant in many "recipies", i.e. deploy targets.

## Assets in repo

* `Makefile`:  [View Makefile](https://github.com/noahgift/Python-MLOps-Cookbook/blob/main/Makefile)
* `requirements.txt`:  [View requirements.txt](https://github.com/noahgift/Python-MLOps-Cookbook/blob/main/requirements.txt)
* `cli.py`: [View cli.py](https://github.com/noahgift/Python-MLOps-Cookbook/blob/main/cli.py)
* `utilscli.py`: [View utilscli.py](https://github.com/noahgift/Python-MLOps-Cookbook/blob/main/utilscli.py)
* `app.py`:  [View app.py](https://github.com/noahgift/Python-MLOps-Cookbook/blob/main/app.py)
* `mlib.py`:  Model Handling Library
* `htwtmlb.csv1`: [View CSV](https://github.com/noahgift/Python-MLOps-Cookbook/blob/main/htwtmlb.csv) Useful for input scaling
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



## DataScience Workflow

![mlb-ht-wt](https://user-images.githubusercontent.com/58792/110829008-a7980e00-8265-11eb-883d-4a87fe6f0a84.png)

This repository is focused on MLOps.  To see more about Data Storytelling, you can go to this [Github repo on Data Story Telling](https://github.com/noahgift/data-story-telling)
