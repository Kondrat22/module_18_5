from django.contrib import admin
from django.urls import path
from task2.views import index, index2
from task4.views import platform, shop, bag
from task5.views import sign_up_by_html, sign_up_by_django


urlpatterns = [
    path('admin/', admin.site.urls),
    path('func', index), path('class', index2.as_view()),
    path('', platform), path('shop', shop), path('bag', bag),
    path('reg', sign_up_by_html),
    path('reg_c', sign_up_by_django)
]