from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.database import Patient

user = 'abdullah'  # input("Enter the username: ")
password = '5343722'  # input("Enter the password: ")
host = '127.0.0.1'
port = 3306
database = 'calendar'


def get_connection():
    """
    Function to get the connection to the database
    :return: connection object
    """
    try:
        db = create_engine(
            f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")
        print("Connection successful")
        return db
    except Exception as e:
        print(e)


def create_patient(**patients):
    """
    Function to add a patient to the database
    :param patient : dictionary containing patient information
    """
    engine = get_connection()
    Session = sessionmaker(bind=engine)
    session = Session()
    patient = Patient()

    if patient.get_patient(session=session, email=patients['email']):
        return "Patient already exists"
    try:
        patient.add_patient(session=session, **patients)
        session.commit()
        print("Patient added successfully")
    except Exception as e:
        print(e)
    finally:
        session.close()


def check_patient(email, password):
    """
    Function to check if the patient exists in the database
    :param email: email of the patient
    :param password: password of the patient
    :return: value of existence of the patient or None
    """
    engine = get_connection()
    Session = sessionmaker(bind=engine)
    session = Session()
    patient = Patient()
    res = patient.check_patient(
        session=session, email=email, password=password)
    print(res)
    session.close()
    return res


def get_patient(email):
    """
    Function to get the patient information from the database using email
    :param email: email of the patient
    :return: patient information
    """
    engine = get_connection()
    Session = sessionmaker(bind=engine)
    session = Session()
    patient = Patient()
    res = patient.get_patient(session=session, email=email)
    print(res)
    session.close()
    return res
