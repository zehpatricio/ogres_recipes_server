# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.recipe import Recipe
from .api.recipe_recipeId import RecipeRecipeid
from .api.recipe_recipeId_uploadImage import RecipeRecipeidUploadimage


routes = [
    dict(resource=Recipe, urls=['/recipe'], endpoint='recipe'),
    dict(resource=RecipeRecipeid, urls=['/recipe/<int:recipeId>'], endpoint='recipe_recipeId'),
    dict(resource=RecipeRecipeidUploadimage, urls=['/recipe/<int:recipeId>/uploadImage'], endpoint='recipe_recipeId_uploadImage'),
]