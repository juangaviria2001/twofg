from django.db import models

# Create your models here.

class Address(models.Model):
    idaddress = models.AutoField('Id Direccion',primary_key=True)
    general = models.CharField('I.General',max_length=255)
    name = models.CharField('Nombre de la direccion',max_length=50)
    description = models.CharField('Descripcion',max_length=150)
    state = models.BooleanField('¿Direccion activa?',default=True)

    class Meta:
        managed = False
        db_table = 'address'
        
    def __str__(self):
        idaddress= self.idaddress
        name= self.name
        return str(idaddress)+ ' - ' + name
    
class Brands(models.Model):
    idbrand = models.AutoField('ID',primary_key=True)
    name = models.CharField('Nombre',max_length=55)

    class Meta:
        managed = False
        db_table = 'brands'
        
    def __str__(self):
        idbrand = self.idbrand
        name = self.name
        return name
    
class Clients(models.Model):
    idclient = models.CharField('Numero de Documento',primary_key=True, max_length=15)
    idaddress = models.ForeignKey(Address ,models.DO_NOTHING, db_column='idaddress')
    fullname = models.CharField('Nombre completo',max_length=80)
    email = models.CharField('Email',max_length=255)
    cellphonenumber = models.CharField('Numero de contacto',max_length=14)
    typeidenum = [
        ("CC", "CC"),
        ("TI", "TI"),
        ("PPE", "PPE"),
        ("CE", "CE"),
    ]
    typeid = models.TextField('Tipo de documento',db_column='typeId', choices=typeidenum)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'clients'

    def __str__(self):
        idclient = self.idclient
        fullname = self.fullname
        return str(idclient)+ ' - ' + fullname

class Clothes(models.Model):
    idclothes = models.AutoField('Referencia unica',primary_key=True)
    idgroupclothes = models.ForeignKey('Groupclothes', models.DO_NOTHING, db_column='idgroupclothes')
    idsede = models.ForeignKey('Sedes', models.DO_NOTHING, db_column='idsede')
    salesClothesSizeEnum = [
        ("XS", "XS"),
        ("S", "S"),
        ("M", "M"),
        ("L", "L"),
        ("XL", "XL"),
        ("XXL", "XXL"),
        ("NA", "NA"),
    ]
    size = models.TextField(choices=salesClothesSizeEnum)  # This field type is a guess.
    color = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'clothes'
        
    def __str__(self):
        idclothes = self.idclothes
        return str(idclothes)

class Groupclothes(models.Model):
    idgroupclothes = models.AutoField('Referencia unica',primary_key=True)
    idbrand = models.ForeignKey(Brands, models.DO_NOTHING, db_column='idbrand')
    GroupclothesEnum = [
        ("Camisa", "Camisa"),
        ("Camibuzo", "Camibuzo"),
        ("Conjunto", "Conjunto"),
        ("Jogger", "Jogger"),
        ("Jean", "Jean"),
        ("Bermuda", "Bermuda"),
        ("Buzo", "Buzo"),
        ("Bolso", "Bolso"),
        ("Chaleco", "Chaleco"),
        ("Abrigo", "Abrigo"),
        ("Sueter", "Sueter"),
        ("Ropa interior para mujer", "Ropa interior para mujer"),
        ("Ropa interior para hombre", "Ropa interior para hombre"),
        ("Gorra", "Gorra"),
        ("Zapatos", "Zapatos"),
        ("Accesorios", "Accesorios") #Acessorios = otros como correas, cadenas, pañoletas, etc.
    ]
    type = models.TextField('Tipo de prenda',choices=GroupclothesEnum)  # This field type is a guess.
    description = models.TextField('Descripcion', max_length=60)
    price = models.BigIntegerField('Precio')
    discount = models.BooleanField('¿Descuento?',default=False)
    valuediscount = models.IntegerField('Valor del decuento',blank=True, null=True,default=0)
    nameimage = models.CharField(max_length=150)
    image = models.ImageField(upload_to='clothes/', )

    class Meta:
        managed = False
        db_table = 'groupclothes'
        
    def __str__(self):
        idgroupclothes = self.idgroupclothes
        type = self.type
        return str(idgroupclothes)

class Sales(models.Model):
    idsale = models.AutoField(primary_key=True)
    idclient = models.ForeignKey(Clients, models.DO_NOTHING, db_column='idclient')
    idseller = models.CharField('Documento vendedor',max_length=11)
    salesStateEnum = [
        ("Pending", "Pending"),
        ("Ok", "Ok"),
        ("Canceled", "Canceled"),
        ("Returned", "Returned"),
    ]
    state = models.TextField('Estado de la venta',choices=salesStateEnum)  # This field type is a guess.
    totalprice = models.BigIntegerField('Valor total')
    date = models.DateField('Fecha de la venta')

    class Meta:
        managed = False
        db_table = 'sales'
        
    def __str__(self):
        idsale = self.idsale
        return str(idsale)


class Salesclothes(models.Model):
    idsalesclothes = models.AutoField(primary_key=True)
    idclothes = models.ForeignKey(Clothes, models.DO_NOTHING, db_column='idclothes')
    idsale = models.ForeignKey(Sales, models.DO_NOTHING, db_column='idsale')
    dayprice = models.BigIntegerField('Precio del dia')

    class Meta:
        managed = False
        db_table = 'salesclothes'
        
    # def __str__(self):
    #     idclothes = self.idclothes
    #     idsale= self.idsale
    #     return str(idclothes)


class Sedes(models.Model):
    idsede = models.AutoField(primary_key=True)
    name = models.CharField(max_length=55)
    address = models.CharField(max_length=100)
    unit = models.CharField(max_length=6)
    hours = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'sedes'

    def __str__(self):
        idsede = self.idsede
        name= self.name
        return str(idsede)+ ' - ' + name
