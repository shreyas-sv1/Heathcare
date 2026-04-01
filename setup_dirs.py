import os

# Define directory structure
dirs = [
    "src/main/java/com/healthcare/app/controller",
    "src/main/java/com/healthcare/app/service/impl",
    "src/main/java/com/healthcare/app/repository",
    "src/main/java/com/healthcare/app/entity",
    "src/main/java/com/healthcare/app/dto/request",
    "src/main/java/com/healthcare/app/dto/response",
    "src/main/java/com/healthcare/app/security",
    "src/main/java/com/healthcare/app/exception",
    "src/main/java/com/healthcare/app/enums",
    "src/main/java/com/healthcare/app/config",
    "src/main/resources",
    "src/test/java/com/healthcare/app/service",
    "gradle/wrapper",
    "frontend",
    "database"
]

# Create directories
for dir_path in dirs:
    os.makedirs(dir_path, exist_ok=True)
    print(f"Created: {dir_path}")

print("\nDirectory structure created successfully!")
