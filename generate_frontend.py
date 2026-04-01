import os

# Base directory for frontend files
FRONTEND_DIR = r"C:\Users\Arunkumar\Desktop\hc\frontend"

# Create frontend directory if it doesn't exist
os.makedirs(FRONTEND_DIR, exist_ok=True)

# API Base URL
API_BASE = "http://localhost:8080/api"

# ============================================================================
# CSS CONTENT
# ============================================================================
css_content = """/* Healthcare Management System - Modern Styles */

:root {
    --primary: #007bff;
    --primary-dark: #0056b3;
    --success: #28a745;
    --danger: #dc3545;
    --warning: #ffc107;
    --info: #17a2b8;
    --light: #f8f9fa;
    --dark: #343a40;
    --white: #ffffff;
    --gray: #6c757d;
    --border: #dee2e6;
    --shadow: rgba(0, 0, 0, 0.1);
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    color: var(--dark);
    background-color: var(--light);
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

/* Header Styles */
header {
    background: linear-gradient(135deg, var(--primary), var(--primary-dark));
    color: var(--white);
    padding: 1rem 0;
    box-shadow: 0 2px 10px var(--shadow);
}

.header-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

.logo {
    font-size: 1.8rem;
    font-weight: bold;
    display: flex;
    align-items: center;
    gap: 10px;
}

.logo::before {
    content: "⚕️";
    font-size: 2rem;
}

/* Hero Section */
.hero {
    text-align: center;
    padding: 80px 20px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: var(--white);
    margin-bottom: 40px;
}

.hero h1 {
    font-size: 3rem;
    margin-bottom: 20px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.hero p {
    font-size: 1.3rem;
    margin-bottom: 30px;
    opacity: 0.9;
}

.hero-buttons {
    display: flex;
    gap: 20px;
    justify-content: center;
    flex-wrap: wrap;
}

/* Card Styles */
.card {
    background: var(--white);
    border-radius: 10px;
    box-shadow: 0 4px 6px var(--shadow);
    padding: 25px;
    margin-bottom: 25px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 12px var(--shadow);
}

.card-header {
    border-bottom: 2px solid var(--primary);
    padding-bottom: 15px;
    margin-bottom: 20px;
}

.card-header h2 {
    color: var(--primary);
    font-size: 1.5rem;
}

.card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    margin-bottom: 30px;
}

/* Form Styles */
.form-group {
    margin-bottom: 20px;
}

.form-group label {
    display: block;
    margin-bottom: 8px;
    font-weight: 600;
    color: var(--dark);
}

.form-group input,
.form-group select,
.form-group textarea {
    width: 100%;
    padding: 12px;
    border: 2px solid var(--border);
    border-radius: 6px;
    font-size: 1rem;
    transition: border-color 0.3s ease;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
    outline: none;
    border-color: var(--primary);
}

.form-group textarea {
    resize: vertical;
    min-height: 100px;
}

.radio-group {
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
}

.radio-group label {
    display: flex;
    align-items: center;
    gap: 8px;
    font-weight: normal;
    cursor: pointer;
}

.radio-group input[type="radio"] {
    width: auto;
}

/* Button Styles */
.btn {
    padding: 12px 30px;
    border: none;
    border-radius: 6px;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
    display: inline-block;
    text-align: center;
}

.btn-primary {
    background: var(--primary);
    color: var(--white);
}

.btn-primary:hover {
    background: var(--primary-dark);
    transform: translateY(-2px);
    box-shadow: 0 4px 8px var(--shadow);
}

.btn-success {
    background: var(--success);
    color: var(--white);
}

.btn-success:hover {
    background: #218838;
}

.btn-danger {
    background: var(--danger);
    color: var(--white);
}

.btn-danger:hover {
    background: #c82333;
}

.btn-warning {
    background: var(--warning);
    color: var(--dark);
}

.btn-warning:hover {
    background: #e0a800;
}

.btn-secondary {
    background: var(--gray);
    color: var(--white);
}

.btn-secondary:hover {
    background: #5a6268;
}

.btn-sm {
    padding: 6px 15px;
    font-size: 0.9rem;
}

/* Table Styles */
table {
    width: 100%;
    border-collapse: collapse;
    background: var(--white);
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 4px var(--shadow);
}

thead {
    background: var(--primary);
    color: var(--white);
}

th, td {
    padding: 15px;
    text-align: left;
    border-bottom: 1px solid var(--border);
}

tbody tr:hover {
    background: var(--light);
}

tbody tr:last-child td {
    border-bottom: none;
}

/* Alert Styles */
.alert {
    padding: 15px 20px;
    border-radius: 6px;
    margin-bottom: 20px;
    display: none;
}

.alert.show {
    display: block;
}

.alert-success {
    background: #d4edda;
    color: #155724;
    border-left: 4px solid var(--success);
}

.alert-danger {
    background: #f8d7da;
    color: #721c24;
    border-left: 4px solid var(--danger);
}

.alert-warning {
    background: #fff3cd;
    color: #856404;
    border-left: 4px solid var(--warning);
}

.alert-info {
    background: #d1ecf1;
    color: #0c5460;
    border-left: 4px solid var(--info);
}

/* Stats Cards */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    margin-bottom: 30px;
}

.stat-card {
    background: linear-gradient(135deg, var(--primary), var(--primary-dark));
    color: var(--white);
    padding: 30px;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0 4px 6px var(--shadow);
}

.stat-card h3 {
    font-size: 2.5rem;
    margin-bottom: 10px;
}

.stat-card p {
    font-size: 1.1rem;
    opacity: 0.9;
}

/* Doctor Cards */
.doctor-card {
    background: var(--white);
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 2px 4px var(--shadow);
    transition: transform 0.3s ease;
}

.doctor-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 8px var(--shadow);
}

.doctor-card h3 {
    color: var(--primary);
    margin-bottom: 10px;
}

.doctor-card .specialization {
    color: var(--success);
    font-weight: 600;
    margin-bottom: 10px;
}

.doctor-card .info {
    color: var(--gray);
    font-size: 0.9rem;
    margin-bottom: 5px;
}

/* Auth Forms */
.auth-container {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 20px;
}

.auth-card {
    background: var(--white);
    border-radius: 10px;
    padding: 40px;
    max-width: 500px;
    width: 100%;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}

.auth-card h2 {
    text-align: center;
    color: var(--primary);
    margin-bottom: 30px;
    font-size: 2rem;
}

.auth-links {
    text-align: center;
    margin-top: 20px;
}

.auth-links a {
    color: var(--primary);
    text-decoration: none;
    font-weight: 600;
}

.auth-links a:hover {
    text-decoration: underline;
}

/* Loading Spinner */
.loading {
    display: inline-block;
    width: 20px;
    height: 20px;
    border: 3px solid rgba(255,255,255,.3);
    border-radius: 50%;
    border-top-color: var(--white);
    animation: spin 1s ease-in-out infinite;
}

@keyframes spin {
    to { transform: rotate(360deg); }
}

/* Medicine Items Table */
.medicine-items {
    margin-top: 20px;
}

.medicine-item {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr 1fr auto;
    gap: 10px;
    margin-bottom: 10px;
    align-items: end;
}

.medicine-item input {
    width: 100%;
}

/* Responsive Design */
@media (max-width: 768px) {
    .hero h1 {
        font-size: 2rem;
    }
    
    .hero p {
        font-size: 1rem;
    }
    
    .hero-buttons {
        flex-direction: column;
        align-items: stretch;
    }
    
    .header-content {
        flex-direction: column;
        gap: 15px;
    }
    
    .card-grid {
        grid-template-columns: 1fr;
    }
    
    .stats-grid {
        grid-template-columns: 1fr;
    }
    
    table {
        font-size: 0.9rem;
    }
    
    th, td {
        padding: 10px;
    }
    
    .medicine-item {
        grid-template-columns: 1fr;
    }
    
    .auth-card {
        padding: 25px;
    }
}

@media (max-width: 480px) {
    .container {
        padding: 10px;
    }
    
    .card {
        padding: 15px;
    }
    
    .btn {
        padding: 10px 20px;
        font-size: 0.9rem;
    }
}

/* Utility Classes */
.text-center {
    text-align: center;
}

.mt-20 {
    margin-top: 20px;
}

.mb-20 {
    margin-bottom: 20px;
}

.hidden {
    display: none;
}

.flex {
    display: flex;
}

.gap-10 {
    gap: 10px;
}

.justify-between {
    justify-content: space-between;
}

.align-center {
    align-items: center;
}
"""

