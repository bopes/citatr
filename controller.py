# flask imports
import os
# import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort,render_template, flash, json, jsonify
# citatr imports
import string_parser

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/convert")
def convert():
  input_citation = request.args.get('input[text]','CITATION',type=str)
  pages = request.args.get('input[pages]','PAGES',type=str)
  final_citation = string_parser.convert_citation(input_citation, pages)
  output = {'finalCitation': final_citation}
  return jsonify(output)


# Heroku setup
if __name__ == '__main__':
  app.debug = True
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)