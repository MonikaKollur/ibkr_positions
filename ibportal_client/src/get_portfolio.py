import requests

# Set up a session to use the API
session = requests.Session()

# The API is not yet secure. You will need to ignore the SSL verification.
session.verify = False

# Example: Get contract info for Apple (AAPL)
symbol = "AAPL"
url = f"https://localhost:5000/v1/api/trsrv/stocks?symbols={symbol}"

try:
    response = session.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

