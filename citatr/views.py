# flask imports
from flask import request, session, g, redirect, url_for, abort,render_template, flash, json, jsonify
import bcrypt
# import citatr app
from citatr import app, db
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
    d = db.get_db()
    # Encode the user provided password for hash comparison
    encode_pw = request.form['password'].encode('UTF-8','strict')
    # Find the given username in databse (SQLi safe)
    cmd = "SELECT * FROM users WHERE username=?"
    user = d.execute(cmd,(request.form['username'],)).fetchone()
    # Check that the user exists and password validates
    if user and bcrypt.hashpw(encode_pw, user[2]) == user[2]:
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
  flash('Account logged out.')
  return redirect(url_for('login'))


@app.route("/index")
def index():
  if not session.get('logged_in'):
    return redirect(url_for('login'))
  return render_template('index.html')


@app.route('/signup', methods=["GET","POST"])
def signup():
  if request.method == "GET":
    if not session.get('logged_in'):
      return render_template('signup.html')
    return redirect(url_for('index'))
  else:
    # Check all fields are entered
    if any(entry == "" for entry in request.form.values()):
      error = 'All values must be filled.'
      return render_template('signup.html', error=error)
    # Confirm password
    elif request.form['password'] != request.form['password_cnf']:
      error = 'Password and password confirmation must match.'
      return render_template('signup.html', error=error)
    d = db.get_db()
    # Check if username has already been taken
    cmd = "SELECT * FROM users WHERE username LIKE ?"
    if d.execute(cmd,(request.form['username'],)).fetchone():
      error = 'Username already taken. Please select a different username.'
      return render_template('signup.html', error=error)
    # Add user to table
    encode_pw = request.form['password'].encode('UTF-8','strict')
    hashed_pw = bcrypt.hashpw(encode_pw, bcrypt.gensalt())
    cmd = "INSERT INTO users (username, password) VALUES (?,?)"
    d.execute(cmd,(request.form['username'], hashed_pw))
    d.commit()
    flash('Account created.')
    return redirect(url_for('login'))




@app.route("/convert", methods=['POST'])
def convert():
  if not session.get('logged_in'):
    abort(401)
  input_citation = request.form['input_text']
  pages = request.form['input_pages']
  final_citation = converter.convert_citation(input_citation, pages)
  output = {'finalCitation': final_citation}
  return jsonify(output)