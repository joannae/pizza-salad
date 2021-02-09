from flask import Flask, render_template, request
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
