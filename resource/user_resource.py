from flask_restful import Resource, reqparse

from repository import user_repository


class RegisterUser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help='username must be provided'
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help='password must be provided'
    )

    def post(self):
        data = RegisterUser.parser.parse_args()
        try:
            if user_repository.find_by_username(data['username']):
                return {'message': 'User already exists'}, 400
            user_repository.persist_user(data)
        except Exception:
            return {'message': 'User could not be saved'}, 404
        else:
            return {'message': 'User created'}, 201
