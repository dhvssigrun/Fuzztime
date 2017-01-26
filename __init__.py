from flask import Flask
from flask_bootstrap import Bootstrap

from views.main import main

bootstrap = Bootstrap()

if __name__ == '__main__':
    app = Flask(__name__)

    bootstrap.init_app(app)

    app.register_blueprint(main)

    app.run(debug=True)
