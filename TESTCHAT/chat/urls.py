from django.urls import path
from chat.views import index


from . import views

urlpatterns = [ 
    path('' , index , name='index'), 
    # path("<str:room_name>/", views.room, name="room"),
    path("<str:room_name>/", views.tetris, name="room"),
    # path("<str:room_name>/", views.room_tetris, name="room"),
    
]
