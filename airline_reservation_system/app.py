from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'airline_db'

mysql = MySQL(app)

@app.route('/')
def index():
    # Fetch flights from the database
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM flights")
    flights = cur.fetchall()
    cur.close()
    return render_template('index.html', flights=flights)

@app.route('/book/<int:flight_id>')
def book(flight_id):
    # Fetch flight details
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM flights WHERE id = %s", (flight_id,))
    flight = cur.fetchone()
    cur.close()
    return render_template('booking.html', flight=flight)

if __name__ == '__main__':
    app.run(debug=True)