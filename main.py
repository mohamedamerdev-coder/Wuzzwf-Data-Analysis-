from scrap import wuzzuf_scrap
from dataclean import clean_jobs_csv
from visualize import visualize_data

def main():
    print(" Starting the Wuzzuf Data Project...")
    print("\nStep 1: Scraping data from Wuzzuf...")

    wuzzuf_scrap(pages=20)
    print("\nStep 2: Cleaning the data...")
    clean_jobs_csv(input_file="wuzzuf_jobs.csv", output_file="jobs_cleaned.csv")

   
    print("\nStep 3: Generating visualizations...")
    visualize_data(file_path="jobs_cleaned.csv")

    print("\n All steps completed successfully!")

if __name__ == "__main__":
    main()



