import os
from flask import *
app = Flask(__name__)

@app.route('/')
def web():
	instance_number = int(os.getenv("CF_INSTANCE_INDEX"))
	return render_template('main.html', instance_number = instance_number)
