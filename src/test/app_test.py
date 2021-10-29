import requests
import json

def util():
    with open('testcases.json') as json_file :
        testcases = json.load(json_file)
    return testcases


test_cases= util()


def test_success():
    url = 'http://127.0.0.1:8080/api'
    for testcase_id in test_cases.keys():
        headers = test_cases[testcase_id]["header"]
        body = test_cases[testcase_id]["body"]
        method = test_cases[testcase_id]["method"]
        if method.lower() == 'get':
            resp = requests.get(url, headers=headers, data=body)
        if method.lower() == 'post':
            resp = requests.post(url, headers=headers, data=body)
        assert resp.status_code == 200
        resp_body = resp.json()
        assert resp_body['Method'] == method
        header_result =  any(elem in headers.items()  for elem in resp_body['Headers'].items())
        assert header_result ,"test passed"
        print(resp_body)
        assert resp_body['Body'] == body , "test passed"


def test_failure():
    url = 'http://127.0.0.1:8080/api'
    for testcase_id in test_cases.keys():
        headers = test_cases[testcase_id]["header"]
        body = test_cases[testcase_id]["body"]
        method = test_cases[testcase_id]["method"]
        if method.lower() == 'get':
            resp = requests.get(url, headers=headers, data=body)
        if method.lower() == 'post':
            resp = requests.post(url, headers=headers, data=body)
        resp_body = resp.json()
        header_result = not any(elem in headers.items() for elem in resp_body['Headers'].items())
        assert header_result == False
        assert not resp_body['Body'] != body

def test_notfound():
    url = 'http://127.0.0.1:8080/api2'
    with open('testcases.json') as json_file :
        testcases = json.load(json_file)
        for testcase_id in testcases.keys():
            headers = testcases[testcase_id]["header"]
            body = testcases[testcase_id]["body"]
            resp = requests.get(url, headers=headers, data=body)
            assert resp.status_code == 404
