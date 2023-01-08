from django.urls import path
from .views.login import Login , logout
from .views.index import Index,store,ourbooks
from .views.aboutus import aboutus
urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('login/',Login.as_view(),name="loginPage"),
    path('store', store , name='store'),
    path('ourbooks',ourbooks,name="ourbook"),
    path('aboutus',aboutus,name="aboutus")
    # path('orders', auth_middleware(OrderView.as_view()), name='orders')
]


