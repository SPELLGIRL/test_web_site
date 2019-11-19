from django.urls import path
from mainapp.views import FilteredMainView

app_name = 'mainapp'

urlpatterns = [
    path('', FilteredMainView.as_view(), name="main"),
]
