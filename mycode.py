import os
import pandas as pd

# Step 1: Create a directory
dir_name = 'my_data_folder'
os.makedirs(dir_name, exist_ok=True)  # Will not raise an error if it already exists

# Step 2: Create single-row DataFrame
data = {
    'Name': 'Sharath',
    'Age': 24,
    'Course': 'M.Tech',
    'Institute': 'IIIT Allahabad'
}
df = pd.DataFrame([data])

# Step 3: Save DataFrame to a CSV file inside the directory
file_path = os.path.join(dir_name, 'student_info.csv')
df.to_csv(file_path, index=False)

print(f"Data saved to {file_path}")
