from django.contrib import admin
from .models import Brands
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

# class StocksAdmin(admin.ModelAdmin):
#     list_display = (
#         'Id_Brands',
#         'Tipe',
#         'Name',
#         'NumberOf',
#         'Price',
#         'Foto',
#         'BarCode',
#         #RUTA 'Img',
#         'Sales',
#     )
#     def Foto(self, obj):
#         return format_html('<img src={} width="80" />', obj.Img.url)
#     ordering= ['Tipe']
#     search_fields= ['Name','Tipe']

# admin.site.register(Stocks, StocksAdmin)

# class InfoStocksAdmin(admin.ModelAdmin):
#     list_display = (
#         #'id',
#         'Barcode_Stocks',
#         'IDescription',
#     )
#     search_fields = ['Barcode_Stocks__BarCode']

# admin.site.register(InfoStocks, InfoStocksAdmin)
                    
# class CustomersAdmin(admin.ModelAdmin):
#     list_display = (
#         'FullName',
#         'IdCustomer',
#         'ContactNumber',
#         'Email',
#         'Address',
#     )
#     search_fields= ['FullName','IdCustomer','Email']

# admin.site.register(Customers, CustomersAdmin)

# class OrdersAdmin(admin.ModelAdmin):
#     list_display = (
#         'Id_Brands',
#         'Id_Stocks',
#         'IdCustomer',
#         'LState',
#         'NProducts',
#         'ODescription',
#     )
#     ordering= ['id']
#     search_fields= ['IdCustomer__IdCustomer','Id_Stocks__BarCode','LState']

# admin.site.register(Orders, OrdersAdmin)
