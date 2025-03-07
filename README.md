# Flask ETL API

## Overview
This project demonstrates an **Extract, Transform, Load (ETL) process** using Flask and Serverless Functions on Vercel. The application reads a CSV file from a local device, sends the data to a Flask API for transformation, and saves the transformed data back to a local file.

## How It Works
This project utilizes **WSGI with Flask** to handle HTTP requests and process data using **Serverless Functions on Vercel**.

### **Usage Workflow**
1. **Extract**: Python script loads a CSV file from the local device.
2. **Transform**: The script makes an API call to process the data using the deployed Flask application.
3. **Load**: The transformed CSV is downloaded and saved locally.

---

## **Deployment Workflow**

### 1️⃣ Create a Project Directory & Clone the Repository
#### **PowerShell**:
```powershell
mkdir flask-data-api
```

#### **Bash**:
```bash
mkdir flask-data-api
cd flask-data-api
git clone <your-github-repo-url>
```

### 2️⃣ Activate Virtual Environment & Install Dependencies
#### **Windows**:
```powershell
cd flask-data-api
cd api
python -m venv env
./env/Scripts/Activate
pip install -r ../requirements.txt
```

#### **Mac/Linux**:
```bash
cd flask-data-api
cd api
python -m venv env
source env/bin/activate
pip install -r ../requirements.txt
```

### 3️⃣ Upload the Code to GitHub
```bash
git remote set-url origin <your-github-repo-url>
git add .
git commit -m "initial commit"
git push -u origin main
```

---

### 4️⃣ Create a Vercel Account
1. Go to [Vercel's website](https://vercel.com/) and click **"Sign Up"**.
2. Sign up using **GitHub**, **GitLab**, or **Bitbucket**.
3. Once signed in, click **"New Project"** to create a deployment.

---

## **Next Steps & Enhancements**
- Implement **API authentication** to secure endpoints.
- Store transformed data in a **database** instead of CSV.
- Add **error handling** to improve reliability.
- Use **Docker** for easier deployment.

---

### **License**
This project is open-source and available under the MIT License.

