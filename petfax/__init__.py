from flask import Flask
from flask_migrate import Migrate

#Factory
def create_app():
    app = Flask(__name__)

    # database config 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:tyler7820@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import models 
    models.db.init_app(app) 
    migrate = Migrate(app, models.db)


    @app.route('/')
    def hello():
        return 'Hello, PetFax'

    #Register pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)
    
    from . import fact 
    app.register_blueprint(fact.bp)

    #Return the app
    return app