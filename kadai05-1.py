from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('kadai05-1.html')

@app.route('/send', methods=['POST'])
def send():
    name = request.form.get('name')
    mail = request.form.get('mail')
    return render_template('receive05-1.html', uname=name, email=mail)

if __name__ == "__main__":
    app.debug = True
    app.run()
