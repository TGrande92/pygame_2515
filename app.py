from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['get'])
def home():
    """
    Opens the score.txt file, reads the contents, and sorts the scores into a list. 
    Then, renders the index.html template with the list of scores as an argument.
    """
    with open("score.txt", "r") as fp:
        scores = fp.read()
        number = ''
        list = []
        for score in scores:
            if score == "\n":
                list.append(int(number))
                number = ''
                pass
            else:
                number = number + score
        list.sort()
    return render_template("index.html", list=list)


@app.route("/add_score", methods=['post'])
def add_score():
    """
    Gets the score from the request JSON, then appends the score to the score.txt 
    file. Returns a status code of 200.
    """
    data = request.json
    with open("score.txt", "a") as fp:
        fp.write(str(data['Score'])+"\n")
    return 200


if __name__ == "__main__":
    app.run(debug=True)
