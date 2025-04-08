import boto3
import json
# changes aws configure before executing the next code

def invoke_lambda(payload_data):

    lambda_client = boto3.client('lambda', region_name='us-east-2')  

    # Convert the data to JSON
    payload = json.dumps(payload_data)

    # Invoke the Lambda function
    response = lambda_client.invoke(
        FunctionName='FirstLambda',  
        InvocationType='RequestResponse', 
        Payload=payload.encode('utf-8'),
    )

    # Read and decode response
    response_payload = response['Payload'].read().decode('utf-8')
    result = json.loads(response_payload)

    return result

if __name__ == "__main__":
    data = {
        "task": "process",
        "input": [1, 2, 3]
    }

    response = invoke_lambda(data)
    print("Lambda response:", response)
