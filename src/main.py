from flask import *
import os
import json as jsonfiles

app = Flask('KatSit', template_folder='templates', static_folder='static')
session_filename = os.path.join('data', 'session.json')
userdata_filename = os.path.join('data', 'userdata.json')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/login')
def login():
  with open(session_filename) as f:
    result = jsonfiles.load(f)
    if 'username' in result and 'password' in result:
        return redirect(url_for('dashboard'))
    return render_template("login.html")
    
@app.route('/dashboard', methods = ['POST', 'GET'])
def dashboard():
  global session_filename
  global userdata_filename
  with open(userdata_filename) as f:
    user_data = jsonfiles.load(f)
  if request.method == 'GET':
    with open(session_filename) as f:
      result = jsonfiles.load(f)
    if 'username' in result and 'password' in result:
      return render_template('dashboard.html',form_data = result, user_data = user_data)
  
  elif request.method == 'POST':
    result = request.form.to_dict(flat=False)
    with open(session_filename, 'w') as f:
      jsonfiles.dump(result, f)
    return render_template('dashboard.html',form_data = result, user_data = user_data)
  
@app.route('/logout')
def logoout():
  global session_filename
  with open(session_filename, 'w') as f:
    jsonfiles.dump({}, f)
  return redirect(url_for('index'))

  
app.run(host='0.0.0.0', port=8080)
