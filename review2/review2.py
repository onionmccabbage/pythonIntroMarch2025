import requests
from util.sanitize import cleanup
from fifo.write_text import writeToFile

def get_data(category, id):
    full_path = f'https://jsonplaceholder.typicode.com/{category}/{id}'
    res = requests.get(full_path)
    j = res.json() # we just want the json data
    return j # return the data as a dict

def main():
    # ask the user for a category and an id
    which_cat = input('which category? ')
    which_id  = input('which id (1-10)? ')
    # use our sanitize module to clean up some data
    cleaned = cleanup(category=which_cat, id=which_id)
    # make a request and return the json
    data = get_data(category=cleaned['category'], id=cleaned['id'])
    resultString = f'Category {cleaned["category"]} member {cleaned['id']} gives the following:\n'
    for k, v in data.items():
        print(f'\t{k}: {v}')
        resultString += f'\t{k}: {v}\n'
    print(resultString)
    writeToFile(resultString)
    # if category is 'users' then we also want all the posts
    if cleaned['category'] == 'users':
        print(f'Posts for user {cleaned['id']}:')
        posts = get_data(category='posts', id='')
        for item in posts: # posts is a list
            if item['userId']==cleaned['id']:
                print(f"Post {item['id']}: title: {item['title']} body:{item['body']}\n")

if __name__ == '__main__':
    main()