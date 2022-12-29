from django.conf.urls import url
from BRMApp import views

urlpatterns=[
 url('view_book',views.viewBooks),
 url('edit_book',views.editBook),
 url('delete_book',views.deletebook),
 url('search_book',views.searchBook),
 url('new_book',views.newbook),
 url('^add',views.add),
 url('search',views.search),
 url('edit',views.edit),

]
