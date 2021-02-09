from flask import Flask, render_template, request
import pizza_salad

app = Flask(__name__)

@app.route('/')
def index():
    weight=request.args['weight'] if request.args and request.args['weight'] else None
    concentration=request.args['concentration'] if request.args and request.args['concentration'] else None
    ingredients=pizza_salad.getReceipe(weight, concentration)
    return render_template('receipe.html', ingredients=ingredients)

