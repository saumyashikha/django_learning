from django.urls import path
from . import views

urlpatterns = [
    path('feesdj/',views.fee_django),
    path('feespy/',views.fee_python),
]