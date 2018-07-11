import requests

# parms = {
#     'Years': '10',
#     'Balance': '6000000',
#     'Rating': '700',
#     'Age': 22,
#     'AccountType': 'Blue'
# }

parms = {
    'Years': '1',
    'Balance': '-1',
    'Rating': '200',
    'Age': 'a',
    'AccountType': 'Blue'
}

# response = requests.get("http://brjw.pythonanywhere.com/Promotions/", params=parms)
response = requests.get("http://127.0.0.1:5000/Promotions/", params=parms)
print('{} {} - a response on a GET request by using "requests"'.format(response.status_code, response.reason))
content = response.content.decode('utf-8')
print(content)

# http://brjw.pythonanywhere.com/Promotions/?Years=1&Balance=-1&Rating=200&Age=a&AccountType=Blue
