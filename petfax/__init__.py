from flask import Flask

#Factory
def create_app():
    app = Flask(__name__)

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