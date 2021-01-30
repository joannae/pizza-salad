# https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3

# Running with flask
# $ python3 -m venv pizza_env
# $ source pizza_env/bin/activate   
# $ export FLASK_APP=app
# $ export FLASK_ENV=development
# $ flask run

from flask import Flask, render_template, request
import pizza_salad

app = Flask(__name__)

@app.route('/')
def index():
    if(request.args):
        print(request.args)
        pizza_salad.getReceipe(request.args['weight'], request.args['concentration'])
        return render_template('receipe.html')
    else:
        return render_template('index.html')
