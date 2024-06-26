from django.urls import path
from . import views
urlpatterns = [

    path('',views.home,name='home'),
    path('addagency/',views.addagency,name='addagency'),
    path('removeagency/<int:id>',views.removeagency,name='removeagency'),
    path('updateagency/<int:id>',views.updateagency,name='updateagency'),
    path('eligible/',views.eligible,name='eligible'),
    path('documents/',views.documents,name='documents'),
    path('agencies/',views.agencies,name='agencies'),
]
