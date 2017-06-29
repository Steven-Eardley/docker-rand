from app import app
import random

random.seed("hello")


# Serve a page which shows a random number sequence
@app.route('/')
def index():
    randseq = [random.randint(0, 100) for i in range(0, 10)]
    print(randseq)
    return "Your random sequence is:\n{0}".format(randseq)
