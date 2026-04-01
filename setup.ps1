# Healthcare App - Directory Setup Script
# Compatible with Windows PowerShell 5.1+

Write-Host "Creating Healthcare Application Directory Structure..." -ForegroundColor Green

$directories = @(
    "src\main\java\com\healthcare\app\controller",
    "src\main\java\com\healthcare\app\service\impl",
    "src\main\java\com\healthcare\app\repository",
    "src\main\java\com\healthcare\app\entity",
    "src\main\java\com\healthcare\app\dto\request",
    "src\main\java\com\healthcare\app\dto\response",
    "src\main\java\com\healthcare\app\security",
    "src\main\java\com\healthcare\app\exception",
    "src\main\java\com\healthcare\app\enums",
    "src\main\java\com\healthcare\app\config",
    "src\main\resources",
    "src\test\java\com\healthcare\app\service",
    "gradle\wrapper",
    "frontend\css",
    "frontend\js",
    "database"
)

foreach ($dir in $directories) {
    if (!(Test-Path $dir)) {
        New-Item -ItemType Directory -Force -Path $dir | Out-Null
        Write-Host "  Created: $dir" -ForegroundColor Gray
    } else {
        Write-Host "  Exists: $dir" -ForegroundColor Yellow
    }
}

Write-Host "`nDirectory structure created successfully!" -ForegroundColor Green
Write-Host "`nNext steps:" -ForegroundColor Cyan
Write-Host "  1. Update application.properties with your MySQL credentials"
Write-Host "  2. Run: .\gradlew.bat build"
Write-Host "  3. Run: .\gradlew.bat bootRun"
