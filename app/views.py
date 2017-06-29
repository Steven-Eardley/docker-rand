from app import app
import random

random.seed("hello")


# Serve a page which shows a random number sequence
@app.route('/')
def index():
    return "Your random sequence is\n".format([random.randint(0, 100) for i in range(0, 10)])
