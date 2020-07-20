from flask import Flask, render_template, request
import datetime

app = Flask(__name__)
data =[]

@app.route('/')
def index():
    return render_template('kadai05-2.html')

@app.route('/', methods=['POST'])
def send():
    walk = request.form.get('walk')
    totime = datetime.datetime.now().strftime('%m/%d %H:%M')
    data.append(totime + ' 歩数：' + walk)
    return render_template('kadai05-2.html', list=data, nwalk=walk)

if __name__ == "__main__":
    app.debug = True
    app.run()
