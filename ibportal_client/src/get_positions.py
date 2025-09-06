import requests
import boto3
import json

# Assuming the gateway is running and authenticated on localhost:5000
#base_url = "https://localhost:5000"
base_url = "https://host.docker.internal:5000"
account_endpoint = "/v1/api/portfolio/accounts"

# You may need to handle authentication cookies or tokens after initial login
# For simplicity, this example assumes a session is already established.

try:
    response = requests.get(f"{base_url}{account_endpoint}", verify=False) # verify=False for self-signed certs
    response.raise_for_status()  # Raise an exception for bad status codes

    account_data = response.json()
    print(account_data)
    
    if isinstance(account_data, list):
            s3 = boto3.client('s3')
            bucket_name = 'portfolio-data'
            for item in account_data:
                account_id = item.get('accountId')
                position_endpoint = f"/v1/api/portfolio/{account_id}/positions"
                response = requests.get(f"{base_url}{position_endpoint}", verify=False)
                response.raise_for_status() 
                positions_data = json.dumps(response.json())
                print("Portfolio Position for Accoount ID: "+account_id+" is: "+positions_data)
                s3_key = account_id + ".json"
                #s3.put_object(Body=positions_data, Bucket=bucket_name, Key=s3_key,ContentType='application/json' )

except requests.exceptions.RequestException as e:
    print(f"Error fetching portfolio data: {e}")
