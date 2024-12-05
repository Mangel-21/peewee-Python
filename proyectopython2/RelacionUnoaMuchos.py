import peewee
from datetime import datetime
# Conexión a la base de datos MySQL
database = peewee.MySQLDatabase('pythonndb', host='localhost', port=3306, user='root', passwd='root')


class Autor(peewee.Model):
    name=peewee.CharField(max_length=50)
   
    class Meta:
        database=database
        db_table='autors'
    
    def __str__(self):
        return self.name

        
class Book(peewee.Model):
    title=peewee.CharField(max_length=50)
    autor=peewee.ForeignKeyField(Autor,backref='books') #todo tipo de autor accedera asus books

    class Meta:
        database=database
        db_table='books'

    def __str__(self):
        return self.title

if __name__ == '__main__':
    database.drop_tables([Autor,Book])
    database.create_tables([Autor,Book])

    autor1=Autor.create(name='angel')

    Book1=Book.create(title='50 sombras', autor=autor1)
    Book2=Book.create(title='El resplandor', autor=autor1)
    Book3=Book.create(title='Cuyo', autor=autor1)

    for book in autor1.books:
        print(book)