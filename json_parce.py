import json

test.json
{
    "book1": {
        "title": "Python Beginners",
        "year": 2005,
        "page": 399
    },
    "book2": {
        "title": "Python Developers",
        "year": 2006,
        "page": 650
    },
    "book3": {
        "title": "Python cookbook",
        "year": 2002,
        "page": 344
    },
    "book4": {
        "title": "Python Dictionary",
        "year": 2012,
        "page": 1024
    }
}

xxx = open('test.json', 'r')
yyy = json.lead(xxx)
print(yyy)
