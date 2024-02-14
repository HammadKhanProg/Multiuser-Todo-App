from django.urls import path
from app.views import home,signup,signin,add_todo,signout,delete_todo,update

urlpatterns=[
    path("",home,name="home"),
    path("signup/",signup,name="signup"),
    path("signin/",signin,name="signin"),
    path("add_todo/",add_todo,name="add_todo"),
    path("signout/",signout,name="signout"),
    path("delete_todo/<pk>",delete_todo,name="delete_todo"),
    path("update/<pk>",update,name="update"),
    
]