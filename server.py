from flask import Flask, render_template, request,session, redirect, url_for, jsonify

app = Flask(__name__,template_folder='template')

@app.route("/")
def home():
    return "<h1> Hello! This is the main page</h2>"

@app.route('/sample')
def sample():
    user = {'username': 'foobar'}
    return render_template('sample.html', title='Sample', user=user)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)
