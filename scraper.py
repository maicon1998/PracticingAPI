import requests
from bs4 import BeautifulSoup

def scraper_data():
    response = requests.get('https://www.boxingscene.com/schedule')

    soup = BeautifulSoup(response.content, "html.parser")

    data = []

    for schedule in soup.find_all('div', class_='schedule-fight mb-4 mb-lg-0 py-lg-3 d-lg-flex align-items-center'):

        fight_date = schedule.find('div', class_='fight-day').text
        fight_day = schedule.find('div', class_='fight-date').text
        fighters_names = schedule.find('h3').text
    
        schedule_dict = {'date': fight_date, 'day': fight_day, 'names': fighters_names}
        data.append(schedule_dict)

    return data
