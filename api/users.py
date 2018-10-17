from app.api.auth import token_auth

@bp.route('/users/<int:id>', methods=['GET'])
@token_auth.login_required
def get_user(id):
    pass

@bp.route('/users', methods=['GET'])
@token_auth.login_required
def get_users():
    pass

@bp.route('/users/<int:id>/followers', methods=['GET'])
@token_auth.login_required
def get_followers(id):
    pass

@bp.route('/users/<int:id>/followed', methods=['GET'])
@token_auth.login_required
def get_followed(id):
    pass

@bp.route('/users', methods=['POST'])
def create_user():
    pass

@bp.route('/users/<int:id>', methods=['PUT'])
@token_auth.login_required
def update_user(id):
    pass