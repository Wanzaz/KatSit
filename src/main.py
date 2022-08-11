from flask import *
import os
import json as jsonfiles

app = Flask('KatSit', template_folder='templates', static_folder='static')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/login')
def login():
  return render_template("login.html")

@app.route('/dashboard', methods = ['POST', 'GET'])
def dashboard():
    if request.method == 'GET':
      filename = os.path.join(app.static_folder, 'data', 'session.json')
      with open(filename) as f:
        jsonfiles.load(result, f)
        return render_template('dashboard.html',form_data = result)
    
    if request.method == 'POST':
      result = request.form.to_dict(flat=False)
      filename = os.path.join(app.static_folder, 'data', 'session.json')
      with open(filename, 'w') as f:
        jsonfiles.dump(result, f)
      return render_template('dashboard.html',form_data = result)
  
app.run(host='0.0.0.0', port=8080)
