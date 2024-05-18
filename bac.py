from flask import Flask, request, render_template, redirect, url_for, flash
from flask import session as flask_session
from back_databse_helper import create_patient, check_patient, get_patient
import json


app = Flask(__name__)
app.secret_key = "secret key"


@app.route('/')
@app.route('/home')
def home():
    if "patient" in flask_session:
        data = json.loads(flask_session["patient_data"])
        return render_template('home.html', patient_data=data)
    else:  
        return render_template('home.html', patient_data=None)


@app.route('/user')
def User():
    if "patient" in flask_session:
        data = json.loads(flask_session["patient_data"])
        return render_template('user.html', patient_data=data)
    else:
        return redirect(url_for('login'))


@app.route('/service')
def service():
    if "patient" in flask_session:
        data = json.loads(flask_session["patient_data"])
        return render_template('service.html', patient_data=data)
    else:
        return redirect(url_for('login'))


@app.route('/signin', methods=['GET', 'POST'])
def login():
    """
    Function to login the patient
    :return: redirect to the user page
    """
    if request.method == 'POST':
        data = request.form
        res = check_patient(data['email'], data['password'])
        if res:
            patient_data = get_patient(data['email'])
            dict_pat_data = json.dumps(patient_data)
            flask_session.permanent = False
            flask_session["patient"] = "email"
            flask_session["patient_data"] = dict_pat_data
            print(flask_session["patient"])
            print("Login Successful")
            return redirect(url_for('service'))
        else:
            print("Invalid Email or Password")

    return render_template('SignIn.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    Function to signup the patient
    :return: redirect to the service page
    """
    if request.method == 'POST':
        data = request.form
        data = dict(data)
        res = create_patient(**data)
        print(res)
        return redirect(url_for('login'))
    return render_template('SignUp.html')


@app.route('/logout')
def logout():
    """
    Function to logout the patient
    :return: redirect to the home page
    """
    flask_session.pop("patient", None)
    flask_session.pop("patient_data", None)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
