import dataset

db = dataset.connect('sqlite:///recipes_database')

table_recipes = db['recipes']