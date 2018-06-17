from lesara import app, db

@app.route('/')
def index():
    return str(dir(db))