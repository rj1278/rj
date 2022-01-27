from unicodedata import name
from django.urls import path
from . import views

urlpatterns=[
    path('signup',views.admin_signup,name='signup'),
    path('signin',views.login_view,name='login'),
    path('book_view',views.book_view,name='bookview'),
    path('',views.student_view,name='home'),
    path('delete_book',views.del_book,name='delete_book'),
    path('update_book',views.update_book,name='update_book')

]