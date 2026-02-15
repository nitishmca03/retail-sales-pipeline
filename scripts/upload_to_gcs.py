import os
import pandas as pd
from google.cloud import storage

# Tell Python where your secret key is
# This looks one folder up from 'scripts' to find the json file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../gcp-key.json"

def upload_data():
    # UPDATED: Using your specific bucket name
    bucket_name = 'student-data-pipeline-nitish' 
    
    # 1. Create a tiny sample dataset
    data = {
        'id': [1, 2, 3],
        'product': ['Laptop', 'Mouse', 'Keyboard'],
        'amount': [1200, 25, 75],
        'sale_date': ['2026-02-14', '2026-02-14', '2026-02-14']
    }
    df = pd.DataFrame(data)
    
    # 2. Save it locally as a CSV file first
    local_file = "sample_data.csv"
    df.to_csv(local_file, index=False)
    print(f"✅ Created local file: {local_file}")

    # 3. Upload to Google Cloud Storage
    try:
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        # This puts the file in a folder named 'landing' inside your bucket
        blob = bucket.blob("landing/sample_data.csv")
        blob.upload_from_filename(local_file)
        print(f"🚀 Success! File uploaded to bucket: {bucket_name}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    upload_data()