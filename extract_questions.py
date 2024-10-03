import pandas as pd
import numpy as np

# Load the questions from the csv file
df = pd.read_csv("BingoQuestions.csv")

# Extract the questions from the dataframe
# This part depends on the table format in the csv file
# The underlying idea is to have an array of questions like this:
# questions = ['Question 1', 'Question 2', ..., 'Question N']
questions = []
for column in df.columns:
    df[column] = df[column] + ';'
    questions.append(df[column].values)
questions = np.array(questions).flatten()
questions[-1] = questions[-1][:-1] # Remove the last semicolon

# Save to a text file
output_file = 'to_copy_into_tex.txt'

with open(output_file, 'w', encoding='utf-8') as file:
    file.write("\n".join(questions))

print(f"Questions have been saved to {output_file}")