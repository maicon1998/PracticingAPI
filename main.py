from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/schedule', methods=['GET'])
def schedule():
    
    response = requests.get('https://www.boxingscene.com/schedule')

    soup = BeautifulSoup(response.content, "html.parser")

    data = []

    for schedule in soup.find_all('div', class_='schedule-fight mb-4 mb-lg-0 py-lg-3 d-lg-flex align-items-center'):

        fight_date = schedule.find('div', class_='fight-day').text
        fight_day = schedule.find('div', class_='fight-date').text
        fighters_names = schedule.find('h3').text
    
        schedule_dict = {'date': fight_date, 'day': fight_day, 'names': fighters_names}
        data.append(schedule_dict)

    return jsonify(data)

@app.route('/schedule/<int:id>', methods=['GET'])
def schedule_id(id):
    
    response = requests.get('https://www.boxingscene.com/schedule')

    soup = BeautifulSoup(response.content, "html.parser")

    data = []

    for schedule in soup.find_all('div', class_='schedule-fight mb-4 mb-lg-0 py-lg-3 d-lg-flex align-items-center'):

        fight_date = schedule.find('div', class_='fight-day').text
        fight_day = schedule.find('div', class_='fight-date').text
        fighters_names = schedule.find('h3').text
    
        schedule_dict = {'date': fight_date, 'day': fight_day, 'names': fighters_names}
        data.append(schedule_dict)

    if id < len(data):
        return jsonify(data[id])
    else:
        return jsonify({'error': 'invalid id'}), 404

if __name__ == '__main__':
    app.run(debug=True)
