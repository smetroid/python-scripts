import requests

# Define the URL and data
url = 'http://localhost:5000/encode'
data = {
    'url': 'https://www.yahoo.com/news/trump-legal-news-brief-live-updates-as-trump-takes-the-witness-stand-154827487.html'
}

# Send the POST request
response = requests.post(url, data=data)

# Check the response
if response.status_code == 200:
    print("Request was successful.")
    print(response.text)
else:
    print(f"Request failed with status code {response.status_code}:")
    print(response.text)
