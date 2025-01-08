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

admin.site.register(Clothes, ClothesAdmin)

class GroupclothesAdmin(admin.ModelAdmin):
    list_display = (
        #'idgroupclothes',
        'idbrand',
        'type',
        'description',
        'price',
        'discount',
        'valuediscount',
        'image',
    )
    ordering= ['-idgroupclothes']
    search_fields = ['type','idbrand__name', 'description']

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