# ============================================================================
# INDEX.HTML
# ============================================================================
index_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Healthcare Management System</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="hero">
        <div class="container">
            <h1>Healthcare Management System</h1>
            <p>Your Complete Healthcare Solution - Manage Appointments, Prescriptions & More</p>
            <div class="hero-buttons">
                <a href="login.html" class="btn btn-primary">Login</a>
                <a href="register.html" class="btn btn-success">Register as Patient</a>
            </div>
        </div>
    </div>

    <div class="container">
        <div class="card-grid">
            <div class="card">
                <h3>👨‍⚕️ For Doctors</h3>
                <p>Manage your appointments, update patient records, and write prescriptions efficiently.</p>
            </div>
            <div class="card">
                <h3>🏥 For Patients</h3>
                <p>Book appointments with top doctors, view your medical history, and manage prescriptions.</p>
            </div>
            <div class="card">
                <h3>⚙️ For Admins</h3>
                <p>Oversee the entire healthcare system, manage doctors, patients, and appointments.</p>
            </div>
        </div>

        <div class="card text-center">
            <h2>Why Choose Us?</h2>
            <div class="card-grid">
                <div>
                    <h4>🔒 Secure & Private</h4>
                    <p>Your health data is encrypted and secure</p>
                </div>
                <div>
                    <h4>📱 Easy to Use</h4>
                    <p>Simple and intuitive interface</p>
                </div>
                <div>
                    <h4>⚡ Fast & Reliable</h4>
                    <p>Quick appointment booking and management</p>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

