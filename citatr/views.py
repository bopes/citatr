# flask imports
from flask import request, session, g, redirect, url_for, abort,render_template, flash, json, jsonify
# import citatr app
from citatr import app
# citatr imports
from citatr.converter_pkg import converter

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
  final_citation = converter.convert_citation(input_citation, pages)
  output = {'finalCitation': final_citation}
  return jsonify(output)