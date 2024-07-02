from flask import Flask, jsonify
from scraper import scraper_data

app = Flask(__name__)

@app.route('/schedule', methods=['GET'])
def schedule():
    data = scraper_data()
    return jsonify(data)

@app.route('/schedule/<int:id>', methods=['GET'])
def schedule_id(id):
    data = scraper_data()

    if id < len(data):
        return jsonify(data[id])
    else:
        return jsonify({'Error': 'Invalid ID'}), 404

if __name__ == '__main__':
    app.run(debug=True)
