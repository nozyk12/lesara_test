SQLALCHEMY_DATABASE_URI = 'mysql://{username}:{password}@{host}/{db_name}'.format(
    username='lesara',
    password='pass',
    host='db',
    db_name='lesara'
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True
