from flask import Blueprint, Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

api = Blueprint('api', __name__)

db = SQLAlchemy()

class Upload(db.Model):
    __tablename__ = "uploads"
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(255))
    
    def __init__(self, file_name):
        self.file_name = file_name
    
    def __repr__(self):
        return '%s/%s' % (self.id, self.file_name)

class Resumee(db.Model):
    __tablename__ = "resumee"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    email = db.Column(db.String(200))
    birth_date = db.Column(db.Date)
    num_tel = db.Column(db.Integer)
    disp = db.Column(db.Integer)
    nb_exp = db.Column(db.Integer)
    message = db.Column(db.String(255))
    
    def __init__(self, first_name, last_name, email, birth_date,num_tel, disp, nb_exp, message):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.birth_date = birth_date
        self.num_tel = num_tel
        self.disp = disp
        self.nb_exp = nb_exp
        self.message = message
        
    def __repr__(self):
        return '%s/%s/%s/%s/%s/%s/%s/%s/%s' % (self.id, self.first_name, self.last_name, self.email, self.birth_date, self.num_tel, self.disp, self.nb_exp, self.message)

               
@api.route('/resumees', methods=['POST', 'GET'])
def data():
    
    # POST a data to database
    if request.method == 'POST':
        body = request.json
        first_name = body['first_name']
        last_name = body['last_name']
        email = body['email']
        birth_date = body['birth_date']
        num_tel = body['num_tel']
        disp = body['disp']
        nb_exp = body['nb_exp']
        message = body['message']

        data = Resumee(first_name, last_name, email, birth_date, num_tel, disp,nb_exp, message)
        db.session.add(data)
        db.session.commit()

        return jsonify({
            'status': 'Data is posted to PostgreSQL!'
        })
    
    # GET all data from database & sort by id
    if request.method == 'GET':
        # data = User.query.all()
        data = Resumee.query.order_by(Resumee.id).all()
        print(data)
        dataJson = []
        for i in range(len(data)):
            # print(str(data[i]).split('/'))
            dataDict = {
                'id': str(data[i]).split('/')[0],
                'first_name': str(data[i]).split('/')[1],
                'last_name': str(data[i]).split('/')[2],
                'email' : str(data[i]).split('/')[3],
                'birth_date' : str(data[i]).split('/')[4],
                'num_tel' : str(data[i]).split('/')[5],
                'disp' : str(data[i]).split('/')[6],
                'nb_exp' : str(data[i]).split('/')[7],
                'message' : str(data[i]).split('/')[8]
            }
            dataJson.append(dataDict)
        return jsonify(dataJson)

@api.route('/resumees/<string:id>', methods=['GET', 'DELETE', 'PUT'])
def onedata(id):

    # GET a specific data by id
    if request.method == 'GET':
        data = Resumee.query.get(id)
        print(data)
        dataDict = {
            'id': str(data).split('/')[0],
            'first_name': str(data).split('/')[1],
            'last_name': str(data).split('/')[2],
            'email' : str(data).split('/')[3],
            'birth_date' : str(data).split('/')[4],
            'num_tel' : str(data).split('/')[5],
            'disp' : str(data).split('/')[6],
            'nb_exp' : str(data).split('/')[7],
            'message' : str(data).split('/')[8]
        }
        return jsonify(dataDict)
        
    # DELETE a data
    if request.method == 'DELETE':
        delData = Resumee.query.filter_by(id=id).first()
        db.session.delete(delData)
        db.session.commit()
        return jsonify({'status': 'Data '+id+' is deleted from PostgreSQL!'})

    # UPDATE a data by id
    if request.method == 'PUT':
        body = request.json
        newFirstName = body['first_name']
        newLastName = body['last_name']
        newEmail = body['email']
        newdate = body['birth_date']
        newTel = body['num_tel']
        newDisp = body['disp']
        newExp = body['nb_exp']
        newMsg = body['message']
        editData = Resumee.query.filter_by(id=id).first()
        editData.first_name = newFirstName
        editData.last_name = newLastName
        editData.email = newEmail
        editData.birth_date = newdate
        editData.num_tel = newTel
        editData.disp = newDisp
        editData.nb_exp = newExp
        editData.message =newMsg
        db.session.commit()
        return jsonify({'status': 'Data '+id+' is updated from PostgreSQL!'})