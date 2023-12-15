from flask import Flask, request

app = Flask(__name__)

messages = []

@app.get("/")
def hello_world():
    return messages

@app.post("/")
def receive():
    messages.append(request.data.decode())
    return "200"