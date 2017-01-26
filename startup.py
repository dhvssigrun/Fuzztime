from flask import Flask
from flask_bootstrap import Bootstrap


bootstrap = Bootstrap()

if __name__ == '__main__':
    app = Flask(__name__)

    bootstrap.init_app(app)

    # import blueprints
    from main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    app.run(debug=True)

# from flask import Flask, render_template
#
# from fuzztime.fuzztime import Fuzztime
#
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def index():
#     fuzztime = Fuzztime()
#     fuzztime.fuzz()
#     # print(fuzztime.target)
#     return "{0}".format(fuzztime.fuzz())
#
# if __name__ == '__main__':
#     app.run(debug=True)