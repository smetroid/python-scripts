import requests

url = 'https://example.com/api'
page_number = 1
page_size = 10

while True:
    params = {'page': page_number, 'size': page_size}
    response = requests.get(url, params=params)
    data = response.json()

    # process the data here...

    if len(data) < page_size:
        # we've reached the last page
        break

    page_number += 1


