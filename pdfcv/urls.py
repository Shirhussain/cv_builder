from django.urls import path
from . views import accept, web_cv, cv_list
urlpatterns = [
    path('', accept, name = 'accept'),
    path('list', cv_list, name = 'cv_list'),
    path('<int:id>/', web_cv, name = 'web_cv'),
]
