# The best pizza salad

A simple converter for pizza salad receipe provided in https://www.kokaihop.se/recept/pizzasallad-5>https://www.kokaihop.se/recept/pizzasallad-5

## Running locally
Running with flask
```
python3 -m venv pizza_env
source pizza_env/bin/activate   
export FLASK_APP=app
export FLASK_ENV=development
flask run
```

## Deploying
Save new requirements and commit if any new
```
pip freeze > requirements.txt
```

Deploying from master
```
vercel --prod
```

