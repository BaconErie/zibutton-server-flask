from flask import Flask, send_from_directory, request, redirect
from jwt import encode, decode
import sqlite3

app = Flask(__name__)

####################
# HELPER FUNCTIONS #
####################

def get_logged_in_user(request):
    '''Returns the user_id of the logged in user, if it exists'''
    token = request.cookies.get('token')

    if token == None:
        return

    try:
        user_id = decode(token).get('user_id')
    except:
        return
    
    return user_id


#################
# STATIC ROUTES #
#################

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/lists')
def lists():
    query_user_id = request.args.get('user')
    
    user_id = get_logged_in_user(request)

    if not query_user_id and not user_id:
        return redirect('/login')
    
    return send_from_directory('static', 'lists.html')


##############
# API ROUTES #
##############

@app.route('/api/users/<query_user_id>')
@app.route('/api/users')
def api_users(query_user_id=None):
    conn = sqlite3.connect('db.db')
    c = conn.cursor()

    user_id = get_logged_in_user(request)

    if not query_user_id and not user_id:
        # Ensures that either query_user_id or user_id exists beyond this point
        return "Bad request", 400

    if query_user_id and query_user_id != user_id:
        c.execute('SELECT id, name FROM lists WHERE owner_id=? AND visibility=\'public\'', (query_user_id))
    else:
        # user_id has to exist at this point.
        c.execute('SELECT id, name FROM lists WHERE owner_id=?', (user_id))
    conn.commit()
    
    results = c.fetchall()

    return_json = {}
    for row in results:
        name = row[1]
        id = row[0]

        return_json[name] = id
    
    return return_json

@app.route('/api/login', methods=['POST'])
def api_login():
    