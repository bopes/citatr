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

@app.route("/convert", methods=["GET","POST"])
def convert():
  cit_input = request.args.get('input[text]','CITATION',type=str)
  pages = request.args.get('input[pages]','PAGES',type=str)
  finalCitation = string_parser.convert_citation(cit_input, pages)
  output = {'finalCitation': finalCitation}
  return jsonify(output)