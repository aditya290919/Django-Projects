from django.urls import path
from chatapp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('<slug:slug>',views.chatroom, name='chatroom'),
]