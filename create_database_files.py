import os

db_dir = r'C:\Users\Arunkumar\Desktop\hc\database'
os.makedirs(db_dir, exist_ok=True)
print('Database directory created successfully')

# Also create the SQL files directly
schema_sql = """-- Healthcare Management System - Database Schema
-- Drop tables in reverse dependency order
DROP TABLE IF EXISTS prescription_items;
DROP TABLE IF EXISTS prescriptions;
DROP TABLE IF EXISTS medical_records;
DROP TABLE IF EXISTS appointments;
DROP TABLE IF EXISTS patient_profiles;
DROP TABLE IF EXISTS doctor_profiles;
DROP TABLE IF EXISTS users;

-- Users table (base table for all user types)
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    role ENUM('ADMIN', 'DOCTOR', 'PATIENT') NOT NULL,
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_email (email),
    INDEX idx_role (role)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Doctor profiles table
CREATE TABLE doctor_profiles (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL UNIQUE,
    specialization VARCHAR(255) NOT NULL,
    experience_years INT NOT NULL,
    qualification VARCHAR(500) NOT NULL,
    availability_days VARCHAR(255),
    consultation_fee DECIMAL(10, 2) DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_specialization (specialization)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Patient profiles table
CREATE TABLE patient_profiles (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL UNIQUE,
    date_of_birth DATE NOT NULL,
    gender ENUM('MALE', 'FEMALE', 'OTHER') NOT NULL,
    blood_group VARCHAR(10),
    address TEXT,
    emergency_contact VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_blood_group (blood_group)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Appointments table
CREATE TABLE appointments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    status ENUM('SCHEDULED', 'COMPLETED', 'CANCELLED', 'NO_SHOW') DEFAULT 'SCHEDULED',
    reason TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (doctor_id) REFERENCES users(id) ON DELETE CASCADE,
    UNIQUE KEY unique_appointment_slot (doctor_id, appointment_date, appointment_time),
    INDEX idx_patient_id (patient_id),
    INDEX idx_doctor_id (doctor_id),
    INDEX idx_appointment_date (appointment_date),
    INDEX idx_status (status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Prescriptions table
CREATE TABLE prescriptions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    appointment_id INT NOT NULL,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    diagnosis TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (appointment_id) REFERENCES appointments(id) ON DELETE CASCADE,
    FOREIGN KEY (patient_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (doctor_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_patient_id (patient_id),
    INDEX idx_doctor_id (doctor_id),
    INDEX idx_appointment_id (appointment_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Prescription items table
CREATE TABLE prescription_items (
    id INT PRIMARY KEY AUTO_INCREMENT,
    prescription_id INT NOT NULL,
    medicine_name VARCHAR(255) NOT NULL,
    dosage VARCHAR(100) NOT NULL,
    frequency VARCHAR(100) NOT NULL,
    duration VARCHAR(100) NOT NULL,
    instructions TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (prescription_id) REFERENCES prescriptions(id) ON DELETE CASCADE,
    INDEX idx_prescription_id (prescription_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Medical records table
CREATE TABLE medical_records (
    id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_id INT,
    record_type ENUM('DIAGNOSIS', 'LAB_RESULT', 'PRESCRIPTION', 'NOTE', 'OTHER') DEFAULT 'NOTE',
    title VARCHAR(255) NOT NULL,
    description TEXT,
    file_path VARCHAR(500),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (doctor_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (appointment_id) REFERENCES appointments(id) ON DELETE SET NULL,
    INDEX idx_patient_id (patient_id),
    INDEX idx_doctor_id (doctor_id),
    INDEX idx_record_type (record_type),
    INDEX idx_created_at (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""

seed_sql = """-- Healthcare Management System - Seed Data
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
(5, 4, 4, 'DIAGNOSIS', 'Viral Upper Respiratory Infection', 'Patient presented with fever (101°F), nasal congestion, and sore throat. Physical examination revealed inflamed throat. Diagnosed as viral URTI. Prescribed symptomatic treatment.'),
(6, 2, 5, 'LAB_RESULT', 'Blood Pressure Monitoring', 'BP Reading: 128/82 mmHg. Heart rate: 72 bpm. Patient shows improvement on current medication. Continue monitoring.'),
(7, 4, NULL, 'NOTE', 'Patient Health Summary', 'Patient is generally healthy. No chronic conditions. Maintains active lifestyle. Recommended annual checkup scheduled.');
"""

drop_all_sql = """-- Healthcare Management System - Drop All Tables
-- Use this script to reset the database completely

