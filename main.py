from flask import Flask

from utils import get_all, load_candidates, get_by_pk, get_by_skill

app = Flask(__name__)

candidat = load_candidates()


@app.route('/')
def index():
    return f"{get_all(candidat)}"


@app.route("/candidates/<int:x>")
def get_candidates(x):
    return get_by_pk(x)


@app.route("/skills/<x>")
def get_skill(x):
    return get_by_skill(x)



if __name__ == '__main__':
    app.run(debug=True)
