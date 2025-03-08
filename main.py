import pandas as pd
import requests  # Import the requests library
import json
import os

current_dir = os.getcwd()

csv_file_path = os.path.join(current_dir, "customers-100.csv")

# Determine if running inside Docker
if os.path.exists("/app"):
    csv_output_path = "/app/output/transformed_data.csv"  # Docker path
else:
    csv_output_path = os.path.join(current_dir, "Output/transformed_data.csv") # Local path


# 1. Load CSV to DataFrame
data = pd.read_csv(csv_file_path)

# 2. Convert DataFrame to JSON (list of records)
json_data = data.to_dict(orient='records')

# 3. Define Headers for API-KEY authentication
headers = {'Content-Type': 'application/json'}

# 4. Vercel URL for the external API, this was mine but it depends on your vercel deployment URL
url = "https://flask-etl-vincentm-techs-projects.vercel.app/transform_data"


# 5. Make the API call
try:
    response = requests.post(url, headers=headers, json=json_data)

    # Check for successful request (status code 200)
    if response.status_code == 200:
        transformed_data = response.json()  # Parse the JSON response
        print("API call successful!")

        #8. Convert the JSON data back to a Pandas DataFrame
        transformed_df = pd.DataFrame(transformed_data)

        #9. Save the DataFrame to a local CSV file
        transformed_df.to_csv(csv_output_path, index=False)  # index=False avoids saving the DataFrame index to the CSV
        #transformed_df.to_csv("/app/output/transformed_data.csv", index=False)

        print("Transformed data saved to transformed_data.csv")


    else:
        print(f"API call failed with status code: {response.status_code}")
        print(response.text) # Print the error message from the API

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
