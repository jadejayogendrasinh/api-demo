
from . import views
from django.urls import path
# from .views import CartItemViews

urlpatterns = [
    path('upload/cards/', views.CardView.as_view(), name='uploadcards'),
    path('upload/gifs/', views.GIFView.as_view(), name='gifs'),
    path('add/quotes/', views.QuotesView.as_view(), name='quotes'),
    path('getcards/', views.CardView.as_view(), name='getcards'),
    path('getgifs/', views.GIFView.as_view(), name='gifs'),
    path('getquotes/', views.QuotesView.as_view(), name='quotes'),
    path('getcards/<int:pk>', views.CardsDetail.as_view(), name='cards'),
    path('getgifs/<int:pk>', views.GIFsDetail.as_view(), name='gifs'),
]