# ============================================================================
# REGISTER.HTML
# ============================================================================
register_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register - Healthcare Management System</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="auth-container">
        <div class="auth-card">
            <h2>Patient Registration</h2>
            
            <div id="alertBox" class="alert"></div>
            
            <form id="registerForm">
                <div class="form-group">
                    <label for="name">Full Name *</label>
                    <input type="text" id="name" name="name" required>
                </div>
                
                <div class="form-group">
                    <label for="email">Email *</label>
                    <input type="email" id="email" name="email" required>
                </div>
                
                <div class="form-group">
                    <label for="password">Password *</label>
                    <input type="password" id="password" name="password" required minlength="6">
                </div>
                
                <div class="form-group">
                    <label for="phone">Phone Number *</label>
                    <input type="tel" id="phone" name="phone" required>
                </div>
                
                <div class="form-group">
                    <label for="dateOfBirth">Date of Birth *</label>
                    <input type="date" id="dateOfBirth" name="dateOfBirth" required>
                </div>
                
                <div class="form-group">
                    <label>Gender *</label>
                    <div class="radio-group">
                        <label>
                            <input type="radio" name="gender" value="MALE" required> Male
                        </label>
                        <label>
                            <input type="radio" name="gender" value="FEMALE"> Female
                        </label>
                        <label>
                            <input type="radio" name="gender" value="OTHER"> Other
                        </label>
                    </div>
                </div>
                
                <div class="form-group">
                    <label for="bloodGroup">Blood Group</label>
                    <select id="bloodGroup" name="bloodGroup">
                        <option value="">Select Blood Group</option>
                        <option value="A+">A+</option>
                        <option value="A-">A-</option>
                        <option value="B+">B+</option>
                        <option value="B-">B-</option>
                        <option value="AB+">AB+</option>
                        <option value="AB-">AB-</option>
                        <option value="O+">O+</option>
                        <option value="O-">O-</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="address">Address *</label>
                    <textarea id="address" name="address" required></textarea>
                </div>
                
                <button type="submit" class="btn btn-primary" style="width: 100%;">Register</button>
            </form>
            
            <div class="auth-links">
                <p>Already have an account? <a href="login.html">Login here</a></p>
                <p><a href="index.html">Back to Home</a></p>
            </div>
        </div>
    </div>

    <script>
        const API_BASE = '""" + API_BASE + """';
        
        function showAlert(message, type) {
            const alertBox = document.getElementById('alertBox');
            alertBox.className = `alert alert-${type} show`;
            alertBox.textContent = message;
            setTimeout(() => {
                alertBox.classList.remove('show');
            }, 5000);
        }
        
        document.getElementById('registerForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const formData = new FormData(e.target);
            const data = {
                name: formData.get('name'),
                email: formData.get('email'),
                password: formData.get('password'),
                phone: formData.get('phone'),
                dateOfBirth: formData.get('dateOfBirth'),
                gender: formData.get('gender'),
                bloodGroup: formData.get('bloodGroup') || null,
                address: formData.get('address')
            };
            
            try {
                const response = await fetch(`${API_BASE}/auth/register`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                });
                
                const result = await response.json();
                
                if (response.ok) {
                    localStorage.setItem('token', result.token);
                    localStorage.setItem('userRole', result.role);
                    localStorage.setItem('userName', result.name);
                    showAlert('Registration successful! Redirecting...', 'success');
                    setTimeout(() => {
                        window.location.href = 'patient-dashboard.html';
                    }, 1500);
                } else {
                    showAlert(result.message || 'Registration failed. Please try again.', 'danger');
                }
            } catch (error) {
                console.error('Error:', error);
                showAlert('Network error. Please check your connection.', 'danger');
            }
        });
    </script>
</body>
</html>
"""

# ============================================================================
# LOGIN.HTML
# ============================================================================
login_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Healthcare Management System</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="auth-container">
        <div class="auth-card">
            <h2>Login</h2>
            
            <div id="alertBox" class="alert"></div>
            
            <form id="loginForm">
                <div class="form-group">
                    <label for="email">Email</label>
                    <input type="email" id="email" name="email" required>
                </div>
                
                <div class="form-group">
                    <label for="password">Password</label>
                    <input type="password" id="password" name="password" required>
                </div>
                
                <button type="submit" class="btn btn-primary" style="width: 100%;">Login</button>
            </form>
            
            <div class="auth-links">
                <p>Don't have an account? <a href="register.html">Register here</a></p>
                <p><a href="index.html">Back to Home</a></p>
            </div>
        </div>
    </div>

    <script>
        const API_BASE = '""" + API_BASE + """';
        
        function showAlert(message, type) {
            const alertBox = document.getElementById('alertBox');
            alertBox.className = `alert alert-${type} show`;
            alertBox.textContent = message;
            setTimeout(() => {
                alertBox.classList.remove('show');
            }, 5000);
        }
        
        document.getElementById('loginForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const formData = new FormData(e.target);
            const data = {
                email: formData.get('email'),
                password: formData.get('password')
            };
            
            try {
                const response = await fetch(`${API_BASE}/auth/login`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                });
                
                const result = await response.json();
                
                if (response.ok) {
                    localStorage.setItem('token', result.token);
                    localStorage.setItem('userRole', result.role);
                    localStorage.setItem('userName', result.name);
                    
                    showAlert('Login successful! Redirecting...', 'success');
                    
                    setTimeout(() => {
                        if (result.role === 'PATIENT') {
                            window.location.href = 'patient-dashboard.html';
                        } else if (result.role === 'DOCTOR') {
                            window.location.href = 'doctor-dashboard.html';
                        } else if (result.role === 'ADMIN') {
                            window.location.href = 'admin-dashboard.html';
                        }
                    }, 1500);
                } else {
                    showAlert(result.message || 'Login failed. Please check your credentials.', 'danger');
                }
            } catch (error) {
                console.error('Error:', error);
                showAlert('Network error. Please check your connection.', 'danger');
            }
        });
    </script>
</body>
</html>
"""

