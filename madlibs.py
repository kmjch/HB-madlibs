from random import sample, choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliments = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliments)

@app.route('/game')
def show_madlib_form():
    game_response = request.args.get("game")

    if game_response == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")

@app.route('/madlib')
def show_madlib():
    person = request.args.get("person")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    verbs = request.args.getlist("verb")
    adverb = request.args.get("adverb")
    secret = request.args.get("secret")

    madlib = choice(["madlib.html", "madlib2.html", "madlib3.html"])

    return render_template(madlib, person=person, color=color, noun=noun, 
                           adjective=adjective, verbs=verbs, adverb=adverb, secret=secret)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
