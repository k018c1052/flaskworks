from flask import Flask, render_template
import mysql.connector as db

db_pram = {
    'user' : 'mysql',
    'host' : 'localhost',
    'password': '',
    'database': 'db1'
}

app = Flask(__name__)

@app.route('/')
def index():
    conn = db.connect(**db_pram)
    cur = conn.cursor()
    stmt = 'SELECT * FROM books'
    cur.execute(stmt)
    rows = cur.fetchall()
    conn.close()
    return render_template('index.html', books=rows)

if __name__ == "__main__":
    app.debug = True
    app.run()
