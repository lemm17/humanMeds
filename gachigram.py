from app import app, db
from app.entities import *


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Publication': Publication, 'association_subscriptions': association_subscriptions}