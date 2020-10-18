import jmespath
import json

with open('example.json', 'r') as f:
    data = f.read()
    parsed = json.loads(data)

    # Search a specific key
    search_result = 'users[0].name'
    print(jmespath.search(search_result, parsed))

    # Find all values of name in that list
    search_result = 'users[*].name'
    print(jmespath.search(search_result, parsed))

    # Find a result for a specific term
    search_result = "users[?age == '34'].country"
    print(jmespath.search(search_result, parsed))

    # Find a result for a specific term
    search_result = 'users[?name=="avi"].[country, age]'
    print(jmespath.search(search_result, parsed))

    listed = parsed['users']

    for item in listed:
        print(listed)

    # y = ['a', 'b', 'c', 'd', 'e']
    # for item in y:
    #     print(item)
