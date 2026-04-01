-- Healthcare Management System - Drop All Tables
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
