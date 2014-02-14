from django.contrib.gis import admin
from models import *
from django.conf import settings

admin.site.register(UserNegocio)
admin.site.register(Barrio)
admin.site.register(Categoria)
admin.site.register(Negocio, admin.OSMGeoAdmin)
admin.site.register(Sucursal, admin.OSMGeoAdmin)

