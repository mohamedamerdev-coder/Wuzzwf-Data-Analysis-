import pandas as pd
import matplotlib.pyplot as plt
import os

def visualize_data(file_path="jobs_cleaned.csv"):
    df = pd.read_csv(file_path)

    os.makedirs("charts", exist_ok=True)

    plt.rcParams['font.family'] = 'DejaVu Sans'

    top_companies = df['company'].value_counts().head(10)
    plt.figure(figsize=(10, 5))
    top_companies.plot(kind='bar', color='skyblue')
    plt.title('Top 10 Companies by Job Count')
    plt.xlabel('Company')
    plt.ylabel('Number of Jobs')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig("charts/top_companies.png", dpi=300)
    plt.close()

    top_locations = df['location'].value_counts().head(10)
    plt.figure(figsize=(10, 5))
    top_locations.plot(kind='barh', color='lightgreen')
    plt.title('Top 10 Locations by Job Count')
    plt.xlabel('Number of Jobs')
    plt.ylabel('Location')
    plt.tight_layout()
    plt.savefig("charts/top_locations.png", dpi=300)
    plt.close()

    job_types = df['type_jop'].value_counts()
    plt.figure(figsize=(6, 6))
    job_types.plot(kind='pie', autopct='%1.1f%%', startangle=140,
                   colors=['#ff9999', '#66b3ff', '#99ff99'])
    plt.title('Job Type Distribution')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig("charts/job_types.png", dpi=300)
    plt.close()

    print("Visualizations generated and saved in 'charts/' folder!")
if __name__ == "__main__":
    visualize_data()
