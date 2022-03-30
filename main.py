from unicodedata import name
from db.database import Database
from helper.WriteAJson import writeAJson

db = Database("db", "livros")


db.create("Livro1", "Autor1", 2001, 10.0)
db.create("Livro2", "Autor2", 2002, 20.0)
db.create("Livro3", "Autor3", 2003, 30)


db.read()


db.update("livro1", 40.0)


db.delete("Livro2")
