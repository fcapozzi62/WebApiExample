import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distance reading of science fiction " \
           "novels.</p> "


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return flask.jsonify(books)


@app.route('/somma/', methods=['GET'])
def somma_f():
    if 'val1' in flask.request.args:
        val1 = float(flask.request.args['val1'])
    else:
        return "Error: No val1 provided."
    if 'val2' in flask.request.args:
        val2 = float(flask.request.args['val2'])
    else:
        return "Error: No val2 provided."
    return str(val1) + " + " + str(val2) + " = " + str(val1 + val2)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in flask.request.args:
        id = int(flask.request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return flask.jsonify(results)


# with the host declaration it is possible to connect from any interface
app.run(host='0.0.0.0')
