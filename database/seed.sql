-- Healthcare Management System - Seed Data
-- Note: All passwords are BCrypt hashed
-- Admin password: admin123
-- Doctor password: doctor123
-- Patient password: patient123
-- Hash: $2a$10$xqkCEjF5.xZZKEIoY5H7R.pUWvKR9hKbGhL9NZ9Pz0zCZKf0J/pMy

-- Insert Admin User
INSERT INTO users (email, password, full_name, role, phone) VALUES
('admin@healthcare.com', '$2a$10$xqkCEjF5.xZZKEIoY5H7R.pUWvKR9hKbGhL9NZ9Pz0zCZKf0J/pMy', 'System Administrator', 'ADMIN', '+1234567890');

-- Insert Doctor Users
INSERT INTO users (email, password, full_name, role, phone) VALUES
('doctor1@healthcare.com', '$2a$10$xqkCEjF5.xZZKEIoY5H7R.pUWvKR9hKbGhL9NZ9Pz0zCZKf0J/pMy', 'Dr. Sarah Johnson', 'DOCTOR', '+1234567891'),
('doctor2@healthcare.com', '$2a$10$xqkCEjF5.xZZKEIoY5H7R.pUWvKR9hKbGhL9NZ9Pz0zCZKf0J/pMy', 'Dr. Michael Chen', 'DOCTOR', '+1234567892'),
('doctor3@healthcare.com', '$2a$10$xqkCEjF5.xZZKEIoY5H7R.pUWvKR9hKbGhL9NZ9Pz0zCZKf0J/pMy', 'Dr. Emily Williams', 'DOCTOR', '+1234567893');

-- Insert Doctor Profiles
INSERT INTO doctor_profiles (user_id, specialization, experience_years, qualification, availability_days, consultation_fee) VALUES
(2, 'Cardiology', 10, 'MD Cardiology', 'MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY', 150.00),
(3, 'Orthopedics', 8, 'MS Orthopedics', 'MONDAY,WEDNESDAY,FRIDAY', 120.00),
(4, 'General Medicine', 15, 'MBBS, MD', 'MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY,SATURDAY', 100.00);

-- Insert Patient Users
INSERT INTO users (email, password, full_name, role, phone) VALUES
('patient1@healthcare.com', '$2a$10$xqkCEjF5.xZZKEIoY5H7R.pUWvKR9hKbGhL9NZ9Pz0zCZKf0J/pMy', 'John Doe', 'PATIENT', '+1234567894'),
('patient2@healthcare.com', '$2a$10$xqkCEjF5.xZZKEIoY5H7R.pUWvKR9hKbGhL9NZ9Pz0zCZKf0J/pMy', 'Jane Smith', 'PATIENT', '+1234567895'),
('patient3@healthcare.com', '$2a$10$xqkCEjF5.xZZKEIoY5H7R.pUWvKR9hKbGhL9NZ9Pz0zCZKf0J/pMy', 'Bob Johnson', 'PATIENT', '+1234567896');

-- Insert Patient Profiles
INSERT INTO patient_profiles (user_id, date_of_birth, gender, blood_group, address, emergency_contact) VALUES
(5, '1990-05-15', 'MALE', 'A+', '123 Main St, Springfield, IL', '+1234567897'),
(6, '1985-08-22', 'FEMALE', 'B+', '456 Oak Ave, Springfield, IL', '+1234567898'),
(7, '1995-03-10', 'MALE', 'O+', '789 Pine Rd, Springfield, IL', '+1234567899');

-- Insert Sample Appointments (dates spread across next 2 weeks)
INSERT INTO appointments (patient_id, doctor_id, appointment_date, appointment_time, status, reason, notes) VALUES
(5, 2, DATE_ADD(CURDATE(), INTERVAL 2 DAY), '10:00:00', 'SCHEDULED', 'Chest pain and shortness of breath', 'First-time consultation'),
(6, 3, DATE_ADD(CURDATE(), INTERVAL 3 DAY), '14:30:00', 'SCHEDULED', 'Knee pain after jogging', 'Patient reports pain for 2 weeks'),
(7, 4, DATE_ADD(CURDATE(), INTERVAL 5 DAY), '09:00:00', 'SCHEDULED', 'Annual checkup', 'Regular health screening'),
(5, 4, DATE_ADD(CURDATE(), INTERVAL -7 DAY), '11:00:00', 'COMPLETED', 'Fever and cold', 'Patient recovered well'),
(6, 2, DATE_ADD(CURDATE(), INTERVAL -3 DAY), '15:00:00', 'COMPLETED', 'Follow-up for hypertension', 'Blood pressure stable');

-- Insert Prescriptions (for completed appointments)
INSERT INTO prescriptions (appointment_id, patient_id, doctor_id, diagnosis, notes) VALUES
(4, 5, 4, 'Viral upper respiratory infection', 'Rest and hydration recommended. Follow up if symptoms worsen.'),
(5, 6, 2, 'Essential Hypertension', 'Continue current medication. Monitor blood pressure daily.');

-- Insert Prescription Items
INSERT INTO prescription_items (prescription_id, medicine_name, dosage, frequency, duration, instructions) VALUES
(1, 'Paracetamol', '500mg', 'Three times a day', '5 days', 'Take after meals'),
(1, 'Cetirizine', '10mg', 'Once a day', '5 days', 'Take at bedtime'),
(1, 'Vitamin C', '500mg', 'Once a day', '7 days', 'Take with breakfast'),
(2, 'Amlodipine', '5mg', 'Once a day', '30 days', 'Take in the morning'),
(2, 'Aspirin', '75mg', 'Once a day', '30 days', 'Take after dinner');

-- Insert Medical Records
INSERT INTO medical_records (patient_id, doctor_id, appointment_id, record_type, title, description) VALUES
(5, 4, 4, 'DIAGNOSIS', 'Viral Upper Respiratory Infection', 'Patient presented with fever (101Â°F), nasal congestion, and sore throat. Physical examination revealed inflamed throat. Diagnosed as viral URTI. Prescribed symptomatic treatment.'),
(6, 2, 5, 'LAB_RESULT', 'Blood Pressure Monitoring', 'BP Reading: 128/82 mmHg. Heart rate: 72 bpm. Patient shows improvement on current medication. Continue monitoring.'),
(7, 4, NULL, 'NOTE', 'Patient Health Summary', 'Patient is generally healthy. No chronic conditions. Maintains active lifestyle. Recommended annual checkup scheduled.');
