from dotenv import load_dotenv
from os import getenv
import requests

load_dotenv()
kibana_url = getenv('DR_KIBANNA_URL')
api_key = getenv('DR_API_KEY')

headers = {
    "Authorization": f"ApiKey {DR_API_KEY}",
    "kbn-xsrf": "true"
}

response = requests.post(f"{kibana_url}/api/detection_engine/rules/_import", headers=headers, files={"file": open(r"./exports/exported_rules.ndjson", "rb")}, verify=False)
print(response.content)
response.raise_for_status()

with open("imported_rules.ndjson", "wb") as f:
    f.write(response.content)
