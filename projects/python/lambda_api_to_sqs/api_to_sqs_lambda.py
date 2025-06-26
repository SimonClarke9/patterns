import json
import os
import boto3
import requests
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    """
    Lambda function that makes an API request and sends the result to an SQS queue.
    
    Parameters:
    - event: Lambda event data
    - context: Lambda context object
    
    Returns:
    - Dictionary containing execution status and details
    """
    try:
        # Get environment variables
        api_url = os.environ.get('API_URL')
        queue_url = os.environ.get('SQS_QUEUE_URL')
        
        if not api_url or not queue_url:
            return {
                'statusCode': 500,
                'body': json.dumps({
                    'message': 'Missing required environment variables: API_URL or SQS_QUEUE_URL'
                })
            }
        
        # Make API request
        response = make_api_request(api_url, event)
        
        # Send to SQS
        message_id = send_to_sqs(queue_url, response)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Successfully processed API request and sent to SQS',
                'messageId': message_id
            })
        }
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': f'Error processing request: {str(e)}'
            })
        }

def make_api_request(url, event):
    """
    Makes an API request and returns the response.
    
    Parameters:
    - url: API endpoint URL
    - event: Lambda event data that may contain request parameters
    
    Returns:
    - API response data
    """
    # Extract request parameters from event if needed
    # This is just an example - modify according to your API requirements
    params = event.get('queryParams', {})
    headers = event.get('headers', {})
    method = event.get('httpMethod', 'GET')
    body = event.get('body', None)
    
    # Make the request
    if method.upper() == 'GET':
        response = requests.get(url, params=params, headers=headers)
    elif method.upper() == 'POST':
        response = requests.post(url, json=body, params=params, headers=headers)
    else:
        raise ValueError(f"Unsupported HTTP method: {method}")
    
    # Check if request was successful
    response.raise_for_status()
    
    # Return the response data
    return response.json()

def send_to_sqs(queue_url, message_body):
    """
    Sends a message to an SQS queue.
    
    Parameters:
    - queue_url: URL of the SQS queue
    - message_body: Message to send (will be converted to JSON)
    
    Returns:
    - Message ID from SQS
    """
    # Initialize SQS client
    sqs = boto3.client('sqs')
    
    # Convert message body to JSON string
    if not isinstance(message_body, str):
        message_body = json.dumps(message_body)
    
    # Send message to SQS
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message_body
    )
    
    return response['MessageId']