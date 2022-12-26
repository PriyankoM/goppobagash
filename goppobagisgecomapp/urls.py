from django.urls import path
from .views.login import Login , logout
from .views.index import Index,store
urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('login/',Login.as_view(),name="loginPage"),
    path('store', store , name='store')
    # path('orders', auth_middleware(OrderView.as_view()), name='orders')
]


