# API to SQS Lambda Function

This Lambda function fetches data from an API and pushes the results to an Amazon SQS queue.

## Setup Instructions

1. Create an SQS queue in your AWS account
2. Create a Lambda function with this code
3. Set up the required environment variables:
   - `API_URL`: The URL of the API to call
   - `SQS_QUEUE_URL`: The URL of your SQS queue
4. Configure IAM permissions for the Lambda to:
   - Make API calls (if to external services)
   - Send messages to SQS

## IAM Policy

The Lambda execution role needs the following permissions:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sqs:SendMessage"
            ],
            "Resource": "arn:aws:sqs:*:*:YOUR_QUEUE_NAME"
        }
    ]
}
```

## Deployment

1. Install dependencies:
   ```
   pip install -r requirements.txt -t ./package
   ```

2. Package the Lambda:
   ```
   cd package
   zip -r ../lambda_function.zip .
   cd ..
   zip -g lambda_function.zip api_to_sqs_lambda.py
   ```

3. Deploy to AWS:
   ```
   aws lambda update-function-code --function-name YOUR_FUNCTION_NAME --zip-file fileb://lambda_function.zip
   ```

## Testing

You can test the Lambda with a test event like:

```json
{
  "httpMethod": "GET",
  "queryParams": {
    "param1": "value1"
  },
  "headers": {
    "Content-Type": "application/json"
  }
}
```