# ============================================================================
# PATIENT-DASHBOARD.HTML
# ============================================================================
patient_dashboard_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Patient Dashboard - Healthcare Management System</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <div class="header-content">
            <div class="logo">Healthcare System</div>
            <div class="flex align-center gap-10">
                <span id="userName">Welcome!</span>
                <button onclick="logout()" class="btn btn-danger btn-sm">Logout</button>
            </div>
        </div>
    </header>

    <div class="container">
        <div id="alertBox" class="alert"></div>

        <!-- My Profile -->
        <div class="card">
            <div class="card-header">
                <h2>My Profile</h2>
            </div>
            <div id="profileContent">Loading...</div>
        </div>

        <!-- Available Doctors -->
        <div class="card">
            <div class="card-header">
                <h2>Available Doctors</h2>
            </div>
            <div id="doctorsGrid" class="card-grid">Loading...</div>
        </div>

        <!-- Book Appointment -->
        <div class="card">
            <div class="card-header">
                <h2>Book Appointment</h2>
            </div>
            <form id="bookAppointmentForm">
                <div class="form-group">
                    <label for="doctorId">Select Doctor</label>
                    <select id="doctorId" name="doctorId" required>
                        <option value="">Choose a doctor...</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="appointmentDate">Date</label>
                    <input type="date" id="appointmentDate" name="appointmentDate" required>
                </div>
                <div class="form-group">
                    <label for="appointmentTime">Time</label>
                    <input type="time" id="appointmentTime" name="appointmentTime" required>
                </div>
                <div class="form-group">
                    <label for="reason">Reason for Visit</label>
                    <textarea id="reason" name="reason" required></textarea>
                </div>
                <button type="submit" class="btn btn-primary">Book Appointment</button>
            </form>
        </div>

        <!-- My Appointments -->
        <div class="card">
            <div class="card-header">
                <h2>My Appointments</h2>
            </div>
            <div style="overflow-x: auto;">
                <table>
                    <thead>
                        <tr>
                            <th>Date</th>
                            <th>Time</th>
                            <th>Doctor</th>
                            <th>Reason</th>
                            <th>Status</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody id="appointmentsTable">
                        <tr><td colspan="6" class="text-center">Loading...</td></tr>
                    </tbody>
                </table>
            </div>
        </div>

        <!-- My Prescriptions -->
        <div class="card">
            <div class="card-header">
                <h2>My Prescriptions</h2>
            </div>
            <div id="prescriptionsList">Loading...</div>
        </div>
    </div>

    <script>
        const API_BASE = '""" + API_BASE + """';
        const token = localStorage.getItem('token');
        
        if (!token) {
            window.location.href = 'login.html';
        }
        
        const headers = {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
        };
        
        document.getElementById('userName').textContent = `Welcome, ${localStorage.getItem('userName')}!`;
        
        function showAlert(message, type) {
            const alertBox = document.getElementById('alertBox');
            alertBox.className = `alert alert-${type} show`;
            alertBox.textContent = message;
            window.scrollTo(0, 0);
            setTimeout(() => alertBox.classList.remove('show'), 5000);
        }
        
        function logout() {
            localStorage.clear();
            window.location.href = 'index.html';
        }
        
        async function loadProfile() {
            try {
                const response = await fetch(`${API_BASE}/patients/me`, { headers });
                if (response.ok) {
                    const patient = await response.json();
                    document.getElementById('profileContent').innerHTML = `
                        <p><strong>Name:</strong> ${patient.name}</p>
                        <p><strong>Email:</strong> ${patient.email}</p>
                        <p><strong>Phone:</strong> ${patient.phone}</p>
                        <p><strong>Date of Birth:</strong> ${patient.dateOfBirth}</p>
                        <p><strong>Gender:</strong> ${patient.gender}</p>
                        <p><strong>Blood Group:</strong> ${patient.bloodGroup || 'N/A'}</p>
                        <p><strong>Address:</strong> ${patient.address}</p>
                    `;
                }
            } catch (error) {
                console.error('Error loading profile:', error);
            }
        }
        
        async function loadDoctors() {
            try {
                const response = await fetch(`${API_BASE}/doctors`, { headers });
                if (response.ok) {
                    const doctors = await response.json();
                    const grid = document.getElementById('doctorsGrid');
                    const select = document.getElementById('doctorId');
                    
                    if (doctors.length === 0) {
                        grid.innerHTML = '<p>No doctors available at the moment.</p>';
                        return;
                    }
                    
                    grid.innerHTML = doctors.map(doc => `
                        <div class="doctor-card">
                            <h3>${doc.name}</h3>
                            <p class="specialization">${doc.specialization}</p>
                            <p class="info">📧 ${doc.email}</p>
                            <p class="info">📞 ${doc.phone}</p>
                            <p class="info">🏥 ${doc.department}</p>
                            <p class="info">Experience: ${doc.experience} years</p>
                        </div>
                    `).join('');
                    
                    select.innerHTML = '<option value="">Choose a doctor...</option>' +
                        doctors.map(doc => `<option value="${doc.id}">${doc.name} - ${doc.specialization}</option>`).join('');
                }
            } catch (error) {
                console.error('Error loading doctors:', error);
            }
        }
        
        async function loadAppointments() {
            try {
                const response = await fetch(`${API_BASE}/appointments/my`, { headers });
                if (response.ok) {
                    const appointments = await response.json();
                    const tbody = document.getElementById('appointmentsTable');
                    
                    if (appointments.length === 0) {
                        tbody.innerHTML = '<tr><td colspan="6" class="text-center">No appointments found.</td></tr>';
                        return;
                    }
                    
                    tbody.innerHTML = appointments.map(apt => `
                        <tr>
                            <td>${apt.appointmentDate}</td>
                            <td>${apt.appointmentTime}</td>
                            <td>${apt.doctorName || 'N/A'}</td>
                            <td>${apt.reason}</td>
                            <td><span class="badge">${apt.status}</span></td>
                            <td>
                                ${apt.status === 'SCHEDULED' ? 
                                    `<button onclick="cancelAppointment(${apt.id})" class="btn btn-danger btn-sm">Cancel</button>` : 
                                    '-'}
                            </td>
                        </tr>
                    `).join('');
                }
            } catch (error) {
                console.error('Error loading appointments:', error);
            }
        }
        
        async function loadPrescriptions() {
            try {
                const response = await fetch(`${API_BASE}/prescriptions/my`, { headers });
                if (response.ok) {
                    const prescriptions = await response.json();
                    const container = document.getElementById('prescriptionsList');
                    
                    if (prescriptions.length === 0) {
                        container.innerHTML = '<p>No prescriptions found.</p>';
                        return;
                    }
                    
                    container.innerHTML = prescriptions.map(pres => `
                        <div class="card" style="margin-bottom: 15px; padding: 15px;">
                            <h4>Prescription #${pres.id}</h4>
                            <p><strong>Doctor:</strong> ${pres.doctorName || 'N/A'}</p>
                            <p><strong>Date:</strong> ${pres.prescriptionDate}</p>
                            <p><strong>Diagnosis:</strong> ${pres.diagnosis}</p>
                            <p><strong>Notes:</strong> ${pres.notes || 'None'}</p>
                            <div>
                                <strong>Medicines:</strong>
                                <ul>
                                    ${pres.medicines ? pres.medicines.map(med => 
                                        `<li>${med.name} - ${med.dosage} (${med.frequency}) for ${med.duration}</li>`
                                    ).join('') : '<li>No medicines prescribed</li>'}
                                </ul>
                            </div>
                        </div>
                    `).join('');
                }
            } catch (error) {
                console.error('Error loading prescriptions:', error);
            }
        }
        
        document.getElementById('bookAppointmentForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(e.target);
            const data = {
                doctorId: parseInt(formData.get('doctorId')),
                appointmentDate: formData.get('appointmentDate'),
                appointmentTime: formData.get('appointmentTime'),
                reason: formData.get('reason')
            };
            
            try {
                const response = await fetch(`${API_BASE}/appointments`, {
                    method: 'POST',
                    headers,
                    body: JSON.stringify(data)
                });
                
                if (response.ok) {
                    showAlert('Appointment booked successfully!', 'success');
                    e.target.reset();
                    loadAppointments();
                } else {
                    const error = await response.json();
                    showAlert(error.message || 'Failed to book appointment.', 'danger');
                }
            } catch (error) {
                console.error('Error:', error);
                showAlert('Network error. Please try again.', 'danger');
            }
        });
        
        async function cancelAppointment(id) {
            if (!confirm('Are you sure you want to cancel this appointment?')) return;
            
            try {
                const response = await fetch(`${API_BASE}/appointments/${id}`, {
                    method: 'DELETE',
                    headers
                });
                
                if (response.ok) {
                    showAlert('Appointment cancelled successfully!', 'success');
                    loadAppointments();
                } else {
                    showAlert('Failed to cancel appointment.', 'danger');
                }
            } catch (error) {
                console.error('Error:', error);
                showAlert('Network error. Please try again.', 'danger');
            }
        }
        
        // Set minimum date to today
        document.getElementById('appointmentDate').min = new Date().toISOString().split('T')[0];
        
        // Load all data
        loadProfile();
        loadDoctors();
        loadAppointments();
        loadPrescriptions();
    </script>
