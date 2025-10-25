from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

def wuzzuf_scrap(pages=100):
    browser = webdriver.Chrome()
    wuzzuf_list = []

    for page in range(pages):
        url = f"https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q=data%20analysis&start={page}"
        browser.get(url)
        time.sleep(5)

        html = browser.page_source
        soup = BeautifulSoup(html, "html.parser")

        container_div = soup.find("div", class_="css-9i2afk")
        if not container_div:
            print(f"no data in {page}")
            break

        list_items = container_div.find_all("div", class_="css-ghe2tq e1v1l3u10")

        for div in list_items:
            jop_title = div.find("h2", class_="css-193uk2c")
            company = div.find("a", class_="css-ipsyv7")
            location = div.find("span", class_="css-16x61xq")
            type_jop = div.find("span", class_="css-uc9rga eoyjyou0")
        
            wuzzuf_list.append({
                "job_title": jop_title.text.strip() if jop_title else " ",
                "company": company.text.strip() if company else " ",
                "location": location.text.strip() if location else " ",
                "type_jop": type_jop.text.strip() if type_jop else " "
            })

        print(f" done {page + 1}")


    browser.quit()

    with open("wuzzuf_jobs.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["job_title", "company", "location", "type_jop"])
        writer.writeheader()
        writer.writerows(wuzzuf_list)

    print(f"\n Done {len(wuzzuf_list)} ")

    return wuzzuf_list



if __name__ == "__main__":
    data = wuzzuf_scrap(50)  




















