import json
from src import app

def test_get_notes():
    event = {"httpMethod": "GET"}
    result = app.lambda_handler(event, None)
    assert result["statusCode"] == 200
    assert json.loads(result["body"]) == ["note1", "note2", "note3"]

def test_post_note():
    event = {
        "httpMethod": "POST",
        "body": json.dumps({"title": "Test Note", "content": "Content here"})
    }
    result = app.lambda_handler(event, None)
    assert result["statusCode"] == 201
    body = json.loads(result["body"])
    assert body["message"] == "Note added"
    assert "data" in body
