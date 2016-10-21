# flask imports
from flask import request, session, g, redirect, url_for, abort,render_template, flash, json, jsonify
import bcrypt
# import citatr app
from citatr import app, get_db
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
    db = get_db()
    # Encode the user provided password for hash comparison
    given_pw = bytes(request.form['password'], 'utf-8')
    # Find the given username in databse (SQLi safe)
    cmd = "SELECT * FROM users WHERE username=?"
    user = db.execute(cmd,(request.form['username'],)).fetchone()
    # Check that the user exists and password validates
    if user and bcrypt.hashpw(given_pw, user[2]) == user[2]:
      session['logged_in'] = True
      return redirect(url_for('index'))
    # Invalid credential handling
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