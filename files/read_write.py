import json

from csv import DictReader
from files import CSV_FILE, JSON_FILE, JSON_FILE_W


with open(JSON_FILE, "r") as f:
    users = json.loads(f.read())

users_list = users


user_data = []
for user in users_list:
    user_data.append({"name": user['name'], "gender": user['gender'], "address": user['address'], "age": user['age'],
                      "books": [], })


books = []
with open(CSV_FILE, newline='') as f:
    reader = DictReader(f)

    for row in reader:
        books.append({"title": row['Title'], "author": row['Author'], "pages": row['Pages'], "genre": row['Genre']},)


user = 0
for book in books:
    user_data[user]['books'].append(book)
    if len(user_data) - 1 > user:
        user += 1
    else:
        user = 0


with open(JSON_FILE_W, "w") as f:
    s = json.dumps(user_data, indent=4)
    f.write(s)
