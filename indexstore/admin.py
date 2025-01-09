from django.contrib import admin
from .models import Brands, Address, Clients, Clothes, Groupclothes, Sales, Salesclothes, Sedes
from django.utils.html import format_html

# Register your models here.


class BrandsAdmin(admin.ModelAdmin):
    list_display = (
        'idbrand',
        'name',
    )
    ordering= ['idbrand']
    search_fields = ['name']

admin.site.register(Brands, BrandsAdmin)

class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'idaddress',
        'general',
        'name',
        'description',
        'state',
    )
    ordering= ['-state']
    search_fields = ['state','name']
    list_per_page = 10

admin.site.register(Address, AddressAdmin)

class ClothesAdmin(admin.ModelAdmin):
    list_display = (
        'idclothes',
        'idgroupclothes',
        'idsede',
        'size',
        'color',
    )
    ordering= ['idgroupclothes']
    search_fields= ['idclothes','idgroupclothes__idgroupclothes']
    list_per_page= 20

admin.site.register(Clothes, ClothesAdmin)

class GroupclothesAdmin(admin.ModelAdmin):
    list_display = (
        #'idgroupclothes',
        'idbrand',
        'type',
        'description',
        'discount',
        'valuediscount',
        'nameimage',
        #'image',
        'Foto',
        'price',
    )
    ordering= ['-idgroupclothes']
    search_fields = ['type','idbrand__name', 'description', 'nameimage']
    list_per_page = 20
    
    def Foto(self, obj):
        return format_html('<img src={} width="80" />', obj.image.url)

admin.site.register(Groupclothes, GroupclothesAdmin)
                    
class ClientsAdmin(admin.ModelAdmin):
    list_display = (
        'idaddress',
        'fullname',
        'email',
        'cellphonenumber',
        'typeid',
    )
    search_fields= ['fullname','idclient','email']
    list_per_page = 10

admin.site.register(Clients, ClientsAdmin)

class SalesAdmin(admin.ModelAdmin):
    list_display = (
        'idsale',
        'idclient',
        'idseller',
        'state',
        'totalprice',
        'date',
    )
    ordering= ['-idsale']
    search_fields= ['idclient__idclient','state','idseller']
    list_per_page = 15

admin.site.register(Sales, SalesAdmin)

class SalesclothesAdmin(admin.ModelAdmin):
    list_display = (
        'idsalesclothes',
        'idclothes',
        'idsale',
        'dayprice',
    )
    ordering= ['-idsalesclothes']
    search_fields= ['idsalesclothes','idsalesclothes__idsalesclothes']
    list_per_page = 10

admin.site.register(Salesclothes, SalesclothesAdmin)

class SedesAdmin(admin.ModelAdmin):
    list_display = (
        'idsede',
        'name',
        'address',
        'unit',
        'hours',
    )
    ordering= ['-idsede']
    search_fields= ['name','idsede']

admin.site.register(Sedes, SedesAdmin)