from dotenv import load_dotenv
from os import getenv
import requests

load_dotenv()
kibana_url = getenv('DR_KIBANA_URL')
api_key = getenv('DR_API_KEY')
if kibana_url is None:
    print("Failed to get env vars!")
    
headers = {
    "Authorization": f"ApiKey {api_key}",
    "kbn-xsrf": "true"
}

response = requests.post(f"{kibana_url}/api/detection_engine/rules/_import", headers=headers, files={"file": open(r"./exports/exported_rules.ndjson", "rb")}, verify=False)
print(response.content)
response.raise_for_status()

with open("imported_rules.ndjson", "wb") as f:
    f.write(response.content)