</body>
</html>
"""

# ============================================================================
# DOCTOR-DASHBOARD.HTML
# ============================================================================
doctor_dashboard_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Doctor Dashboard - Healthcare Management System</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <div class="header-content">
            <div class="logo">Healthcare System - Doctor Portal</div>
            <div class="flex align-center gap-10">
                <span id="userName">Welcome!</span>
                <button onclick="logout()" class="btn btn-danger btn-sm">Logout</button>
            </div>
        </div>
    </header>

    <div class="container">
        <div id="alertBox" class="alert"></div>

        <!-- My Appointments -->
        <div class="card">
            <div class="card-header">
                <h2>My Appointments</h2>
            </div>
            <div style="overflow-x: auto;">
                <table>
                    <thead>
                        <tr>
                            <th>Date</th>
                            <th>Time</th>
                            <th>Patient</th>
                            <th>Reason</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody id="appointmentsTable">
                        <tr><td colspan="5" class="text-center">Loading...</td></tr>
                    </tbody>
                </table>
            </div>
        </div>

        <!-- Update Appointment Status -->
        <div class="card">
            <div class="card-header">
                <h2>Update Appointment Status</h2>
            </div>
            <form id="updateStatusForm">
                <div class="form-group">
                    <label for="appointmentId">Select Appointment</label>
                    <select id="appointmentId" name="appointmentId" required>
                        <option value="">Choose an appointment...</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="status">New Status</label>
                    <select id="status" name="status" required>
                        <option value="">Select status...</option>
                        <option value="CONFIRMED">Confirmed</option>
                        <option value="COMPLETED">Completed</option>
                        <option value="CANCELLED">Cancelled</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="notes">Notes (Optional)</label>
                    <textarea id="notes" name="notes"></textarea>
                </div>
                <button type="submit" class="btn btn-primary">Update Status</button>
            </form>
        </div>

        <!-- Write Prescription -->
        <div class="card">
            <div class="card-header">
                <h2>Write Prescription</h2>
            </div>
            <form id="prescriptionForm">
                <div class="form-group">
                    <label for="prescriptionAppointmentId">Select Appointment</label>
                    <select id="prescriptionAppointmentId" name="appointmentId" required>
                        <option value="">Choose an appointment...</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="diagnosis">Diagnosis</label>
                    <textarea id="diagnosis" name="diagnosis" required></textarea>
                </div>
                <div class="form-group">
                    <label for="prescriptionNotes">Notes</label>
                    <textarea id="prescriptionNotes" name="notes"></textarea>
                </div>
                
                <div class="medicine-items">
                    <h4>Medicines</h4>
                    <div id="medicinesList">
                        <div class="medicine-item">
                            <div class="form-group">
                                <label>Medicine Name</label>
                                <input type="text" class="medicine-name" required>
                            </div>
                            <div class="form-group">
                                <label>Dosage</label>
                                <input type="text" class="medicine-dosage" placeholder="e.g., 500mg" required>
                            </div>
                            <div class="form-group">
                                <label>Frequency</label>
                                <input type="text" class="medicine-frequency" placeholder="e.g., Twice daily" required>
                            </div>
                            <div class="form-group">
                                <label>Duration</label>
                                <input type="text" class="medicine-duration" placeholder="e.g., 7 days" required>
                            </div>
                            <div class="form-group">
                                <label>&nbsp;</label>
                                <button type="button" onclick="removeMedicine(this)" class="btn btn-danger btn-sm">Remove</button>
                            </div>
                        </div>
                    </div>
                    <button type="button" onclick="addMedicine()" class="btn btn-secondary btn-sm mt-20">Add Medicine</button>
                </div>
                
                <button type="submit" class="btn btn-success mt-20">Submit Prescription</button>
            </form>
        </div>
    </div>

    <script>
        const API_BASE = '""" + API_BASE + """';
        const token = localStorage.getItem('token');
        
        if (!token) {
            window.location.href = 'login.html';
        }
        
        const headers = {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
        };
        
        document.getElementById('userName').textContent = `Welcome, Dr. ${localStorage.getItem('userName')}!`;
        
        function showAlert(message, type) {
            const alertBox = document.getElementById('alertBox');
            alertBox.className = `alert alert-${type} show`;
            alertBox.textContent = message;
            window.scrollTo(0, 0);
            setTimeout(() => alertBox.classList.remove('show'), 5000);
        }
        
        function logout() {
            localStorage.clear();
            window.location.href = 'index.html';
        }
        
        async function loadAppointments() {
            try {
                const response = await fetch(`${API_BASE}/appointments/doctor/me`, { headers });
                if (response.ok) {
                    const appointments = await response.json();
                    const tbody = document.getElementById('appointmentsTable');
                    const selectStatus = document.getElementById('appointmentId');
                    const selectPrescription = document.getElementById('prescriptionAppointmentId');
                    
                    if (appointments.length === 0) {
                        tbody.innerHTML = '<tr><td colspan="5" class="text-center">No appointments found.</td></tr>';
                        return;
                    }
                    
                    tbody.innerHTML = appointments.map(apt => `
                        <tr>
                            <td>${apt.appointmentDate}</td>
                            <td>${apt.appointmentTime}</td>
                            <td>${apt.patientName || 'N/A'}</td>
                            <td>${apt.reason}</td>
                            <td><span class="badge">${apt.status}</span></td>
                        </tr>
                    `).join('');
                    
                    const options = appointments.map(apt => 
                        `<option value="${apt.id}">${apt.appointmentDate} - ${apt.patientName} (${apt.status})</option>`
                    ).join('');
                    
                    selectStatus.innerHTML = '<option value="">Choose an appointment...</option>' + options;
                    selectPrescription.innerHTML = '<option value="">Choose an appointment...</option>' + options;
                }
            } catch (error) {
                console.error('Error loading appointments:', error);
            }
        }
        
        document.getElementById('updateStatusForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(e.target);
            const appointmentId = formData.get('appointmentId');
            const data = {
                status: formData.get('status'),
                notes: formData.get('notes')
            };
            
            try {
                const response = await fetch(`${API_BASE}/appointments/${appointmentId}/status`, {
                    method: 'PUT',
                    headers,
                    body: JSON.stringify(data)
                });
                
                if (response.ok) {
                    showAlert('Appointment status updated successfully!', 'success');
                    e.target.reset();
                    loadAppointments();
                } else {
                    const error = await response.json();
                    showAlert(error.message || 'Failed to update status.', 'danger');
                }
            } catch (error) {
                console.error('Error:', error);
                showAlert('Network error. Please try again.', 'danger');
            }
        });
        
        function addMedicine() {
            const medicinesList = document.getElementById('medicinesList');
            const newMedicine = document.createElement('div');
            newMedicine.className = 'medicine-item';
            newMedicine.innerHTML = `
                <div class="form-group">
                    <label>Medicine Name</label>
                    <input type="text" class="medicine-name" required>
                </div>
                <div class="form-group">
                    <label>Dosage</label>
                    <input type="text" class="medicine-dosage" placeholder="e.g., 500mg" required>
                </div>
                <div class="form-group">
                    <label>Frequency</label>
                    <input type="text" class="medicine-frequency" placeholder="e.g., Twice daily" required>
                </div>
                <div class="form-group">
                    <label>Duration</label>
                    <input type="text" class="medicine-duration" placeholder="e.g., 7 days" required>
                </div>
                <div class="form-group">
                    <label>&nbsp;</label>
                    <button type="button" onclick="removeMedicine(this)" class="btn btn-danger btn-sm">Remove</button>
                </div>
            `;
            medicinesList.appendChild(newMedicine);
        }
        
        function removeMedicine(button) {
            const medicinesList = document.getElementById('medicinesList');
            if (medicinesList.children.length > 1) {
                button.closest('.medicine-item').remove();
            } else {
                showAlert('At least one medicine is required.', 'warning');
            }
        }
        
        document.getElementById('prescriptionForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(e.target);
            
            const medicines = [];
            document.querySelectorAll('.medicine-item').forEach(item => {
                medicines.push({
                    name: item.querySelector('.medicine-name').value,
                    dosage: item.querySelector('.medicine-dosage').value,
                    frequency: item.querySelector('.medicine-frequency').value,
                    duration: item.querySelector('.medicine-duration').value
                });
            });
            
            const data = {
                appointmentId: parseInt(formData.get('appointmentId')),
                diagnosis: formData.get('diagnosis'),
                notes: formData.get('notes'),
                medicines: medicines
            };
            
            try {
                const response = await fetch(`${API_BASE}/prescriptions`, {
                    method: 'POST',
                    headers,
                    body: JSON.stringify(data)
                });
                
                if (response.ok) {
                    showAlert('Prescription created successfully!', 'success');
                    e.target.reset();
                    document.getElementById('medicinesList').innerHTML = `
                        <div class="medicine-item">
                            <div class="form-group">
                                <label>Medicine Name</label>
                                <input type="text" class="medicine-name" required>
                            </div>
                            <div class="form-group">
                                <label>Dosage</label>
                                <input type="text" class="medicine-dosage" placeholder="e.g., 500mg" required>
                            </div>
                            <div class="form-group">
                                <label>Frequency</label>
                                <input type="text" class="medicine-frequency" placeholder="e.g., Twice daily" required>
                            </div>
                            <div class="form-group">
                                <label>Duration</label>
                                <input type="text" class="medicine-duration" placeholder="e.g., 7 days" required>
                            </div>
                            <div class="form-group">
                                <label>&nbsp;</label>
                                <button type="button" onclick="removeMedicine(this)" class="btn btn-danger btn-sm">Remove</button>
                            </div>
                        </div>
                    `;
                } else {
                    const error = await response.json();
                    showAlert(error.message || 'Failed to create prescription.', 'danger');
                }
            } catch (error) {
                console.error('Error:', error);
                showAlert('Network error. Please try again.', 'danger');
            }
        });
        
        loadAppointments();
    </script>
</body>
</html>
"""

