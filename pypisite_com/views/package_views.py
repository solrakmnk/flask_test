import flask
import services.package_service as package_service

blueprint = flask.Blueprint('packages', __name__, template_folder='template')


@blueprint.route('/project/<package_name>')
def package_details(package_name: str):
    # test_packages = package_service.get_latest_packages()
    package = package_name
    return flask.render_template('packages/details.html', package=package)

@blueprint.route('/<int:rank>')
def popular(rank: int):
    return "the top {} popular packages".format(rank)
