import json

def lambda_handler(event, context):
    print(json.dumps(event))
    lower_headers = {}
    if 'headers' in event :
        for k in event['headers'].keys() :
            lower_headers[k.lower()] = event['headers'][k]

    token = '-1'
    if 'authorization' in lower_headers :
        token = lower_headers['authorization']

    print(token)
    if token == '1' :
        return {
            'principalId': 1,
            'policyDocument': {
                'Version': '2012-10-17',
                'Statement': [
                    {
                        'Action': '*',
                        'Effect': 'Allow',
                        'Resource': event['methodArn']
                    }
                ]
            }
        }

    return {
        'principalId': 1,
        'policyDocument': {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Action': '*',
                    'Effect': 'Deny',
                    'Resource': event['methodArn']
                }
            ]
        }
    }
