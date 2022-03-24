from requests import post, get

test_1 = post('http://localhost:8080/api/jobs', json={
    "team_leader": 1,
    "job": "aboba",
    "work_size": 24,
    "collaborators": "2, 3",
    "is_finished": False,
    "start_date": "22/04",
    "end_date": "21/05"
}).json()

if get("http://localhost:8080/api/jobs").json()["jobs"][-1]["job"] == "aboba":
    print("ok")
else:
    print("test failed")

test_2 = post('http://localhost:8080/api/jobs').json()  # отсутсвуют передаваемые данные
if test_2["error"] == "Empty request":
    print("ok")

test_3 = post('http://localhost:8080/api/jobs', json={  # передаем уже существующий ид
    "team_leader": 1,
    "job": "aboba",
    "work_size": 24,
    "collaborators": "2, 3",
    "is_finished": False,
    "start_date": "22/04",
    "end_date": "21/05",
    "id": 1
}).json()

if test_3["error"] == "Id already exists":
    print("ok")

test_4 = post('http://localhost:8080/api/jobs', json={  # не передаем некоторые поля
    "collaborators": "2, 3",
    "is_finished": False,
    "start_date": "22/04",
    "end_date": "21/05"
}).json()

if test_4["error"] == "Bad request":
    print("ok")
