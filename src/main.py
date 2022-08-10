from flask import *
app = Flask('KatSit', template_folder='templates', static_folder='static')

@app.route('/')
def hello_world():
  return render_template('base.html')

app.run(host='0.0.0.0', port=8080)
