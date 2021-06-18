import dataset

db = dataset.connect('sqlite:///recipes')

recipes_table = db['recipes']