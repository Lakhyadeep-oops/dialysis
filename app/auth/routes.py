from app.auth import auth_bp
from flask import render_template ,request


@auth_bp.route('/login', methods=['GET','POST'] )
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        print('Username:',username)
        print('Password:',password)
    return render_template('login.html')