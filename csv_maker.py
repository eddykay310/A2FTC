from bs4 import BeautifulSoup
import os
import pandas as pd
import A2FTC_

base = os.getcwd()
all_csvs = []

def csvMaker():

    for folder in A2FTC_.folders:

        web_res_fol = f"{folder}\web_results"

        for item in os.listdir(f"{folder}\web_results"):
            if item.endswith(".summary.html"):
                html_doc = f"{web_res_fol}\{item}"

        summary_soup = BeautifulSoup(open(html_doc, encoding='utf8'), "html.parser")

        # getting the header from the HTML file
        list_header = []
        summary_header = summary_soup.find_all("table")[0].find("tr")

        for columns in summary_header:
            try:
                list_header.append(columns.text)
            except:
                continue

        data = []
        counter = 0

        for tr in summary_soup.findAll('tr')[1:]:
            # print(tr.find('a')['href'])
            no_ = tr.find('td').text
            sample_code = tr.find('a').text
            NoR = tr.findAll('td')[-1].text

            html_name = tr.find('a')['href']
            html_doc = f"{web_res_fol}\{html_name}"
            sample_soup = BeautifulSoup(open(html_doc, encoding='utf8'), "html.parser")

            if counter == 0:
                sample_header = sample_soup.find_all("table")[0].find("tr")
                for items in sample_header:
                    try:
                        list_header.append(items.text)
                    except:
                        continue
            counter+=1

            tr = sample_soup.findAll('tr')[1:]
            for element in tr: 
                sub_data = []
                sub_data.extend([no_,sample_code,NoR])
                for sub_element in element:
                    try:
                        # print(sub_element)
                        sub_data.append(sub_element.text)
                    except:
                        continue

                data.append(sub_data)

        # Storing the data into Pandas DataFrame 
        dataFrame = pd.DataFrame(data = data, columns = list_header) 

        # Converting Pandas DataFrame into CSV file 
        csv_name = folder.split("/")[-1]
        csv_path = f"{folder}\web_results\{csv_name}.csv"
        dataFrame.to_csv(csv_path,index=False) 

        all_csvs.append(csv_path)

    csvs = []
    for csv in all_csvs:
        read_csv = pd.read_csv(csv)
        csvs.append(read_csv)

    combined = pd.concat(csvs,keys=[i for i in range(len(csvs))],sort=False)
    combined.to_csv('combined.csv')

    