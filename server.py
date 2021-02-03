from flask import Flask, render_template, request,session, redirect, url_for, jsonify

app = Flask(__name__,template_folder='template')

@app.route("/")
def home():
    return "<h1> Hello! This is the main page</h2>"
    
if __name__ == "__main__":
    app.run()
