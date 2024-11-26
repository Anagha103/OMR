import pandas as pd

# Step 1: Load the CSV file
input_file = "omr_sheet.csv"
df = pd.read_csv(input_file)

# Step 2: Initialize columns for evaluation
df['Right'] = 0
df['Wrong'] = 0
df['Unattended'] = 0

# Step 3: Evaluate each row
for index, row in df.iterrows():
    actual = row['Actual Answers']
    marked = row['Marked Answers']
    
    # Check for unattended answers
    if pd.isna(marked) or str(marked).strip() == "":
        df.at[index, 'Unattended'] = 1
    # Check for correct answers
    elif actual.strip().upper() == marked.strip().upper():
        df.at[index, 'Right'] = 1
    # Check for wrong answers
    else:
        df.at[index, 'Wrong'] = 1

# Step 4: Save the evaluated data to a new CSV file
output_file = "evaluated_omr_sheet.csv"
df.to_csv(output_file, index=False)

print(f"Evaluation complete. Results saved to '{output_file}'.")