# ============================================================================
# ADMIN-DASHBOARD.HTML
# ============================================================================
admin_dashboard_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Dashboard - Healthcare Management System</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <div class="header-content">
            <div class="logo">Healthcare System - Admin Portal</div>
            <div class="flex align-center gap-10">
                <span id="userName">Welcome Admin!</span>
                <button onclick="logout()" class="btn btn-danger btn-sm">Logout</button>
            </div>
        </div>
    </header>

    <div class="container">
        <div id="alertBox" class="alert"></div>

        <!-- Statistics -->
        <div class="stats-grid">
            <div class="stat-card">
                <h3 id="totalPatients">0</h3>
                <p>Total Patients</p>
            </div>
            <div class="stat-card" style="background: linear-gradient(135deg, var(--success), #1e7e34);">
                <h3 id="totalDoctors">0</h3>
                <p>Total Doctors</p>
            </div>
            <div class="stat-card" style="background: linear-gradient(135deg, var(--warning), #d39e00);">
                <h3 id="totalAppointments">0</h3>
                <p>Total Appointments</p>
            </div>
        </div>

        <!-- Add Doctor -->
        <div class="card">
            <div class="card-header">
                <h2>Add New Doctor</h2>
            </div>
            <form id="addDoctorForm">
                <div class="card-grid">
                    <div class="form-group">
                        <label for="name">Full Name *</label>
                        <input type="text" id="name" name="name" required>
                    </div>
                    <div class="form-group">
                        <label for="email">Email *</label>
                        <input type="email" id="email" name="email" required>
                    </div>
                    <div class="form-group">
                        <label for="password">Password *</label>
                        <input type="password" id="password" name="password" required minlength="6">
                    </div>
                    <div class="form-group">
                        <label for="phone">Phone *</label>
                        <input type="tel" id="phone" name="phone" required>
                    </div>
                    <div class="form-group">
                        <label for="specialization">Specialization *</label>
                        <input type="text" id="specialization" name="specialization" required>
                    </div>
                    <div class="form-group">
                        <label for="department">Department *</label>
                        <input type="text" id="department" name="department" required>
                    </div>
                    <div class="form-group">
                        <label for="qualification">Qualification *</label>
                        <input type="text" id="qualification" name="qualification" required>
                    </div>
                    <div class="form-group">
                        <label for="experience">Experience (years) *</label>
                        <input type="number" id="experience" name="experience" required min="0">
                    </div>
                </div>
                <button type="submit" class="btn btn-success">Add Doctor</button>
            </form>
        </div>

        <!-- All Doctors -->
        <div class="card">
            <div class="card-header">
                <h2>All Doctors</h2>
            </div>
            <div style="overflow-x: auto;">
                <table>
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Name</th>
                            <th>Email</th>
                            <th>Phone</th>
                            <th>Specialization</th>
                            <th>Department</th>
                            <th>Experience</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody id="doctorsTable">
                        <tr><td colspan="8" class="text-center">Loading...</td></tr>
                    </tbody>
                </table>
            </div>
        </div>

        <!-- All Appointments -->
        <div class="card">
            <div class="card-header">
                <h2>All Appointments</h2>
            </div>
            <div style="overflow-x: auto;">
                <table>
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Patient</th>
                            <th>Doctor</th>
                            <th>Date</th>
                            <th>Time</th>
                            <th>Status</th>
                            <th>Reason</th>
                        </tr>
                    </thead>
                    <tbody id="appointmentsTable">
                        <tr><td colspan="7" class="text-center">Loading...</td></tr>
                    </tbody>
                </table>
            </div>
        </div>

        <!-- All Patients -->
        <div class="card">
            <div class="card-header">
                <h2>All Patients</h2>
            </div>
            <div style="overflow-x: auto;">
                <table>
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Name</th>
                            <th>Email</th>
                            <th>Phone</th>
                            <th>Gender</th>
                            <th>Blood Group</th>
                            <th>Date of Birth</th>
                        </tr>
                    </thead>
                    <tbody id="patientsTable">
                        <tr><td colspan="7" class="text-center">Loading...</td></tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    <script>
        const API_BASE = '""" + API_BASE + """';
        const token = localStorage.getItem('token');
        
        if (!token) {
            window.location.href = 'login.html';
        }
        
        const headers = {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
        };
        
        function showAlert(message, type) {
            const alertBox = document.getElementById('alertBox');
            alertBox.className = `alert alert-${type} show`;
            alertBox.textContent = message;
            window.scrollTo(0, 0);
            setTimeout(() => alertBox.classList.remove('show'), 5000);
        }
        
        function logout() {
            localStorage.clear();
            window.location.href = 'index.html';
        }
        
        async function loadDoctors() {
            try {
                const response = await fetch(`${API_BASE}/doctors`, { headers });
                if (response.ok) {
                    const doctors = await response.json();
                    document.getElementById('totalDoctors').textContent = doctors.length;
                    const tbody = document.getElementById('doctorsTable');
                    
                    if (doctors.length === 0) {
                        tbody.innerHTML = '<tr><td colspan="8" class="text-center">No doctors found.</td></tr>';
                        return;
                    }
                    
                    tbody.innerHTML = doctors.map(doc => `
                        <tr>
                            <td>${doc.id}</td>
                            <td>${doc.name}</td>
                            <td>${doc.email}</td>
                            <td>${doc.phone}</td>
                            <td>${doc.specialization}</td>
                            <td>${doc.department}</td>
                            <td>${doc.experience} years</td>
                            <td>
                                <button onclick="deleteDoctor(${doc.id})" class="btn btn-danger btn-sm">Delete</button>
                            </td>
                        </tr>
                    `).join('');
                }
            } catch (error) {
                console.error('Error loading doctors:', error);
            }
        }
        
        async function loadPatients() {
            try {
                const response = await fetch(`${API_BASE}/patients`, { headers });
                if (response.ok) {
                    const patients = await response.json();
                    document.getElementById('totalPatients').textContent = patients.length;
                    const tbody = document.getElementById('patientsTable');
                    
                    if (patients.length === 0) {
                        tbody.innerHTML = '<tr><td colspan="7" class="text-center">No patients found.</td></tr>';
                        return;
                    }
                    
                    tbody.innerHTML = patients.map(pat => `
                        <tr>
                            <td>${pat.id}</td>
                            <td>${pat.name}</td>
                            <td>${pat.email}</td>
                            <td>${pat.phone}</td>
                            <td>${pat.gender}</td>
                            <td>${pat.bloodGroup || 'N/A'}</td>
                            <td>${pat.dateOfBirth}</td>
                        </tr>
                    `).join('');
                }
            } catch (error) {
                console.error('Error loading patients:', error);
            }
        }
        
        async function loadAppointments() {
            try {
                const response = await fetch(`${API_BASE}/appointments`, { headers });
                if (response.ok) {
                    const appointments = await response.json();
                    document.getElementById('totalAppointments').textContent = appointments.length;
                    const tbody = document.getElementById('appointmentsTable');
                    
                    if (appointments.length === 0) {
                        tbody.innerHTML = '<tr><td colspan="7" class="text-center">No appointments found.</td></tr>';
                        return;
                    }
                    
                    tbody.innerHTML = appointments.map(apt => `
                        <tr>
                            <td>${apt.id}</td>
                            <td>${apt.patientName || 'N/A'}</td>
                            <td>${apt.doctorName || 'N/A'}</td>
                            <td>${apt.appointmentDate}</td>
                            <td>${apt.appointmentTime}</td>
                            <td><span class="badge">${apt.status}</span></td>
                            <td>${apt.reason}</td>
                        </tr>
                    `).join('');
                }
            } catch (error) {
                console.error('Error loading appointments:', error);
            }
        }
        
        document.getElementById('addDoctorForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(e.target);
            const data = {
                name: formData.get('name'),
                email: formData.get('email'),
                password: formData.get('password'),
                phone: formData.get('phone'),
                specialization: formData.get('specialization'),
                department: formData.get('department'),
                qualification: formData.get('qualification'),
                experience: parseInt(formData.get('experience'))
            };
            
            try {
                const response = await fetch(`${API_BASE}/doctors`, {
                    method: 'POST',
                    headers,
                    body: JSON.stringify(data)
                });
                
                if (response.ok) {
                    showAlert('Doctor added successfully!', 'success');
                    e.target.reset();
                    loadDoctors();
                } else {
                    const error = await response.json();
                    showAlert(error.message || 'Failed to add doctor.', 'danger');
                }
            } catch (error) {
                console.error('Error:', error);
                showAlert('Network error. Please try again.', 'danger');
            }
        });
        
        async function deleteDoctor(id) {
            if (!confirm('Are you sure you want to delete this doctor?')) return;
            
            try {
                const response = await fetch(`${API_BASE}/doctors/${id}`, {
                    method: 'DELETE',
                    headers
                });
                
                if (response.ok) {
                    showAlert('Doctor deleted successfully!', 'success');
                    loadDoctors();
                } else {
                    showAlert('Failed to delete doctor.', 'danger');
                }
            } catch (error) {
                console.error('Error:', error);
                showAlert('Network error. Please try again.', 'danger');
            }
        }
        
        // Load all data
        loadDoctors();
        loadPatients();
        loadAppointments();
    </script>
