import requests
import json

class DataProcessor:
    def __init__(self, api_key = None):
        # No API key is required for this example
        self.api_key = api_key

    def fetch_data(self, url):
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch data from {url} with error code {response.status_code}")
        else:
            return response.json()
        
    def extract_fields(self, data):
        # Extract relevant fields from the data
        if data:
            return {
                "title": data.get("title"),
                "primaryImage": data.get("primaryImage"),
                "objectDate": data.get("objectDate"),
                "creditLine": data.get("creditLine"),
                "country": data.get("country")
            }
        return None
