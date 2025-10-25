import pandas as pd

def clean_jobs_csv(input_file="wuzzuf_jobs.csv", output_file="jobs_cleaned.csv"):
    df = pd.read_csv(input_file)
    df['company'] = df['company'].str.replace(' -', '').str.strip()
    df['location'] = df['location'].str.strip()
    df['type_jop'] = df['type_jop'].str.lower().str.replace(' / ', '/').str.strip()
    df = df.drop_duplicates()
    df.to_csv(output_file, index=False)
    print(f"done, {output_file}")

if __name__ == "__main__":
    clean_jobs_csv()

