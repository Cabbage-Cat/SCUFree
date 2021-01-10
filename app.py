from flask import Flask, render_template, request, redirect
import scuCourseScore
import scucas
import json
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("login.html")
    # return 'Hello World!'


@app.route('/test', methods=['POST'])
def test_app():
    username = request.form.get('username')
    passwd = request.form.get('passwd')
    loginFlag = True
    try:
        sess = scucas.zhjwLogin(username, passwd)
    except:
        loginFlag = False
    finally:
        if loginFlag:
            jsonStr = scuCourseScore.getCourseScoreJson(sess).decode('utf-8')
            jsonData = json.loads(jsonStr)
            return render_template("score.html", data=jsonData)
        else:
            return render_template("login.html")


if __name__ == '__main__':
    app.run()
