from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import select

Base = declarative_base()


class Doctor(Base):
    __tablename__ = 'doctor'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    phone = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    specialization = Column(String(255), nullable=False)
    experience = Column(Integer, nullable=False)
    fee = Column(Integer, nullable=False)

    @classmethod
    def get_basic_info(cls, session: Session, ID=None):
        if ID is None:
            results = session.query(
                cls.name, cls.email, cls.phone, cls.address, cls.specialization
            ).order_by(cls.id).all()

            result_dicts = [
                {"name": name, "email": email, "phone": phone,
                    "address": address, "specialization": specialization}
                for name, email, phone, address, specialization in results
            ]
        else:
            results = session.query(
                cls.name, cls.email, cls.phone, cls.address, cls.specialization, cls.experience, cls.fee
            ).filter(cls.id == ID).all()

            result_dicts = [
                {"name": name, "email": email, "phone": phone, "address": address,
                    "specialization": specialization, "experience": experience, "fee": fee}
                for name, email, phone, address, specialization, experience, fee in results
            ]

        return result_dicts


class Patient(Base):
    __tablename__ = 'patient'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    gender = Column(String(255), nullable=False)
    email = Column(String(255))
    password = Column(String(255), nullable=False)
    phone = Column(String(255), nullable=False)
    address = Column(String(255))
    dob = Column(Date)
    diagnosis = Column(String(255))
    last_visit = Column(Date)

    @classmethod
    def get_basic_info(cls, session: Session, ID):
        results = session.query(
            cls.name, cls.gender, cls.email, cls.phone, cls.address,
            cls.age, cls.diagnosis, cls.last_visit, Doctor.name
        ).join(Doctor, cls.doctor_id == Doctor.id).filter(cls.id == ID).all()
        result_dict = {"name": results[0], "gender": results[1], "email": results[2], "phone": results[3],
                       "address": results[4], "age": results[5], "diagnosis": results[6], "last_visit": results[7],
                       "doctor": results[8]}
        return result_dict

    @classmethod
    def add_patient(cls, session: Session, **kwargs):
        patient = cls(**kwargs)
        session.add(patient)
        session.commit()
        return patient.id

    @classmethod
    def get_patient(cls, session: Session, email):
        result = session.query(
            cls.id, cls.name, cls.email, cls.phone, cls.address, cls.dob).filter(cls.email == email).first()
        if result:
            dict_result = {
                "id": result.id,
                "name": result.name,
                "email": result.email,
                "phone": result.phone,
                "address": result.address,
                "dob": str(result.dob)
            }
            print(dict_result)
            return dict_result
        return None

    @classmethod
    def check_patient(cls, session: Session, email, password):
        result = session.query(cls.id).filter(
            cls.email == email, cls.password == password).all()
        if result:
            return result[0]
        return None
