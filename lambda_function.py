import json

def lambda_handler(event, context):
    # Static mock data simulating MongoDB output
    mock_data = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25}
    ]

    return {
        'statusCode': 200,
        'body': json.dumps(mock_data)
    }
