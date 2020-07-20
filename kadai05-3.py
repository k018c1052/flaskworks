from flask import Flask, render_template, request
import datetime

app = Flask(__name__)
data = []
num = []

@app.route('/')
def index():
    zero = 0
    return render_template('kadai05-3.html', count=zero)

@app.route('/', methods=['POST'])
def send():
    totime = datetime.datetime.now().strftime('%m/%d %H:%M')
    walk = request.form.get('walk')
    data.append(totime + ' 歩数：' + walk)
    num.append(int(walk))
    nsum = sum(num) / len(num)
    return render_template('kadai05-3.html', list=data, nwalk=walk, count=nsum)

if __name__ == "__main__":
    app.debug = True
    app.run()
