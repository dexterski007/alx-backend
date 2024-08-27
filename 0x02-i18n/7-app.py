#!/usr/bin/env python3
"""Flask app documentation."""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz


class Config:
    """Config class for babel."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Get locale function for babel."""
    locale = request.args.get('locale')
    if locale in app.config["LANGUAGES"]:
        return locale
    head_locale = request.headers.get("locale", "")
    if head_locale in app.config["LANGUAGES"]:
        return head_locale
    if g.user and g.user['locale'] in app.config["LANGUAGES"]:
        return g.user['locale']
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index() -> str:
    """Get index route for flask app."""
    return render_template("7-index.html")


def get_user() -> dict:
    """Function to get user information"""
    user_id = request.args.get('login_as')
    if user_id is not None and int(user_id) in users.keys():
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """Function to get user before request."""
    g.user = get_user()


@babel.timezoneselector
def get_timezone() -> str:
    """Function to get timezone."""
    try:
        if request.args.get('timezone'):
            return pytz.timezone(request.args.get('timezone')).zone
        if g.user and g.user['timezone']:
            return pytz.timezone(g.user['timezone']).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return pytz.timezone('UTC').zone


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
