"""
Healthcare Application - Source File Generator
Generates all Java source files in the correct directory structure
"""

import os

# File content templates
files = {
    # Main Application
    "src/main/java/com/healthcare/app/HealthcareApplication.java": """package com.healthcare.app;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class HealthcareApplication {

    public static void main(String[] args) {
        SpringApplication.run(HealthcareApplication.class, args);
    }

}
""",

    # Application Properties
    "src/main/resources/application.properties": """# Server Configuration
server.port=8080
spring.application.name=healthcare-app

# MySQL Database Configuration
spring.datasource.url=jdbc:mysql://localhost:3306/healthcare_db?createDatabaseIfNotExist=true&useSSL=false&serverTimezone=UTC
spring.datasource.username=root
spring.datasource.password=root
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver

# JPA/Hibernate Configuration
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.MySQL8Dialect
spring.jpa.properties.hibernate.format_sql=true

# JWT Configuration
jwt.secret=your-secret-key-change-this-in-production-minimum-256-bits-required-for-hs256-algorithm
jwt.expiration=86400000

# Logging Configuration
logging.level.com.healthcare.app=INFO
logging.level.org.springframework.security=INFO
logging.level.org.hibernate.SQL=DEBUG
logging.level.org.hibernate.type.descriptor.sql.BasicBinder=TRACE

# Swagger Configuration
springdoc.api-docs.path=/api-docs
springdoc.swagger-ui.path=/swagger-ui.html
springdoc.swagger-ui.operationsSorter=method
"""
}

# Create all files
for filepath, content in files.items():
    # Create directory if it doesn't exist
    directory = os.path.dirname(filepath)
    if directory:
        os.makedirs(directory, exist_ok=True)
    
    # Write file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created: {filepath}")

print("\n✓ Basic files created successfully!")
print("\nRun this script again after setup.ps1 completes to generate all remaining files.")
