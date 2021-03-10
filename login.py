from flask import Flask,request

app=Flask(__name__)

@app.route('/sucsses/<succsses>')
def succsses(succsses):
    if request.method=='POST':
        # Handle POST Request here 
        pass
        

@app.route('/')
def home():
    return "welcome"

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        # Handle POST Request here
        username = request.form["username"]
        return "Welcome to post " + username
    else:
        username = request.args.get("username")
        return "welcome to get " + username


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)