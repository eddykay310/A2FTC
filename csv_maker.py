from bs4 import BeautifulSoup
import os
import pandas as pd
import re


def csvMaker(base_dir,folders):

    all_csvs = []
    bestscores_allcsvs = []
    csvs = []
    bestscores_csvs = []
    csv_names = []
    bestscores_csvnames = []
    best_scores = []
    
    for folder in folders:
        
        web_res_fol = os.path.join(folder, "web_results")

        for item in os.listdir(web_res_fol):
            if item.endswith(".summary.html"):
                html_doc = os.path.join(web_res_fol, item)

        summary_soup = BeautifulSoup(open(html_doc, encoding='utf8'), "html.parser")

        # getting the header from the HTML file
        list_header = []
        summary_header = summary_soup.find_all("table")[0].find("tr")

        for column in summary_header:
            try:
                column = column.text
                column = column.replace("\n"," ").replace(" ","")
                list_header.append(column)
            except:
                continue

        data = []
        counter = 0
        # get individual sample
        print("\nExtracting table data from smple sequences")
        for tr in summary_soup.findAll('tr')[1:]:
            # print(tr.find('a')['href'])
            no_ = tr.find('td').text
            sample_code = tr.find('a').text
            NoR = tr.findAll('td')[-1].text

            html_name = tr.find('a')['href']
            html_doc = os.path.join(web_res_fol, html_name)
            sample_soup = BeautifulSoup(open(html_doc, encoding='utf8'), "html.parser")

            if counter == 0:
                sample_header = sample_soup.find_all("table")[0].find("tr")
                for column in sample_header:
                    try:
                        column = column.text
                        column = column.replace("\n"," ").replace(" ","")
                        list_header.append(column)
                    except:
                        continue
            counter+=1

            # get individual repeat found
            trs = sample_soup.findAll('tr')[1:]
            counter2 =0
            for tr in trs: 
                sub_data = []
                sub_data.extend([no_,sample_code,NoR])
                for sub_element in tr:
                    try:
                        # print(sub_element)
                        sub_data.append(sub_element.text)
                    except:
                        print("\nCouldn't extract data from individual tandem repeats")
                
                data.append(sub_data)

                print("\nGetting consensus sequence")
                htmlDoc = tr.find('a')['href'].split('#')[0]
                html_doc = os.path.join(web_res_fol,htmlDoc)
                repeat_soup = BeautifulSoup(open(html_doc, encoding='utf8'), "html.parser")

                consensus_pattern = re.sub("[^ATCG]", "", repeat_soup.find('pre').text.split('Consensus pattern',1)[1].split(':')[1])
                sub_data.append(consensus_pattern)

                if counter2 ==0:
                    best_scores.append(data[-1])
                counter2+=1

        list_header.append("ConsensusPattern")

        # Storing the data into Pandas DataFrame 
        print("\nBuilding individual dataframes")
        dataFrame = pd.DataFrame(data=data,columns=list_header)
        best_scoresdf = pd.DataFrame(data=best_scores,columns=list_header)

        # Converting Pandas DataFrame into CSV file 
        csv_name = folder.split("/")[-1]
        bestscores_csvname = folder.split("/")[-1]+"_bestscore"

        csv_path = os.path.join(web_res_fol, f"{csv_name}.csv")
        bestscores_csvpath = os.path.join(web_res_fol, f"{bestscores_csvname}.csv")

        dataFrame.to_csv(csv_path,index=False) 
        best_scoresdf.to_csv(bestscores_csvpath,index=False)

        csv_names.append(csv_name)
        bestscores_csvnames.append(bestscores_csvname)

        all_csvs.append(csv_path)
        bestscores_allcsvs.append(bestscores_csvpath)
    
    print("\nIndividual CSVs made in the web results folder of each selected folder")
    
    for csv in all_csvs:
        read_csv = pd.read_csv(csv)
        csvs.append(read_csv)
    
    combined = pd.concat(csvs,keys=[i for i in csv_names],sort=False,names=['Folders','ID'])
    combined.to_csv('all_combined_repeatfiles.csv')

    for csv in bestscores_allcsvs:
        read_csv = pd.read_csv(csv)
        bestscores_csvs.append(read_csv)
    
    bestscores_combined = pd.concat(bestscores_csvs,keys=[i for i in bestscores_csvnames],sort=False,names=['Folders','ID'])
    bestscores_combined.to_csv('bestscores_combined_repeatfiles.csv')

    print("\nCombined CSV made in parent folder of each selected folder")

