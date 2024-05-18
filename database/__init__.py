from sqlalchemy import create_engine
from sqlalchemy.sql import select
from sqlalchemy.orm import sessionmaker
# from database import Patient

# DEFINE THE DATABASE CREDENTIALS
user = 'abdullah'
password = '5343722'
host = '127.0.0.1'
port = 3306
database = 'calendar'


def get_connection():
    return create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")
