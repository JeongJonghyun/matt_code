'''learning_logs URL Configuration'''
from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Page for showing all topics
    path('topics/', views.topics, name='topics'),

    # Page for a single topic and its entries
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    
    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),

    path('about_me/', views.about_me, name='about_me'),

    path('interest_me/', views.interest_me, name='interest_me'),
    

    # # Page for adding a new entry to a topic
    # path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # # Page for editing an existing entry
    # path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
