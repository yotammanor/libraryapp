from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [ url(r'^items/', include('items.urls', namespace="items")),
                url(r'^admin/',include(admin.site.urls)),
            ]

