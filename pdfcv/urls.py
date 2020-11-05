from django.urls import path
from . views import accept, web_cv
urlpatterns = [
    path('', accept, name = 'accept'),
    path('<int:id>/', web_cv, name = 'web_cv'),
]
