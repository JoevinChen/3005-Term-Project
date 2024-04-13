-- Name: Danny Tran, Joevin Chen, Steven Lin
-- Student Number: 101225611, 101227689, 101240382

-- Insert sample data into the Admins table
INSERT INTO Admins (email, username, password, f_name, l_name, age) VALUES
('moofood0@gmail.com', 'bignut100', 'pass1', 'Danny', 'Tran', 20),
('slin1@ocdsb.ca', 'hekboner', 'pass2', 'Steven', 'Lin', 20),
('joevinchen2003@gmail.com', 'gengai', 'pass3', 'Joevin', 'Chen', 20);

-- Insert sample data into the Room table
INSERT INTO Room (room_number, room_use) VALUES
(101, 'Booked'),
(102, 'Booked'),
(103, 'Booked'),
(104, 'Not in use'),
(105, 'Not in use');

-- Insert sample data into the Equipment Table
INSERT INTO Equipment (equipment_name, maintenance_status, maintenance_date) VALUES
('Leg Press', 'New', '2024-04-01'),
('Bench Press', 'Good', '2024-03-13'),
('Cable', 'Broken', '2024-03-17'),
('Lat Pulldown', 'Good', '2024-04-15'),
('Leg Extension', 'Good', '2024-04-01');

-- Insert sample data into the Trainer table
INSERT INTO Trainer (email, username, password, f_name, l_name, age) VALUES
('veggiefa@outlook.com', 'veggiedawg', 'pass1', 'Justin', 'Yu', 45),
('nugget@gmail.com', 'nugget', 'pass2', 'Nugget', 'Nong', 20),
('junfat@gmail.com', 'jun', 'pass3', 'Jun', 'Zhang', 21);

-- Insert sample data into the GroupTraining Table
INSERT INTO GroupTraining (name, max_capacity, members_registered, date, start_time, end_time, room_id, trainer_id) VALUES
('Yoga', '50', '40', '2024-03-16', '11:00:00', '12:00:00', 1, 1),
('Pilates', '50', '20', '2024-03-17', '12:00:00', '13:00:00', 2, 2),
('Zumba', '50', '33', '2024-03-18', '13:00:00', '14:00:00', 3, 3);

-- Insert sample data into the Members Table
INSERT INTO Members (email, username, password, f_name, l_name, age) VALUES
('mlin1@gmail.com', 'mani', 'pass1', 'Manikanth', 'Lin', 39),
('dereck@outlook.com', 'dza', 'pass2', 'Dereck', 'Zhang', 59),
('ethan@gmail.com', 'efan', 'pass3', 'Ethan', 'Gefan', 22);

-- Insert sample data into the Payment table
INSERT INTO Payment (member_id, bill_reason, billing_fee, amount_paid) VALUES
(1, 'Membership Renewal', 10.00, 10.00),
(2, 'Membership Renewal', 20.00, 0),
(3, 'Membership Renewal', 30.00, 0),
(2, 'Membership Renewal', 20.00, 20.00);

-- Insert sample data into the FitnessGoals table
INSERT INTO FitnessGoals (member_id, weight_goal, date_started) VALUES
(1, 150, '2024-03-01'),
(2, 180, '2024-04-15'),
(3, 190, '2024-03-30');

-- Insert sample data into ExerciseRoutine table 
INSERT INTO ExerciseRoutine (member_id, exercise_name, sets, weight, reps) VALUES
(1, 'Bench Press', 3, 100, 10),
(1, 'Squats', 3, 200, 10), 
(1, 'Deadlifts', 3, 300, 10),
(1, 'Leg Press', 3, 400, 10),
(1, 'Leg Extension', 3, 100, 10);

-- Insert sample data into the Achievements Table
INSERT INTO Achievements (member_id, achievement, date_completed) VALUES
(1, 'Ran 5km', '2024-03-01'),
(2, 'Benched 100', '2024-03-15'),
(3, 'Squatted 300', '2024-03-30');

-- Insert sample data into the HealthMetric table
INSERT INTO HealthMetric (member_id, user_weight, height, bmi) VALUES
(1, 150, 177, 21.5),
(2, 180, 183, 24.5),
(3, 190, 174, 29);

-- Insert sample data into the Availability table
INSERT INTO Availability (trainer_id, date_available, start_time, end_time) VALUES
(1, '2024-03-15', '06:00:00', '12:00:00'),
(2, '2024-03-16', '10:00:00', '18:00:00'),
(3, '2024-03-17', '12:00:00', '18:00:00');

-- Insert sample data into the Trains table
INSERT INTO Trains(member_id, trainer_id, booking_start_time, booking_end_time, booking_date) VALUES
(1, 1, '06:00:00', '07:00:00', '2024-03-15'),
(2, 2, '10:00:00', '12:00:00', '2024-03-16');

-- Insert sample data into the Participates table
INSERT INTO Participates (member_id, class_id) VALUES
(1, 2),
(1, 1),
(2, 1),
(3, 3);