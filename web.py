import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
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
    return '''<h1>WEB CUA STEVE</h1>
<p>Truy cap la bi hack may tinh.</p>'''


@app.route('/api/sd', methods=['GET'])
def api_all():
    return jsonify(books)


@app.route('/api/user', methods=['GET'])
def api_user():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'ten' in request.args:
        vten = request.args['ten']
        vtuoi = request.args['tuoi']
    else:
        return "Error: No id field provided. Please specify an id."
    import mysql.connector

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="sakila"
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO steve_table (ten, tuoi) VALUES ( %s, %s)"
    val = (vten,vtuoi)
    mycursor.execute(sql, val)
    mydb.commit()
    return vten+" "+vtuoi
    
@app.route('/api/chon', methods=['GET'])
def api_chon():
    import mysql.connector
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sakila"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM steve_table")
    myresult = mycursor.fetchall()
    return str(myresult)
     
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)