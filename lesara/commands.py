import csv 
import click

from lesara import app, db
from lesara.models import Order

@app.cli.command()
@click.argument('csvfile_path')
def fill_db(csvfile_path):
    with open(csvfile_path, 'r') as f:
        reader = csv.reader(f)
        #skip the header
        next(reader, None) 
        for row in reader:
            db.session.add(Order(*row))
        db.session.commit()