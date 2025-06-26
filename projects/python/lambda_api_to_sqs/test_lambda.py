import unittest
from unittest.mock import patch, MagicMock
import json
import os
from api_to_sqs_lambda import lambda_handler, make_api_request, send_to_sqs

class TestLambdaFunction(unittest.TestCase):
    
    @patch('api_to_sqs_lambda.make_api_request')
    @patch('api_to_sqs_lambda.send_to_sqs')
    @patch.dict(os.environ, {'API_URL': 'https://api.example.com', 'SQS_QUEUE_URL': 'https://sqs.example.com'})
    def test_lambda_handler_success(self, mock_send_to_sqs, mock_make_api_request):
        # Setup mocks
        mock_make_api_request.return_value = {"data": "test_data"}
        mock_send_to_sqs.return_value = "message-123"
        
        # Test event
        event = {
            "httpMethod": "GET",
            "queryParams": {"param1": "value1"}
        }
        
        # Call the function
        result = lambda_handler(event, {})
        
        # Assertions
        self.assertEqual(result['statusCode'], 200)
        response_body = json.loads(result['body'])
        self.assertEqual(response_body['messageId'], "message-123")
        
        # Verify mocks were called correctly
        mock_make_api_request.assert_called_once_with('https://api.example.com', event)
        mock_send_to_sqs.assert_called_once_with('https://sqs.example.com', {"data": "test_data"})
    
    @patch('api_to_sqs_lambda.requests.get')
    def test_make_api_request_get(self, mock_get):
        # Setup mock
        mock_response = MagicMock()
        mock_response.json.return_value = {"result": "success"}
        mock_get.return_value = mock_response
        
        # Test data
        url = "https://api.example.com"
        event = {
            "httpMethod": "GET",
            "queryParams": {"param1": "value1"},
            "headers": {"Authorization": "Bearer token"}
        }
        
        # Call the function
        result = make_api_request(url, event)
        
        # Assertions
        self.assertEqual(result, {"result": "success"})
        mock_get.assert_called_once_with(
            url, 
            params=event["queryParams"], 
            headers=event["headers"]
        )
    
    @patch('api_to_sqs_lambda.boto3.client')
    def test_send_to_sqs(self, mock_boto_client):
        # Setup mock
        mock_sqs = MagicMock()
        mock_sqs.send_message.return_value = {"MessageId": "msg-123"}
        mock_boto_client.return_value = mock_sqs
        
        # Test data
        queue_url = "https://sqs.example.com"
        message = {"data": "test_message"}
        
        # Call the function
        result = send_to_sqs(queue_url, message)
        
        # Assertions
        self.assertEqual(result, "msg-123")
        mock_sqs.send_message.assert_called_once_with(
            QueueUrl=queue_url,
            MessageBody=json.dumps(message)
        )

if __name__ == '__main__':
    unittest.main()