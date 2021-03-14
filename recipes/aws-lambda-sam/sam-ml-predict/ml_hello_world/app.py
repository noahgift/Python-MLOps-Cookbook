import json
import mlib


def lambda_handler(event, context):
    """Sample pure Lambda function

    """
    
    default_input = 200
    prediction = mlib.predict(default_input)
    print(f"Event Body {event}")
    return {
        "statusCode": 200,
        "body": json.dumps(prediction
        ),
    }
