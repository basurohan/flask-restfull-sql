from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from model import Item
from repository import item_repository


class ItemResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help='This field cannot be left blank.'
    )

    @jwt_required()
    def get(self, name):
        item = item_repository.get_item_by_name(name)
        if item:
            return {'item': item.__dict__}
        else:
            return {'message': 'item not found'}, 404

    def post(self, name):
        if item_repository.get_item_by_name(name) :
            return {'message': 'item already exists'}

        data = ItemResource.parser.parse_args()

        item = Item(name, data['price'])
        try:
            item_repository.persist_item(item)
        except Exception:
            return {'message': 'error occurred while creating item'}, 500
        else:
            return item.__dict__, 201

    # @jwt_required()
    def delete(self, name):
        if item_repository.get_item_by_name(name) is None:
            return {'message': 'item does not exist'}, 400

        try:
            item_repository.delete_item_by_name(name)
        except Exception:
            return {'message': 'error occurred while deleting item'}, 500
        else:
            return {'message': 'item deleted'}

    def put(self, name):
        data = ItemResource.parser.parse_args()

        item = item_repository.get_item_by_name(name)
        if item is None:
            try:
                item_repository.persist_item(Item(name, data['price']))
            except Exception:
                return {'message': 'error occurred while creating item'}, 500
        else:
            item.price = data['price']
            try:
                item_repository.update_item(item)
            except Exception:
                return {'message': 'error occurred while updating item'}, 500

        return item.__dict__, 201


class ItemListResource(Resource):

    def get(self):
        item_list = item_repository.get_items_list()
        return {'items': [item.__dict__ for item in item_list]}
