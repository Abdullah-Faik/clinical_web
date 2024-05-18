INSERT INTO
    doctor (
        name,
        email,
        phone,
        address,
        specialization,
        experience,
        fee
    )
VALUES
    (
        'Dr. Sarah Johnson',
        'sarah.johnson@example.com',
        '555-123-4567',
        '123 Main Street, Springfield',
        'Pediatrics',
        15,
        150
    ),
    (
        'Dr. Michael Chang',
        'michael.chang@example.com',
        '555-987-6543',
        '456 Oak Avenue, Oakville',
        'Cardiology',
        20,
        200
    ),
    (
        'Dr. Emily Rodriguez',
        'emily.rodriguez@example.com',
        '555-456-7890',
        '789 Elm Street, Elmwood',
        'Dermatology',
        10,
        120
    ),
    (
        'Dr. Daniel Lee',
        'daniel.lee@example.com',
        '555-234-5678',
        '567 Pine Street, Pinewood',
        'Orthopedics',
        18,
        180
    ),
    (
        'Dr. Jessica Martinez',
        'jessica.martinez@example.com',
        '555-876-5432',
        '890 Maple Street, Mapleville',
        'Neurology',
        12,
        140
    ),
    (
        'Dr. David Kim',
        'david.kim@example.com',
        '555-345-6789',
        '234 Cedar Street, Cedarville',
        'Pediatrics',
        25,
        250
    ),
    (
        'Dr. Samantha Patel',
        'samantha.patel@example.com',
        '555-654-3210',
        '678 Birch Street, Birchwood',
        'Cardiology',
        8,
        100
    ),
    (
        'Dr. Christopher Nguyen',
        'christopher.nguyen@example.com',
        '555-543-2109',
        '345 Elm Street, Elmville',
        'Dermatology',
        14,
        130
    );

-- Path: project.session.sql
SELECT
    *
FROM
    doctor;

show tables;

INSERT INTO
    patient (
        name,
        gender,
        email,
        password,
        phone,
        address,
        dob
    )
VALUES
    (
        'John Doe',
        'male',
        'johndoe@example.com',
        'password123',
        '555-234-5678',
        '456 Elm Street, Springfield',
        '1995-05-15'
    ),
    (
        'Jane Roe',
        'female',
        'janeroe@example.com',
        'pass1234',
        '555-345-6789',
        '1988-02-20'
    ),
    (
        'Michael Johnson',
        'male',
        'michaelj@example.com',
        'mypass987',
        '555-456-7890',
        '1992-08-30'
    ),
    (
        'Emily Davis',
        'female',
        'emilyd@example.com',
        'emilypass',
        '555-567-8901',
        '2001-12-10'
    ),
    (
        'Chris Brown',
        'male',
        'chrisb@example.com',
        'chris123',
        '555-678-9012',
        '1985-07-25'
    ),
    (
        'Patricia Miller',
        'female',
        'patriciam@example.com',
        'patricia456',
        '555-789-0123',
        '1978-03-14'
    ),
    (
        'David Wilson',
        'male',
        'davidw@example.com',
        'davidpass',
        '555-890-1234',
        '1990-11-11'
    ),
    (
        'Sophia Moore',
        'female',
        'sophiam@example.com',
        'sophia789',
        '555-901-2345',
        '2003-09-22'
    ),
    (
        'James Taylor',
        'male',
        'jamest@example.com',
        'jamestaylor',
        '555-012-3456',
        '1982-06-17'
    ),
    (
        'Olivia Martinez',
        'female',
        'oliviam@example.com',
        'olivia123',
        '555-123-4568',
        '1998-04-08'
    );

SELECT
    *
FROM
    patient;