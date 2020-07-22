from flask import Flask, request, jsonify
from operation import *
import json

app = Flask(__name__)


@app.route('/WritePassage', methods=['POST'])
def GetPassage():
    Passage = request.form['passage']
    AuthorID = int(request.form['AuthorID'])
    WriteTime = request.form['time']
    PlaceID = request.form['id'].split("-")
    try:
        P.Insert(Passage, AuthorID, WriteTime, PlaceID)
        return 1
    except:
        return 0


@app.route('/GetPassage', methods=['POST'])
def GetPassage():
    ID = request.form['id']
    try:
        PassOp = PassageDBoperate()
        res = PassOp.Search(ID)
        return json.dumps(res)
    except:
        return 0


@app.route('/GetInfor', methods=['POST'])
def GetInfro():
    ID = request.form['id']
    try:
        InforOp = InfroDBoperate()
        res = InforOp.Search(ID)
        return json.dumps(res)
    except:
        return 0


@app.route('/GetUser', methods=['POST'])
def GetUser():
    ID = request.form['id']
    try:
        UserOp = UserDBoperate()
        res = UserOp.Search(ID)
        return json.dumps(res)
    except:
        return 0


@app.route('/Sign', methods=['POST'])
def SignUp():
    Name = request.form['name']
    Pw = request.form['passwd']
    Like = request.form['like'].split("-")
    try:
        UserOp = UserDBoperate()
        UserOp.Insert(Name, Pw, Like)
        return 1
    except:
        return 0


if __name__ == '__main__':
    app.run()
