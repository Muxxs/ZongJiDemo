from flask import Flask,request,jsonify
from operation import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    UserOp = UserDBoperate()
    UserOp.OpenUserDB()
    UserOp.Insert('wj', '123', [0, 1, 2, 3])
    return 'Hello World!'

@app.route('/sign',methods=['POST'])
def SignUp():
    Name=request.form['name']
    Pw=request.form['passwd']
    Like=request.form['like'].split("-")
    UserOp = UserDBoperate()
    UserOp.OpenUserDB()
    UserOp.Insert(Name, Pw, Like)

if __name__ == '__main__':
    app.run()
