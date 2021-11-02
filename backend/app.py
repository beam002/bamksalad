from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import config

db = SQLAlchemy()
migrate = Migrate()
cors = CORS()


def create_app():
    app = Flask(__name__)
    
    app.config.from_object(config)

    from views import user_views, analysis_views
    url_prefix='/api'
    app.register_blueprint(user_views.bp, url_prefix=url_prefix)
    app.register_blueprint(analysis_views.bp, url_prefix=url_prefix)
    
    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
    return app

if __name__ == "__main__":
    app = create_app()
    # app.run(host='0.0.0.0', port='5000', debug=True)
    app.run(debug=True)
