import flask


blueprint = flask.Blueprint('account', __name__, template_folder='templates')


# ################### INDEX #################################


@blueprint.route('/account')
def index():
    return {}


# ################### REGISTER #################################

@blueprint.route('/account/register', methods=['GET'])
def register_get():
    return {}


@blueprint.route('/account/register', methods=['POST'])
def register_post():
    return {}


# ################### LOGIN #################################

@blueprint.route('/account/login', methods=['GET'])
def login_get():
    return {}


@blueprint.route('/account/login', methods=['POST'])
def login_post():
    return {}


# ################### LOGOUT #################################

@blueprint.route('/account/logout')
def logout():
    return {}