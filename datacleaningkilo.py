from google.colab import files
import pandas as pd
import re

def remove_special_characters(text):
    """Removes special characters from a string, keeping only letters, numbers, spaces, and hyphens."""
    return re.sub(r"[^a-zA-Z0-9\s-]", "", text)

def fill_empty_fields(df):
    """Fills empty fields in the DataFrame with 'Unknown'."""
    return df.fillna("Unknown")

# Step 1: Upload the CSV file
uploaded = files.upload()

# Assuming the file uploaded is the one you're working with
file_name = list(uploaded.keys())[0]

# Load CSV file into a DataFrame
df = pd.read_csv(file_name)

# Change column headings to use underscores and remove spaces
df.columns = df.columns.str.replace(' ', '_')

# Apply the function to the 'Job Title' column
df['Job_Title'] = df['Job_Title'].apply(remove_special_characters)

# Apply the function to the 'Description' column
df['Description'] = df['Description'].apply(remove_special_characters)

# Fill empty fields with 'Unknown'
#df = fill_empty_fields(df)

# Step 2: Remove duplicate rows
df.drop_duplicates(inplace=True)

# Step 3: Drop the "Employer Logo" column if it exists
if 'Employer_Logo' in df.columns:
    df = df.drop('Employer_Logo', axis=1)

# Step 4: Save cleaned data to a new CSV file
cleaned_file_name = 'cleaned_cyber_securityjobs.csv'
df.to_csv(cleaned_file_name, index=False)

print(f"\nCleaned data saved to {cleaned_file_name}")

# Download the cleaned file
files.download(cleaned_file_name)
