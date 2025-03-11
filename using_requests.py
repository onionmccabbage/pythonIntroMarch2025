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
def getOneUser(n=1): # we may choose to give 'n' a default value
    '''make a request for a single user, n'''
    # we should validate that n is an integer between 1 and 10
    if type(n)==int and n in range(1,11):
        apiURL = 'https://jsonplaceholder.typicode.com/users'
        response = requests.get(f'{apiURL}/{n}') # we combine the URL with the id n
        data = response.json()
        return data
    else:
        raise TypeError('Value must be an integer between 1-10')

users = getAllUsers()
print(users)
single = getOneUser(4)
print(single)
# we can use try-except to handle exceptions
try:
    problem = getOneUser('Leanne') # this should throw an exception (TypeError)
except Exception as err:
    print(f'there was a problem: {err}')

# since we have handled the exception, our code may contune to execute
print('we carry on as normal')