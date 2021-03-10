from flask import Flask,redirect,session,make_response,render_template,request,url_for

app=Flask(__name__)
app.secret_key='1234'

"""this is sessions"""

@app.route('/login/<username>',methods=['GET','POST'])
def login(username):
    session['username'] = username
    return redirect(url_for('home'))


@app.route('/home',methods=['GET','POST'])
def home():
  
    return render_template('home.html',username=session['username'])

@app.route('/contact',methods=['GET','POST'])
def contact():
    return session['username']







"""___________________________________________"""




if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
     app.run(port=5000,debug=True)