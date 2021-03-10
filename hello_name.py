# from flask import Flask
# app=Flask(__name__)
  


# @app.route('/hello/<name>',methods=['GET','POST'])
# def hello_name(name):
#     return "hello" % name



# if __name__ == '__main__':
#     #DEBUG is SET to TRUE. CHANGE FOR PROD
#     app.run(port=5000,debug=True)

from flask import Flask
app = Flask(__name__)


@app.route('/hello/'<admin>)
def admin():
   return "Hello admin"


@app.route('/hello/'<guest>)
def guest():
   return "Hello guest"


if __name__ == '__main__':

   app.run(port=5000,debug=True)