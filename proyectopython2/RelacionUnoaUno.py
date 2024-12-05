import peewee
from datetime import datetime
# Conexión a la base de datos MySQL
database = peewee.MySQLDatabase('pythonndb', host='localhost', port=3306, user='root', passwd='root')



class User(peewee.Model):
    username=peewee.CharField(max_length=50)
    email=peewee.CharField(max_length=50)
    
    class Meta:
        database=database
        data_table='users'

    def __str__(self):
        return self.username
    @property
    def admin(self):
        return self.admins.first()  

class Admin(peewee.Model):
    Permission_level=peewee.IntegerField(default=1)
    user=peewee.ForeignKeyField(User,backref='admins',unique=True)

    class Meta:
        database    =database
        data_table='admins'

    def __str__(self):
        return 'Admin ' +str(self.id)

if __name__ == '__main__':
    database.drop_tables([User,Admin])
    database.create_tables([User,Admin])

    user1=User.create(username='User1',email='Moangel5602599@gmail.com')
    admin1=Admin.create(Permission_level=10,user=user1)


    #print(admin1.user.email)
    print(user1.admin)

    admin2=Admin.create(Permission_level=5)

