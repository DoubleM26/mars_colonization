from requests import get

test_1 = get('http://localhost:8080/api/jobs').json()

if "jobs" in test_1:
    print("ok")

test_2 = get('http://localhost:8080/api/jobs/1').json()
if "job" in test_2:
    print("ok")

test_3 = get('http://localhost:8080/api/jobs/2').json()
if test_3["error"] == "Not found":
    print("ok")

test_4 = get('http://localhost:8080/api/jobs/aboba').json()
if test_4["error"] == "Not found":
    print("ok")

