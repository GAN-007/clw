from  flask import Flask,render_template
app=Flask(__name__)
@app.route('/students',methods=['GET','POST'])
def student():
    student=["dan", "mike","don","moss"]
    return render_template("students.html", students = student)
        

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)