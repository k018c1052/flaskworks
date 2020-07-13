from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/sample/<username>/')
def template(username):
    l_list = {'apple':'リンゴ', 'orange':'みかん', 'lemon':'レモン'}
    return render_template('index.html', title1='タイトル', obj={'title2': 'タイトル2'}, num = 7,
                           list1=["アイテム1", "アイテム2", "アイテム3"], list2=l_list, message=username)



if __name__ == "__main__":
    app.debug = True
    app.run()
