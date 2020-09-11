from bs4 import BeautifulSoup
import requests

def write_to_csv(data):
    #print("I am here !!!")
    file = open("C:/Users/TAHIR/Desktop/univelcity/python class/SQL/coviddata.csv","a")

    file.write(f"{data[0]},{data[1]},{data[2]},{data[3]}\n")
    file.close()


data = requests.get("https://en.wikipedia.org/wiki/COVID-19_pandemic_by_country_and_territory")

wiki_soup = BeautifulSoup(data.content,features="html.parser")

write_to_csv(["location","cases","deaths","recoveries"])

world_data = wiki_soup.find("tr",{"class":"sorttop"})
world_data_cells = world_data.find_all("th")
world_cases,world_deaths,world_recoveries = world_data_cells[2].get_text(),world_data_cells[3].get_text(),world_data_cells[4].get_text()

world_cases = world_cases.replace(",","").replace("\n","")
world_deaths = world_deaths.replace(",","").replace("\n","")
world_recoveries = world_recoveries.replace(",","").replace("\n","")

write_to_csv(["Global",world_cases,world_deaths,world_recoveries])

other_countries = wiki_soup.find("div",{"id":"covid19-container"}).find_all("tr")

for row in other_countries:
    row_cells = row.find_all("td")
# 
    try:
        # print(row_cells[0])

        country_name = row.find("a").get_text()
        #print(country_name.get_text())

        row_cells_cases,row_cells_deaths,row_cells_recoveries = row_cells[0].get_text(),row_cells[1].get_text(),row_cells[2].get_text()
        
        row_cells_cases = row_cells_cases.replace(",","").replace("\n","")
        row_cells_deaths = row_cells_deaths.replace(",","").replace("\n","")
        row_cells_recoveries = row_cells_recoveries.replace(",","").replace("\n","")

        write_to_csv([country_name,row_cells_cases,row_cells_deaths,row_cells_recoveries])

    except IndexError :
        pass 