import pytest
import requests
import json
import random
import time

auth_token='cm9vdA==.NDQtMA==.yAG6JhA8vTuXHRB39HJpB0lDVd07G6'
headers = {
    'Authorization': 'Bearer perm:' + auth_token,
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}
base_url = 'https://asmtest.myjetbrains.com/youtrack/'
url_project = base_url +'api/admin/projects?fields=id,name,shortName'


def test_create_issue():
    s = requests.Session()
    r = s.get(url_project, headers=headers, timeout = 2)

    if r.status_code == 200:
        print('Getting project list is successful')

    else:
        print('Getting project list failed with status code: ' + r.status_code)

    data = r.json()
    data = random.choice(data)

    project_id = ''
    if 'id' in data:
        project_id = data["id"]

    project_data = {
        "id": project_id
    }

    url_issue = base_url + 'api/issues/'
    payload = {
        "project": project_data,
        "summary": "WITH RANDOM REST API lets you create issues!",
        "description": "Let's create a new issue using YouTrack's REST API."
    }
    response_decoded_json = requests.post(url_issue, data=json.dumps(payload), headers=headers)
    response_json = response_decoded_json.json()
    print('Issue is created : ' + str(response_json))
    print(r.elapsed)


def test_get_issue_fields():
    url_issue = base_url + 'api/issues/'
    resp = requests.get(url_issue, headers=headers)

    issues = resp.json()
    issue = issues[-1]
    print('Getting issue ' + str(issue))

    issue_id = ''
    if 'id' in issue:
        issue_id = issue["id"]

    issue_data = {
        "id": issue_id
    }

    resp = requests.get(url_issue + issue_id + '/customFields?{fields}', headers=headers)
    print('Custom fields are: ' + str(resp.json()))




