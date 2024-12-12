# Remove existing virtual environment (if necessary)
Remove-Item -Recurse -Force .\venv

# Create a new virtual environment
python -m venv .\venv

# Activate the virtual environment
.\venv\Scripts\Activate

# Install Flask
pip install flask

Write-Host "Virtual environment setup complete. Flask installed."
