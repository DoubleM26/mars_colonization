from requests import post, get, delete

test_1 = delete('http://localhost:8080/api/jobs/1').json()

if get("http://localhost:8080/api/jobs/1").json()["error"] == "Not found":
    print("ok")
else:
    print("test failed")

test_2 = delete('http://localhost:8080/api/jobs/aboba').json()  # передача строки вместо числа
if test_2["error"] == "Not found":
    print("ok")

test_3 = delete('http://localhost:8080/api/jobs/999').json()  # передача ид несуществующей работы
if test_2["error"] == "Not found":
    print("ok")
