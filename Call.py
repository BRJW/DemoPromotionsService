import requests

parms = {
    'Years': '10',
    'Balance': '6000000',
    'Rating': '700',
    'Age': 22,
    'AccountType': 'Blue'
}

response = requests.get("http://localhost:5000/Promotions/", params=parms)
print('{} {} - a response on a GET request by using "requests"'.format(response.status_code, response.reason))
content = response.content.decode('utf-8')
print(content[:100], '...')