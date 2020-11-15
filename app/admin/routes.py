from flask import Blueprint, Flask, render_template, request, jsonify
from .app import db


admin = Blueprint('admin', __name__)
@admin.route("/")
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    pwd = db.Column(db.String(255))
    
    def __init__(self, username, pwd):
        self.username = username
        self.pwd = pwd
    
    def __repr__(self):
        return '%s/%s/%s' % (self.id, self.username, self.pwd)
@app.route('/users', methods=['POST', 'GET'])
def users():
    
    # POST a user credential to database
    if request.method == 'POST':
        body = request.json
        username = body['username']
        pwd = body['pwd']
        data = User(username, pwd)
        db.session.add(data)
        db.session.commit()

        return jsonify({
            'status': 'Data is posted to PostgreSQL!',
            'username': username,
            'pwd': pwd
        })
    
    # GET all data from database & sort by id
    if request.method == 'GET':
        # data = User.query.all()
        data = User.query.order_by(User.id).all()
        print(data)
        dataJson = []
        for i in range(len(data)):
            # print(str(data[i]).split('/'))
            dataDict = {
                'id': str(data[i]).split('/')[0],
                'username': str(data[i]).split('/')[1],
                'pwd': str(data[i]).split('/')[2]
            }
            dataJson.append(dataDict)
        return jsonify(dataJson)

@app.route('/users/<string:id>', methods=['GET'])
def oneuser(id):

    # GET a specific data by id
    if request.method == 'GET':
        data = User.query.get(id)
        print(data)
        dataDict = {
                'id': str(data).split('/')[0],
                'username': str(data).split('/')[1],
                'pwd': str(data).split('/')[2]
            }
        return jsonify(dataDict)

def admin_home():
    return "<h1>Admin Home</h1>"