-- Drop tables in reverse dependency order
DROP TABLE IF EXISTS prescription_items;
DROP TABLE IF EXISTS prescriptions;
DROP TABLE IF EXISTS medical_records;
DROP TABLE IF EXISTS appointments;
DROP TABLE IF EXISTS patient_profiles;
DROP TABLE IF EXISTS doctor_profiles;
DROP TABLE IF EXISTS users;

-- Confirmation message
SELECT 'All tables dropped successfully' AS Status;
"""

verify_sql = """-- Healthcare Management System - Verification Script
-- Run this script to verify data has been loaded correctly

-- Count records in all tables
SELECT 'Users' as Table_Name, COUNT(*) as Count FROM users
UNION ALL SELECT 'Doctor Profiles', COUNT(*) FROM doctor_profiles
UNION ALL SELECT 'Patient Profiles', COUNT(*) FROM patient_profiles
UNION ALL SELECT 'Appointments', COUNT(*) FROM appointments
UNION ALL SELECT 'Prescriptions', COUNT(*) FROM prescriptions
UNION ALL SELECT 'Prescription Items', COUNT(*) FROM prescription_items
UNION ALL SELECT 'Medical Records', COUNT(*) FROM medical_records;

-- Display all users by role
SELECT '-- Users by Role --' as Info;
SELECT role, COUNT(*) as Count, GROUP_CONCAT(email SEPARATOR ', ') as Emails
FROM users
GROUP BY role
ORDER BY role;

-- Display upcoming appointments
SELECT '-- Upcoming Appointments --' as Info;
SELECT 
    a.id,
    a.appointment_date,
    a.appointment_time,
    p.full_name as Patient,
    d.full_name as Doctor,
    a.status,
    a.reason
FROM appointments a
JOIN users p ON a.patient_id = p.id
JOIN users d ON a.doctor_id = d.id
WHERE a.appointment_date >= CURDATE()
ORDER BY a.appointment_date, a.appointment_time;

-- Display doctors with their specializations
SELECT '-- Doctors and Specializations --' as Info;
SELECT 
    u.full_name as Doctor_Name,
    dp.specialization,
    dp.experience_years,
    dp.consultation_fee,
    dp.availability_days
FROM users u
JOIN doctor_profiles dp ON u.id = dp.user_id
ORDER BY u.full_name;

-- Display patients with their details
SELECT '-- Patients --' as Info;
SELECT 
    u.full_name as Patient_Name,
    pp.date_of_birth,
    pp.gender,
    pp.blood_group,
    u.phone
FROM users u
JOIN patient_profiles pp ON u.id = pp.user_id
ORDER BY u.full_name;
"""

# Write all SQL files
with open(os.path.join(db_dir, 'schema.sql'), 'w', encoding='utf-8') as f:
    f.write(schema_sql)
print('Created schema.sql')

with open(os.path.join(db_dir, 'seed.sql'), 'w', encoding='utf-8') as f:
    f.write(seed_sql)
print('Created seed.sql')

with open(os.path.join(db_dir, 'drop_all.sql'), 'w', encoding='utf-8') as f:
    f.write(drop_all_sql)
print('Created drop_all.sql')

with open(os.path.join(db_dir, 'verify.sql'), 'w', encoding='utf-8') as f:
    f.write(verify_sql)
print('Created verify.sql')

print('\\nAll database SQL files created successfully!')
