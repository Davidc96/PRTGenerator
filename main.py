from flask import Flask, render_template, request
from pass_prt import PRTGenerator

DUMMY_URI = 'NEED TO CHANGE THIS ON THE MAIN PY CODE'

DUMMY_TOKEN = ""

app = Flask(__name__)
@app.route('/', methods=["GET","POST"])
def generate_token():
    generator = PRTGenerator()
    valid_token = ""
    DUMMY_TOKEN = generator.generate_PRT(DUMMY_URI)
    if request.method == "POST":
        new_uri = request.form.get('new_uri', "")
        valid_token = generator.generate_PRT(new_uri)

    return render_template("generator_template.html", dummy_uri=DUMMY_URI, dummy_token=DUMMY_TOKEN,
                           new_token=valid_token)
