from django.urls import path,include
from . import views

app_name='portfolioapp'


urlpatterns = [
    path('logme/',views.logme,name='logme'),
    path('', views.PortfolioView.as_view(), name='homeview'),
    path('aboutme/', views.AboutMeView.as_view(),name='aboutme'),
    path('aboutme/<int:pk>/edit', views.AboutMeForm.as_view(),name='aboutmeupdate'),
    path('projects/', views.Projects.as_view(),name='projectview'),
    path('<int:pk>/edit', views.PortfolioUpdateView.as_view(), name='portfolioupdate'),
    ]
