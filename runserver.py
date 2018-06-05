#!/usr/bin/env python
import os
from web import app

# run application
app.run(host='0.0.0.0', port=int(os.getenv("PORT")), debug=False, threaded=True)
