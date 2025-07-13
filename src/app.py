import json

def lambda_handler(event, context):
    method = event.get("httpMethod", "")
    if method == "GET":
        return {
            "statusCode": 200,
            "body": json.dumps(["note1", "note2", "note3"])
        }
    elif method == "POST":
        data = json.loads(event.get("body", "{}"))
        return {
            "statusCode": 201,
            "body": json.dumps({"message": "Note added", "data": data})
        }
    else:
        return {
            "statusCode": 405,
            "body": json.dumps({"error": "Method not allowed"})
        }
