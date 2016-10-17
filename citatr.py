# flask imports
import os
from flask import Flask, request, session, g, redirect, url_for, abort,render_template, flash, json, jsonify
# citatr imports
import string_parser

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    SECRET_KEY='development key',
    USERNAME='bigep',
    PASSWORD='yankeehotelfoxtrot'
))


@app.route("/")
def root():
  if session.get('logged_in'):
    return render_template('index.html')
  return render_template('login.html')


@app.route("/login", methods=["GET","POST"])
def login():
  error = None
  if request.method == "POST":
    if request.form['username'] == app.config['USERNAME'] and request.form['password'] == app.config['PASSWORD']:
      session['logged_in'] = True
      flash('Successfully logged in.')
      return redirect(url_for('index'))
    else:
      error = 'Invalid credentials.'
      return render_template('login.html', error=error)
  else:
    if not session.get('logged_in'):
      return render_template('login.html')
    return redirect(url_for('index'))


@app.route("/logout")
def logout():
  session['logged_in'] = False
  flash('Successfully logged out.')
  return redirect(url_for('login'))


@app.route("/index")
def index():
  if not session.get('logged_in'):
    return redirect(url_for('login'))
  return render_template('index.html')


@app.route("/convert", methods=['POST'])
def convert():
  if not session.get('logged_in'):
    abort(401)
  input_citation = request.form['input_text']
  pages = request.form['input_pages']
  final_citation = string_parser.convert_citation(input_citation, pages)
  output = {'finalCitation': final_citation}
  return jsonify(output)


if __name__ == '__main__':
  app.debug = True
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)