from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
  
    UserId=request.cookies.get('userId')
    Username=request.cookies.get('Username')
    return 'welcome '+ str(Username) + 'your id is '+ str(UserId)


       
@app.route('/result',methods=['GET','POST'])
def result():
    if request.method=='POST':
       result=request.form
       return render_template('result.html' , result=result) 


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)