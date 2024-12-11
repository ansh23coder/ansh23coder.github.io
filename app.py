from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "your_secret_key"

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '$1979'  # Replace with your actual MySQL password
app.config['MYSQL_DB'] = 'hospital'
mysql = MySQL(app)

# Home route for nurses
@app.route('/')
def home():
    return render_template('nurse.html')

# Route to add patient data
@app.route('/add_patient', methods=['POST'])
def add_patient():
    try:
        if request.method == 'POST':
            name = request.form['name']
            bp = request.form['bp']
            pulse = request.form['pulse']
            spo2 = request.form['spo2']
            temp = request.form['temp']

            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO Patients (name, bp, pulse, spo2, temperature) VALUES (%s, %s, %s, %s, %s)",
                (name, bp, pulse, spo2, temp)
            )
            mysql.connection.commit()
            cur.close()
            flash("Patient data added successfully!", "success")
    except Exception as e:
        flash("Error: Could not save data. Please try again.", "error")
    return redirect(url_for('home'))


# Route for doctors to view patient data
@app.route('/doctor')
def doctor():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Patients")
    data = cur.fetchall()
    cur.close()
    return render_template('doctor.html', patients=data)

if __name__ == '__main__':
    app.run(debug=True)
