# Morse Code 2

A simple web-based Morse Code project that converts or demonstrates Morse code interactions through a Python backend and HTML frontend.  
This repository includes containerization and CI/CD configuration for easy deployment.

## 🚀 Features

- Web interface using HTML templates
- Python backend for processing logic
- Docker support for containerized deployment
- Jenkins pipeline configuration included
- Lightweight and easy to extend

## 📁 Project Structure

<img width="587" height="179" alt="image" src="https://github.com/user-attachments/assets/42dab2b1-8832-4757-a37c-63b8f8ff29f0" />



## 🛠️ Tech Stack

- **Frontend:** HTML (templates)
- **Backend:** Python
- **Containerization:** Docker
- **CI/CD:** Jenkins

## 📌 Prerequisites

- Python 3.7+
- pip
- (Optional) Docker installed

## 📦 Installation & Run

1️⃣ Clone repository  

git clone https://github.com/Sanjeevan-17/morse-code-2.git

cd morse-code-2


2️⃣ Create virtual environment

python -m venv venv

source venv/bin/activate # Linux/Mac

venv\Scripts\activate         # Windows

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Run application

python app.py

5️⃣ Open browser

http://localhost:5000

🐳 Run with Docker

Build image:

docker build -t morse-app .

Run container:

docker run -p 5000:5000 morse-app

🤝 Contributing
1. Fork the repo

2. Create a branch (git checkout -b feature-name)

3. Commit changes

4. Push branch

5. Open Pull Request
