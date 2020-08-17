from flask import Flask, render_template, request, redirect
import mysql.connector as db
import datetime

db_param = {
    'user': 'mysql',
    'host': 'localhost',
    'password': '',
    'database': 'tododb'
}

app = Flask(__name__)

@app.route('/')
def index():
    conn = db.connect(**db_param)
    cur = conn.cursor()
    stmt = 'SELECT * FROM list'
    cur.execute(stmt)
    rows = cur.fetchall()
    conn.close()
    return render_template('last_task_1.html', list=rows)


@app.route('/send', methods=['POST'])
def send():
    ndate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    title = request.form.get('title')
    if title == "":
        return redirect('/')

    conn = db.connect(**db_param)
    cur = conn.cursor()
    stmt = 'SELECT * FROM list WHERE title=%s'
    cur.execute(stmt, (title,))
    rows = cur.fetchall()
    print(title)
    if title in ',':
        t_list = title.split(',')
        for item in t_list:
            cur.execute('INSERT INTO list(date, title) VALUES(%s, %s)',
                    (ndate, item))
    else:
        cur.execute('INSERT INTO list(date, title) VALUES(%s, %s)', (ndate, title))
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    del_list = request.form.getlist('del_list')
    conn = db.connect(**db_param)
    cur = conn.cursor()
    for id in del_list:
        stmt = 'SELECT * FROM list WHERE id=%s'
        cur.execute(stmt, (id,))
        rows = cur.fetchall()
        stmt = 'DELETE FROM list WHERE id=%s'
        cur.execute(stmt, (id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/')

if __name__ == "__main__":
    app.debug = True
    app.run()
