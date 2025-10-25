
Wuzzwf Data Analysis

---

Overview

This project collects and analyzes "Data Analysis" job data from Wuzzuf using web scraping, cleans the dataset, and presents visualizations for easy insights.


---

Features

Data Scraping:
Uses Selenium and BeautifulSoup to extract job title, company, location, and job type.

Data Cleaning:
Removes duplicates, standardizes formats, and cleans columns.

Data Visualization:
Creates charts showing job distribution by company, location, and job type.

Automated Pipeline:
The main.py script runs all steps automatically: scraping → cleaning → visualizing.



---

Technologies Used

Python – Main programming language

Selenium – For scraping web pages

BeautifulSoup – For parsing HTML

Pandas – For data manipulation and analysis

Matplotlib – For data visualization



---

How to Use

1. Clone the repository:



git clone https://github.com/mohamedamerdev-coder/Wuzzwf-Data-Analysis-
cd Wuzzwf-Data-Analysis-

2. Install dependencies:



pip install selenium beautifulsoup4 pandas matplotlib

3. Run the main script:



python main.py

Steps executed automatically:

1. Scrapes job data from Wuzzuf


2. Cleans and saves the data


3. Generates charts in the charts/ folder




---

Project Structure

Wuzzwf-Data-Analysis/
│
├── scrap.py             # Scraping functions
├── dataclean.py         # Data cleaning functions
├── visualize.py         # Visualization functions
├── main.py              # Main pipeline
├── wuzzuf_jobs.csv      # Raw scraped data
├── jobs_cleaned.csv     # Cleaned data
└── charts/              # Generated visualizations


---

Notes

You can adjust the number of pages to scrape by changing the pages argument in wuzzuf_scrap().

Make sure ChromeDriver is installed and compatible with your Chrome version.

Visualizations are saved in charts/ as high-resolution PNG files.



---

License

This project is licensed under the MIT License.
