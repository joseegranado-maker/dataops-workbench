param(
    [string]$ProjectRoot = (Get-Location).Path
)

Write-Host "Project root: $ProjectRoot"
Set-Location $ProjectRoot

if (-not (Test-Path ".venv")) {
    python -m venv .venv
}

& "$ProjectRoot\.venv\Scripts\Activate.ps1"
python -m pip install --upgrade pip

$requirements = Join-Path $ProjectRoot "requirements.txt"
if (Test-Path $requirements) {
    pip install -r $requirements
} else {
    pip install pandas numpy matplotlib seaborn ipykernel python-dotenv
}

$folders = @("data","notebooks","scripts","outputs","pbix","docs")
foreach ($folder in $folders) {
    New-Item -ItemType Directory -Force -Path (Join-Path $ProjectRoot $folder) | Out-Null
}

Write-Host "Environment ready."
