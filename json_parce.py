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

# ここから別の例題

{
    "Python": {
        "目的": "AI機械学習",
        "期日": 2018,
        "コース": "Python機械学習"
    },
    "Original": {
        "目的": "Python起業コース",
        "期日": 2017,
        "コース": "起業Webサービス"
    }
}
