# Serverless Notes API with AWS SAM 📝

This is a simple serverless API built with AWS SAM. It allows users to create and retrieve notes using Lambda and API Gateway.

## Features
- `GET /notes` - Returns a list of mock notes.
- `POST /notes` - Accepts a JSON body to simulate adding a note.

## Technologies Used
- AWS Lambda
- AWS API Gateway
- AWS SAM (Serverless Application Model)
- Python 3.13

## Getting Started

### 1. Build and Deploy
```bash
sam build
sam deploy --guided
```

### 2. Test Locally
```bash
sam local invoke "NotesFunction" -e events/event.json
```

## License
MIT
