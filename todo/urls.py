from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('registerUser/', views.registerUser, name='registerUser'),
	path('loginUser/', views.loginUser, name='loginUser'),
	path('logoutUser/', views.logoutUser, name='logoutUser'),
    path('todo/', views.todoView, name='todoView'),
    path('addTodo/', views.addTodo, name='addTodo'),
    path('deleteTodo/<todo_id>/', views.deleteTodo, name='deleteTodo'),
    path('doneTodo/<todo_id>/', views.doneTodo, name='doneTodo'),
    path('undoneTodo/<todo_id>/', views.undoneTodo, name='undoneTodo'),
    path('updateTodo/<todo_id>/', views.updateTodo, name='updateTodo'),


]