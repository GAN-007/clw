from flask import Flask,redirect,session,make_response,render_template,request

app=Flask(__name__)

"""this is sessions"""

@app.route('/login/<username>',methods=['GET','POST'])
def login(username):
    sessions[username] = username
    return redirect(url_for('home'))



"""___________________________________________"""


@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/setcookies',methods=['GET','POST'])
def setcookies():
    if request.method=='POST':
        name = request.form['name']
        resp = make_response(render_template('readcookies.html'))
        resp.set_cookie('Username', 'name')
   
        return resp



@app.route('/readcookies')
def readcookies():
  
    UserId=request.cookies.get('userId')
    Username=request.cookies.get('Username')
    return 'welcome '+ str(Username) + ' your id is '+ str(UserId)



if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)