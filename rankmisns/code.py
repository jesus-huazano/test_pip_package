from os import getenv
from os.path import join, dirname
import boto3

class ConnectToSNS:
    def __init__(
        self, 
        sns_endpoint, 
        aws_region, 
        aws_access_key_id, 
        aws_secret_access_key, 
        aws_account_id, 
        sns_env, 
        sns_api,
        type_queue = 'sns',
        protocol = 'https'
    ):
        self.ENDPOINT = sns_endpoint
        self.type_queue = type_queue
        self.protocol = protocol
        self.region_name = aws_region
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key

        self.CLIENT = boto3.client( type_queue, aws_region, aws_access_key_id, aws_secret_access_key )
        self.TOPIC_ARN = "arn:aws:sns:{}:{}:{}-{}".format( aws_region, aws_account_id, sns_env, sns_api )

    def suscribe(self):
        message = 'default error'
        try:
            suscription = self.CLIENT.subscribe(
                TopicArn=self.TOPIC_ARN,
                Protocol=self.protocol,
                Endpoint=f"{self.ENDPOINT}/sns/suscription"
            )
            return ( True, suscription )
        except self.CLIENT.exceptions.NotFoundException as e:
            message = e.response.get('Error').get('Message')
        except Exception as e:
            message = e
        return ( False, message )

    def confirm_suscription(self, token):
        message = 'default error'
        try:
            confirm = self.CLIENT.confirm_subscription(
                TopicArn=self.TOPIC_ARN,
                Token=token
            )
            return ( True, confirm )
        except self.CLIENT.exceptions.NotFoundException as e:
            message = e.response.get('Error').get('Message')
        except Exception as e:
            message = e
        return ( False, message )
