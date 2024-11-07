from crud import *
from flask import *
app=Flask(__name__)
@app.route('/')
def openhomepage():
    return render_template('home.html')
@app.route('/studentreg')
def OpenStudentRegPage():
    return render_template('student_reg.html')

@app.route('/savetodb_student_table',methods=['POST','GET'])
def savetodb():
    if request.method=='POST':
        a=int(request.form['sid'])
        b=request.form['sname']
        c=request.form['snum']
        d=request.form['saddress']
        e= request.form['sdob']
        f= request.form['sdoj']
        print(a,b,c,d,e,f)
        try:
            insertstudent(a,b,c,d,e,f)
            msg="sucessfully Inserted"
        except:
            msg="Not sucessfull"
        finally:
            return render_template('result.html',msg=msg)


if __name__=='__main__':
    app.run()
