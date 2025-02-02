import requests
import json

ip = input("What is your target IP: ").strip()
url = f"http://ip-api.com/json/{ip}"

response = requests.get(url)
values =response.json()

print(f"IP: {values.get('query', 'N/A')}")
print(f"City: {values.get('city', 'N/A')}")
print(f"ISP: {values.get('isp', 'N/A')}")
print(f"Organization: {values.get('org', 'N/A')}")
print(f"Country: {values.get('country', 'N/A')}")
print(f"Region: {values.get('region', 'N/A')}")
print(f"Timezone: {values.get('timezone', 'N/A')}")
print(f"Zip: {values.get('zip', 'N/A')}")
