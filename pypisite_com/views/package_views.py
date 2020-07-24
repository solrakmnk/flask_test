import flask
import services.package_service as package_service

blueprint = flask.Blueprint('packages', __name__, template_folder='template')


@blueprint.route('/project/<package_name>')
def package_details(package_name: str):
    if not package_name:
        return flask.abort(status=404)
    # test_packages = package_service.get_latest_packages()
    package = package_service.get_package_by_id(package_name)
    if not package:
        return flask.abort(status=404)

    latest_version = "0.0.0"
    latest_release = None
    is_latest = True

    if package.releases:
        latest_release = package.releases[0]
        latest_version = latest_release.version_text

    return flask.render_template('packages/details.html', package=package,
                                 latest_version=latest_version,
                                 latest_release=latest_release,
                                 release_version=latest_release,
                                 is_latest=is_latest)


@blueprint.route('/<int:rank>')
def popular(rank: int):
    return "the top {} popular packages".format(rank)
