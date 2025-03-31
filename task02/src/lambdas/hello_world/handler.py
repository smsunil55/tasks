from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger(__name__)


class HelloWorld(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        """
        Explain incoming event here
        """
        # todo implement business logic
        if ('requestContext' in event):
            requestContext = event['requestContext']
            httpVals = requestContext['http']
            if (httpVals['method'] == 'GET' and httpVals['path'] == '/hello'):
                return {
                "statusCode": 200,
                "message": "Hello from Lambda"
                }
            else:
                return {
                "statusCode": 400,
                "message": "Bad request syntax or unsupported method. Request path: " + httpVals['path'] + ". HTTP method: " + httpVals['method']
                }
        return 200

HANDLER = HelloWorld()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
