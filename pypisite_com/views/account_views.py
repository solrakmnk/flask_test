import flask

from pypisite_com.infrastructure import cookie_auth, request_dict
from pypisite_com.infrastructure.view_modifiers import response
from pypisite_com.services import user_service
from pypisite_com.viewmodels.account.index_viewmodel import IndexViewModel
from pypisite_com.viewmodels.account.register_viewmodel import RegisterViewModel

blueprint = flask.Blueprint('account', __name__, template_folder='templates')


# ################### INDEX #################################


@blueprint.route('/account')
@response(template_file='account/index.html')
def index():
    vm = IndexViewModel()
    if not vm.user:
        return flask.redirect('account/login')
    return vm.to_dict()


# ################### REGISTER #################################

@blueprint.route('/account/register', methods=['GET'])
@response(template_file='account/register.html')
def register_get():
    vm = RegisterViewModel()
    return vm.to_dict()


@blueprint.route('/account/register', methods=['POST'])
@response(template_file='account/register.html')
def register_post():
    vm = RegisterViewModel()
    vm.validate()

    if vm.error:
        return vm.to_dict()
    user = user_service.create_user(vm.name, vm.email, vm.password)
    if not user:
        vm.error = 'The account could not be created'
        return vm.to_dict()

    resp = flask.redirect('/account')
    cookie_auth.set_auth(resp, user.id)

    return resp


# ################### LOGIN #################################

@blueprint.route('/account/login', methods=['GET'])
def login_get():
    return flask.render_template('account/login.html')


@blueprint.route('/account/login', methods=['POST'])
@response(template_file='account/login.html')
def login_post():
    r = flask.request
    email = r.form.get('email')
    password = r.form.get('password')

    if not email or not password:
        return {
            'email': email,
            'password': password,
            'error': "Some required fields are missing.",
        }
    user = user_service.login_user(email, password)
    if not user:
        return {
            'email': email,
            'error': "Invalid User/Password"
        }

    resp = flask.redirect('/account')
    cookie_auth.set_auth(resp, user_id=user.id)
    return resp


# ################### LOGOUT #################################

@blueprint.route('/account/logout')
def logout():
    resp = flask.redirect('/')
    cookie_auth.logout(resp)
    return resp
