from django.urls import path, include
from community import views as my_view
urlpatterns = [
    path('t1', my_view.test),

]
