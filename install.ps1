$env:FLASK_APP = "flaskr"
$env:FLASK_DEBUG = "true"

pip install -r requirements.txt

flask init-db