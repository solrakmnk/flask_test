import flask

from services import cms_service

blueprint = flask.Blueprint('cms', __name__, template_folder='templates')


@blueprint.route('/<path:full_url>')
def cms_page(full_url: str):
    page = cms_service.get_page(full_url)
    if not page:
        flask.abort(404)
    return flask.render_template('cms/page.html', page=page)

