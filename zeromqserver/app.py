from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/measurements')
def measurements():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, latitude, longitude, accuracy, altitude, speed, timestamp, cell_info FROM locations")
    rows = cursor.fetchall()
    conn.close()
    data = []
    for r in rows:
        data.append({
            "id": r[0],
            "lat": r[1],
            "lon": r[2],
            "accuracy": r[3],
            "altitude": r[4],
            "speed": r[5],
            "timestamp": r[6],
            "cell_info": r[7]
        })
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
