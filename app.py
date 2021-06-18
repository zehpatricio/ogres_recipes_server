from flask import Flask, request
from flask_restful import Resource, Api
from database import recipes_table

app = Flask(__name__)
api = Api(app)


class RecipesResource(Resource):
    def get(self):
        return [r for r in recipes_table.all()]
    
    def post(self):
        _id = recipes_table.insert(request.json)
        request.json['id'] = _id
        return request.json, 200
    
    def put(self):
        return recipes_table.update(request.json, ['id'])


class RecipeResource(Resource):

    def get(self, recipe_id):
        return recipes_table.find_one(id=recipe_id)
    
    def delete(self, recipe_id):
        return recipes_table.delete(id=recipe_id)


# api.add_resource(RecipesResource, '/<string:todo_id>')
api.add_resource(RecipesResource, '/')
api.add_resource(RecipeResource, '/<int:recipe_id>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')