CREATE DATABASE IF NOT EXISTS calendar;

USE calendar;

CREATE TABLE IF NOT EXISTS doctor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    specialization VARCHAR(255) NOT NULL,
    experience INT NOT NULL,
    fee INT NOT NULL
);

CREATE TABLE IF NOT EXISTS patient (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    gender VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    password VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    dob DATE,
    diagnosis VARCHAR(255),
    last_visit DATE
);

CREATE TABLE IF NOT EXISTS available_appointment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    doctor_id INT NOT NULL,
    date DATE NOT NULL,
    time TIME NOT NULL,
    status ENUM('available', 'booked') NOT NULL,
    FOREIGN KEY (doctor_id) REFERENCES doctor(id)
);

CREATE TABLE IF NOT EXISTS appointment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    doctor_id INT NOT NULL,
    patient_id INT NOT NULL,
    date DATE NOT NULL,
    time TIME NOT NULL,
    status ENUM('pending', 'confirmed', 'cancelled') NOT NULL,
    FOREIGN KEY (doctor_id) REFERENCES doctor(id),
    FOREIGN KEY (patient_id) REFERENCES patient(id)
);

--  appointment resport
CREATE TABLE IF NOT EXISTS appointment_report (
    id INT AUTO_INCREMENT PRIMARY KEY,
    appointment_id INT NOT NULL,
    medication VARCHAR(255),
    diagnosis VARCHAR(255),
    advice VARCHAR(255),
    requested_tests VARCHAR(255),
    follow_up DATE,
    FOREIGN KEY (appointment_id) REFERENCES appointment(id)
);

SHOW DATABASES;

