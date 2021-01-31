# https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
# https://medium.com/firebase-developers/hosting-flask-servers-on-firebase-from-scratch-c97cfb204579

# Running with flask
# $ python3 -m venv pizza_env
# $ source pizza_env/bin/activate   
# $ export FLASK_APP=app
# $ export FLASK_ENV=development
# $ flask run

from flask import Flask, render_template, request
import os
import pizza_salad

app = Flask(__name__)

@app.route('/')
def index():
    if(request.args):
        print(request.args)
        ingredients=pizza_salad.getReceipe(request.args['weight'], request.args['concentration'])
        return render_template('receipe.html', ingredients=ingredients)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
