import peewee
from datetime import datetime

# Conexión a la base de datos MySQL
# Se establece la conexión a la base de datos llamada 'pythonndb' en el servidor localhost
database = peewee.MySQLDatabase('pythonndb', host='localhost', port=3306, user='root', passwd='root')

# Definición de la clase Product (Producto)
class Product(peewee.Model):
    # Se definen los campos que tendrá la tabla 'products'
    name = peewee.CharField(max_length=50)  # Cambié 'title' por 'name' para mayor claridad
    price = peewee.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        database = database  # Se asocia con la base de datos 'pythonndb'
        db_table = 'products'  # Nombre de la tabla

    def __str__(self):
        return self.name  # Cuando se imprime un objeto de Product, muestra su nombre

# Definición de la clase Category (Categoría)
class Category(peewee.Model):
    # Se define un campo 'name' para representar el nombre de la categoría
    name = peewee.CharField(max_length=20)

    class Meta:
        database = database  # Se asocia con la base de datos 'pythonndb'
        db_table = 'categories'  # Nombre de la tabla

    def __str__(self):
        return  self.name  # Cuando se imprime un objeto de Category, muestra su nombre

# Definición de la clase ProductCategory (Categoría del Producto) - Relación Muchos a Muchos
class ProductCategory(peewee.Model):
    # Definimos las relaciones de clave foránea a los modelos Product y Category
    product = peewee.ForeignKeyField(Product, backref='categories')  # Relación con el producto
    category = peewee.ForeignKeyField(Category, backref='products')  # Relación con la categoría
    
    class Meta:
        database = database  # Se asocia con la base de datos 'pythonndb'
        db_table = 'product_categories'  # Nombre de la tabla intermedia


# Código principal que se ejecuta cuando se corre el script
if __name__ == '__main__':
    
    # Borra las tablas existentes si ya existen, y las crea nuevamente
    database.drop_tables([Product, Category, ProductCategory])
    database.create_tables([Product, Category, ProductCategory])

    # Creamos instancias de productos
    ipad = Product.create(name='iPad', price=500.50)
    iphone = Product.create(name='iPhone', price=800.00)
    tv = Product.create(name='TV', price=600.50)

    Product.create(name='product1', price=500.50)
    Product.create(name='product2', price=500.50)
    Product.create(name='product3', price=500.50)




    # Creamos instancias de categorías
    technology = Category.create(name='Technology')  # Renombré 'tecnology' a 'technology' para corregir el error ortográfico
    home = Category.create(name='Home')

    # Relacionamos productos con categorías a través de la tabla intermedia ProductCategory
    ProductCategory.create(product=ipad, category=technology)
    ProductCategory.create(product=iphone, category=technology)
    ProductCategory.create(product=tv, category=technology)

    

    ProductCategory.create(product=tv, category=home)

    # Realizamos un join entre las tablas para obtener los productos con sus categorías
    for product in Product.select(Product.name, Category.name).join(ProductCategory).join(Category,
           on=(ProductCategory.category == Category.id)):

        # Imprimimos el nombre del producto y el nombre de la categoría asociada
        print(product.name, '-', product.productcategory.category.name)  # Se corrige el acceso a las relaciones



    #listar en consola todos los productos que no posean una categoria
    #lefJoin
    products=Product.select(
        Product.name
        ).join(
            ProductCategory,
            peewee.JOIN.LEFT_OUTER
        ).where(
            ProductCategory.id== None
        )
    
    for product in products:
        print(product.name) 