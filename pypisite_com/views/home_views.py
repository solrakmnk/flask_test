import flask
import services.package_service as package_service
from services import user_service

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
def index():
    return flask.render_template('home/index.html',
                                 releases=package_service.get_latest_releases(),
                                 packages_count=package_service.get_package_count(),
                                 release_count=package_service.get_release_count(),
                                 user_count=user_service.get_user_count(),
                                 )


@blueprint.route('/about')
def about():
    return flask.render_template('home/about.html')
