import os
import pandas as pd

# Step 1: Create a directory
dir_name = 'my_data_folder'
os.makedirs(dir_name, exist_ok=True)

# Step 2: Create a DataFrame with a single row
data = {
    'Name': 'Sharath',
    'Age': 24,
    'Course': 'M.Tech',
    'Institute': 'IIIT Allahabad'
}
df = pd.DataFrame([data])

# Step 2.1: Add another row using df.loc
new_index = len(df)  # get next index (here 1)
df.loc[new_index] = ['ANUJ', 25, 'M.Tech', 'IIIT Allahabad']

# Step 2.1: Add another row using df.loc
new_index = len(df)  # get next index (here 1)
df.loc[new_index] = ['SAMAR', 25, 'M.Tech', 'IIIT Allahabad']

# Step 3: Save DataFrame to CSV file inside the directory
file_path = os.path.join(dir_name, 'student_info.csv')
df.to_csv(file_path, index=False)

print(f"Data saved to {file_path}")
