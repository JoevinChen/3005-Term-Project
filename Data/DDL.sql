CREATE TABLE IF NOT EXISTS Members
(
    member_id SERIAL PRIMARY KEY,
    email TEXT NOT NULL UNIQUE,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    f_name VARCHAR(255) NOT NULL,
    l_name VARCHAR(255) NOT NULL,
    age INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Trainer
(
    trainer_id SERIAL PRIMARY KEY,
    email TEXT NOT NULL UNIQUE,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    f_name VARCHAR(255) NOT NULL,
    l_name VARCHAR(255) NOT NULL,
    age INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Admins
(
    admin_id SERIAL PRIMARY KEY,
    email TEXT NOT NULL UNIQUE,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    f_name VARCHAR(255) NOT NULL,
    l_name VARCHAR(255) NOT NULL,
    age INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Room
(
    room_id SERIAL PRIMARY KEY,
    room_number INT NOT NULL UNIQUE,
    room_use TEXT NOT NULL DEFAULT 'NOT IN USE'
);

CREATE TABLE IF NOT EXISTS HealthMetric
(
    member_id INT NOT NULL,
    user_weight INT NOT NULL,
    height INT NOT NULL,
    bmi FLOAT(5) NOT NULL,
    FOREIGN KEY (member_id) REFERENCES Members (member_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS FitnessGoals
(
    member_id INT NOT NULL,
    weight_goal INT NOT NULL,
    date_started DATE NOT NULL,
    FOREIGN KEY (member_id) REFERENCES Members (member_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Achievements
(
    member_id INT NOT NULL,
    achievement TEXT NOT NULL,
    date_completed DATE NOT NULL,
    FOREIGN KEY (member_id) REFERENCES Members (member_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS ExerciseRoutine
(
    exercise_id SERIAL PRIMARY KEY,
    exercise_name TEXT NOT NULL UNIQUE,
    member_id INT NOT NULL,
    sets INT NOT NULL,
    weight INT NOT NULL,
    reps INT NOT NULL,
    FOREIGN KEY (member_id) REFERENCES Members (member_id) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS Payment
(
    member_id INT NOT NULL,
    bill_reason TEXT NOT NULL,
    billing_fee FLOAT(5) NOT NULL DEFAULT 0,
    amount_paid FLOAT(5) NOT NULL DEFAULT 0,
    FOREIGN KEY (member_id) REFERENCES Members (member_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Availability
(
    trainer_id INT NOT NULL UNIQUE,
    date_available DATE NOT NULL UNIQUE,
    start_time TIME NOT NULL DEFAULT '06:00:00' UNIQUE,
    end_time TIME NOT NULL DEFAULT '18:00:00' UNIQUE,
    FOREIGN KEY (trainer_id) REFERENCES Trainer (trainer_id) ON DELETE CASCADE,
    PRIMARY KEY (trainer_id, date_available)
);

CREATE TABLE IF NOT EXISTS GroupTraining
(
    class_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    max_capacity INT NOT NULL,
    Members_registered INT NOT NULL,
    date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    room_id INT NOT NULL,
    trainer_id INT NOT NULL,
    FOREIGN KEY (trainer_id) REFERENCES Trainer (trainer_id) ON DELETE CASCADE,
    FOREIGN KEY (room_id) REFERENCES Room (room_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Equipment
(
    equipment_id SERIAL PRIMARY KEY,
    equipment_name TEXT NOT NULL,
    maintenance_status TEXT NOT NULL DEFAULT 'NOT IN NEED',
    maintenance_date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS Trains
(    
    member_id INT NOT NULL,
    trainer_id INT NOT NULL,
    booking_start_time TIME NOT NULL,
    booking_end_time TIME NOT NULL,
    booking_date DATE NOT NULL,
    FOREIGN KEY (trainer_id) REFERENCES Trainer (trainer_id) ON DELETE CASCADE,
    FOREIGN KEY (member_id) REFERENCES Members (member_id) ON DELETE CASCADE,
    PRIMARY KEY(trainer_id, member_id)
);

CREATE TABLE IF NOT EXISTS Participates
(
    member_id INT NOT NULL,
    class_id INT NOT NULL,
    FOREIGN KEY (class_id) REFERENCES GroupTraining (class_id) ON DELETE CASCADE,
    FOREIGN KEY (member_id) REFERENCES Members (member_id) ON DELETE CASCADE,
    PRIMARY KEY(class_id, member_id)
);