# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import Resource
from v1.api import database


class RecipeRecipeid(Resource):

    def get(self, recipeId):
        return database.table_recipes.find_one(id=recipeId), 200, None

    def delete(self, recipeId):
        database.table_recipes.delete(id=recipeId)
        return None, 400, None