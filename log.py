from flask import Flask,redirect,url_for,render_template,request
from flask.globals import request

app=Flask(__name__)


@app.route('/user',methods=['GET','POST'])
def user():
   user_name=input('name')  
   password=input('password')
   if request.form['user_name'] != user_name:
        return render_template("error.html",msg="Check user_name and retry")
   else:
        return  render_template("enter.html",msg="Welcome %s as User")   

   if request.form['password'] != password:
         return render_template("error.html",msg="Check password and retry")
   else:
         return  render_template("enter.html",msg="Welcome %s as User")   

   return render_template("welcome.html",user_name=user_name)
if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)