</body>
</html>
"""

# ============================================================================
# WRITE FILES
# ============================================================================
def write_file(filename, content):
    filepath = os.path.join(FRONTEND_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ Created: {filepath}")

print("=" * 70)
print("HEALTHCARE MANAGEMENT SYSTEM - FRONTEND GENERATOR")
print("=" * 70)
print(f"\nGenerating frontend files in: {FRONTEND_DIR}\n")

# Write CSS
write_file('styles.css', css_content)

# Write HTML files
write_file('index.html', index_html)
write_file('register.html', register_html)
write_file('login.html', login_html)
write_file('patient-dashboard.html', patient_dashboard_html)
write_file('doctor-dashboard.html', doctor_dashboard_html)
write_file('admin-dashboard.html', admin_dashboard_html)

print("\n" + "=" * 70)
print("✓ ALL FRONTEND FILES GENERATED SUCCESSFULLY!")
print("=" * 70)
print("\nGenerated files:")
print("  1. styles.css - Modern healthcare-themed styles")
print("  2. index.html - Landing page")
print("  3. register.html - Patient registration")
print("  4. login.html - User login")
print("  5. patient-dashboard.html - Patient dashboard")
print("  6. doctor-dashboard.html - Doctor dashboard")
print("  7. admin-dashboard.html - Admin dashboard")
print("\nTo use the frontend:")
print("  1. Ensure your backend is running on http://localhost:8080")
print(f"  2. Open {os.path.join(FRONTEND_DIR, 'index.html')} in your browser")
print("  3. Or serve the frontend folder with any web server")
print("\n" + "=" * 70)
