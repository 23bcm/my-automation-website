import pandas as pd

def calculate_work_hours(input_file, output_file):
    try:
        print(f"Reading {input_file}...")
        df = pd.read_excel(input_file)
        print("File read successfully!")

        print("Checking required columns...")
        required_columns = {'Employee', 'Start Time', 'End Time'}
        if not required_columns.issubset(df.columns):
            print(f"Error: Missing required columns. Found columns: {df.columns}")
            return

        print("Processing data...")
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['End Time'] = pd.to_datetime(df['End Time'])
        df['Hours Worked'] = (df['End Time'] - df['Start Time']).dt.total_seconds() / 3600

        print("Calculating total hours per employee...")
        summary = df.groupby('Employee')['Hours Worked'].sum().reset_index()

        print(f"Saving results to {output_file}...")
        summary.to_excel(output_file, index=False)
        print("Done! Results saved.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Starting the script...")
    calculate_work_hours("input.xlsx", "output.xlsx")
    print("Script finished.")



