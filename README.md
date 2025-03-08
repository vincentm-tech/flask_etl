# Flask ETL API

## Overview
This project demonstrates an Extract, Transform, Load (ETL) process using Flask and Serverless Functions on Vercel. The application reads a CSV file from a local device, sends the data to a Flask API for transformation, and saves the transformed data back to a local file.

## How It Works
This project utilizes WSGI with Flask to handle HTTP requests and process data. It can be run **locally** or inside a **Docker container**.

### Usage Workflow
1. **Extract**: Python script loads a CSV file from the local device.
2. **Transform**: The script makes an API call to process the data using the deployed Flask application.
3. **Load**: The transformed CSV is downloaded and saved locally.

## Deployment Workflow
### 1️⃣ Create a Project Directory & Clone the Repository
**PowerShell:**
```powershell
mkdir flask-data-api
```
**Bash:**
```bash
mkdir flask-data-api
cd flask-data-api
git clone <your-github-repo-url>
```

### 2️⃣ Activate Virtual Environment & Install Dependencies
#### Windows:
```powershell
cd flask-data-api
cd api
python -m venv env
./env/Scripts/Activate
pip install -r ../requirements.txt
```
#### Mac/Linux:
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

### 4️⃣ Create a Vercel Account
1. Go to Vercel's website and click "Sign Up".
2. Sign up using GitHub, GitLab, or Bitbucket.
3. Once signed in, click "New Project" to create a deployment.

## Running the Application
### 🏃 Running Locally (Without Docker)
```bash
python main.py
```

### 🐳 Running with Docker
If you prefer to run the Flask ETL process inside a **Docker container**, follow these steps:

#### 1️⃣ Build the Docker Image

```sh
docker build -t flask-etl .
```

#### 2️⃣ Run the Docker Container

```sh
docker run -p 5000:5000 -v "<Output Path>:/app/output" flask-etl
```

This will:

- Start the Flask API on **port 5000**

- Mount the **output folder** so the transformed CSV files can be saved to the local system.

---

## Vercel Deployment

Currently, the **Dockerized version of this project does not use Vercel**.

Vercel is optimized for **serverless functions**, while Docker runs Flask as a long-running service.

If you want to deploy to Vercel, you would need to:

- Modify Flask to work as a serverless function.

- Remove the need for a continuously running process.

---

## Next Steps & Enhancements

✅ Implement API authentication to secure endpoints.

✅ Store transformed data in a database instead of CSV.

✅ Add error handling to improve reliability.


---

## License

This project is open-source and available under the MIT License.


