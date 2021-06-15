# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import g

from . import Resource
from v1.api import database


class Recipe(Resource):

    def get(self):
        return [r for r in database.table_recipes.all()], 200, None

    def post(self):
        database.table_recipes.insert(g.json)

        return database.table_recipes.find_one(**g.json), 200, None
        