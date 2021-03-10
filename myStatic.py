from flask import Flask,render_template

app=Flask(__name__)


@app.route('/')
def click():
   return render_template('myStatic.html')

if __name__ == '__main__':

   app.run(debug=True)