# test_hello_add.py
from slcm import app
from flask import json

def test_add():        
    response = app.test_client().post(
        '/api/v1/get',
        data=json.dumps({
  "request":
  {
    "credentials":
    {
      "username":"180907612",
      "password":"Mitaspirant14@"
    },
    "type":"ATTENDANCE"
  }
}),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    print(data)
    