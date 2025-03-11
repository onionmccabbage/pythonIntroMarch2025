# we may import additional libraries so long as we have already added them
# we may need to add libraries to python
# this is done using PIP

import requests

# the requests library lets us access remote data over https
def getAllUsers():
    '''make a reuest to a remote URL to return some data'''
    apiURL = 'http://jsonplaceholder.typicode.com/users'
    # here we use 'get'
    # we could also use 'post' and send additional headers (e.g. for auithentiaction)
    response = requests.get(apiURL) # ask the server for a response
    # this particular API will return data in JSON format
    data = response.json() # or response.text() or response.xml() .....
    return data # all the received data is now returned in a Python structure

# we may need to retrieve a single user
def getOneUser(n=1): # we maychoose to give 'n' a default value
    '''make a request for a single user, n'''
    apiURL = 'http://jsonplaceholder.typicode.com/users'
    response = requests.get(f'{apiURL}/{n}') # we combine the URL with the id n
    data = response.json()
    return data


users = getAllUsers()
print(users)
single = getOneUser(4)
print(single)