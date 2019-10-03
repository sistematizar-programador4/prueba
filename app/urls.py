from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'students', StudentView, basename='student')
router.register(r'professors', ProfessorView, basename='professor')
router.register(r'scores', ScoreView, basename='scores')
urlpatterns = router.urls
urlpatterns += [
    path('students_list/', StudentListView.as_view()),
    path('students_list/<int:pk>', SingleStudentView.as_view()),
    path('professors_list/', ProfessorListView.as_view()),
    path('professors_list/<int:pk>', SingleProfessorView.as_view()),
    path('score_list/', ScoreListView.as_view()),
    path('score_list/<int:pk>', SingleScoreView.as_view()),
]