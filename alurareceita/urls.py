from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

import receitas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('receitas.urls'))
]
