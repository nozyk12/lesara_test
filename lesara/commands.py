import click
from lesara import app, db

@app.cli.command()
def update_db():
    db.create_all()
