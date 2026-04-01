-- Healthcare Management System - Verification Script
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
