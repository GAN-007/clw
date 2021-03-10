from flask import Flask,render_template,request

app=Flask(__name__)


@app.route('/students',methods=['GET','POST'])
def home():
  
    return render_template("enter.html")
        
        
if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)