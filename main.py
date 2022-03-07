import json
import pandas as pd
import joblib

from flask import Flask,render_template,request


app = Flask(__name__)

@app.route('/')
@app.route('/home',methods=['GET'])
def hello():
    return 'hello_world'

@app.route('/api',methods=["POST"])
def sample():
    if request.method == "POST":
        try:
            post_data=request.get_json()
            json_data=json.dumps(post_data)
            s=pd.read_json(json_data)
            p=joblib.load('filename.pkl')
            r=p.predict(s)
            return str(r)
        except Exception as e:
            return (e)


if __name__ == "__main__":
    app.run(debug=True)