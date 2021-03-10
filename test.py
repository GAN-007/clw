








    from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

# @app.route('/')
# def home():
#    return render_template('enter.html')

@app.route('/first/last/password',method=['POST'])
def log():
   # First name =input("name")
   # Last name = input("name")
   # password="1234567"

   if request.form == 'POST' and request.form['Fisrt name'] == input("name")and request.form['Last name'] == input("name")and request.form['password'] == "1234567" :
         return render_template('welcome.html')
   else:
      return render_template('error.html')


# @app.route('/login',methods = ['POST', 'GET']) 
# def first(): 
#    return render_template('welcome.html')

# @app.route('/login',methods = ['POST', 'GET']) 
# def Last():
#     return render_template('welcome.html')


# @app.route('/login',methods = ['POST', 'GET']) 
# def password(): 
#     return render_template('welcome.html')


@app.route('/success')
def success():
   return 'logged in successfully'

@app.route('/error')
def error():
   return 'could not logged in successfully'   
	
if __name__ == '__main__':
   app.run(debug = True)


