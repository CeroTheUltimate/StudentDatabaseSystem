import pandas as pd

# Read the Excel BSIT database
df = pd.read_excel("BSIT DATA.xlsx")

# Removes unnecessary or empty columns and clean column names
df = df.dropna(axis=1, how="all")
df.columns = df.columns.astype(str).str.strip()

# Display available columns
print("===== BSIT STUDENT DATABASE =====")
print("Available Columns:")

for column in df.columns:
    print(column)


# FREQUENCY AND PERCENTAGE
def frequency_percentage():

    column = input("Enter column name: ")

    if column not in df.columns:
        print("Column not found!")
        return

    # Counts each answer
    frequency = df[column].value_counts()

    # Calculates the percentage
    percentage = df[column].value_counts(normalize=True) * 100

    # Displays the results
    result = pd.DataFrame({
        "Frequency": frequency,
        "Percentage": percentage.round(2)
    })

    print("===== FREQUENCY AND PERCENTAGE =====")
    print(result)


# MEAN
def calculate_mean():

    # Selects the numerical columns
    numeric_data = df.select_dtypes(include="number")

    # Calculates the average of each column
    mean = numeric_data.mean()

    print("===== MEAN RESULTS =====")
    print(mean.round(2))

# MAIN MENU
while True:

    print("===== STUDENT STATISTICAL SYSTEM =====")
    print("1. View Student Database")
    print("2. Calculate the Frequency and Percentage")
    print("3. Calculate the Mean")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # (.to_string) means to display the DataFrame as text
        # ((index=False)) means it hides the automatic row numbers
        print(df.to_string(index=False))

    elif choice == "2":
        frequency_percentage()

    elif choice == "3":
        calculate_mean()

    elif choice == "4":
        print("You have closed the program!")
        break

    else:
        print("Invalid choice. Please try again.")
