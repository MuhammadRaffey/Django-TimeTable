from django.urls import path
from . import views

urlpatterns = [
    path('', views.daily_timetable, name='daily_timetable'),
    path('lecture/<int:pk>/detail/', views.lecture_detail, name='lecture_detail'),
    path('create-timetable/', views.create_timetable, name='create_timetable'),
     path('lecture/<int:pk>/update/', views.LectureUpdateView.as_view(), name='lecture_update'),
    path('lecture/<int:pk>/delete/', views.LectureDeleteView.as_view(), name='lecture_delete'),
]
