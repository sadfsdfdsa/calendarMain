from flask import render_template, flash, redirect, url_for, request
from flask import Flask
import sqlite3


app = Flask(__name__)
base_url = 'http://127.0.0.1:5000/' ## поменять в day.html и index.html

@app.route('/kalend', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    class Data:
        month = request.args.get("month")
        year = request.args.get("year")
    data = Data
    months = {'January' : 31, 'February' : 30, 'March' : 31, 'April' : 30, 'May' : 31, 'June' : 30, 'July' : 31, 'August' : 31, 'September' : 30, 'October' : 31, 'November' : 30, 'December' : 31}
    days = months.get(data.month, 0)
    return render_template('index.html', days=days, title=data.month, year=data.year, base_url=base_url)

@app.route('/day', methods=['GET', 'POST'])
def day():
    class Data:
        day = request.args.get("day")
        month = request.args.get("month")
        year = request.args.get("year")
        if request.args.get('add'):
            add = (request.args.get('add'))
        else:
            add=False
        if request.args.get('del'):
            delete=True
        else:
            delete=False
    data = Data
    conn = sqlite3.connect('default.sqlite3')
    cursor = conn.cursor()
    if data.add:
        try:
            string = "DELETE FROM data WHERE day = "+data.day+" AND month = '"+str(data.month)+"' AND year = "+data.year
            cursor.execute(string)
        except:
            pass
        string = "INSERT INTO data VALUES ("+data.day+", '"+data.month+"', "+data.year+", '"+data.add+"')"
        cursor.execute(string)
    if data.delete:
        try:
            string = "DELETE FROM data WHERE day = "+data.day+" AND month = '"+str(data.month)+"' AND year = "+data.year
            cursor.execute(string)
        except:
            pass
    string = "SELECT text FROM data WHERE day = "+data.day+" AND month = '"+str(data.month)+"' AND year = "+data.year
    cursor.execute(string)
    text = cursor.fetchone()
    try:
        text=text[0]
    except:
        text="Заметок нет"
    conn.commit()
    return render_template('day.html', data = data, text = text, base_url=base_url)

if __name__ == '__main__':
    app.run()

