import requests

# Making a GET request
response = requests.get('https://api.github.com/events')

# Making a POST request
response = requests.post('https://httpbin.org/post', data={'key': 'value'})

# Making a PUT request
response = requests.put('https://httpbin.org/put', data={'key': 'value'})

# Making a DELETE request
response = requests.delete('https://httpbin.org/delete')

# Accessing the response data
data = response.json()
