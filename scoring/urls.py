from django.urls import path
from .views import *

urlpatterns = [
    path('', ListUserFlags.as_view()),
    path('highscore/', HighScoreList.as_view()),
    path('ind_score/', IndividualScore.as_view()),
    path('score_flag/', VerifyFlag.as_view()),
    path('flags/', ListFlags.as_view()),
    path('checkregister/', CheckRegister.as_view()),
    path('flags/<int:id>/', UpdateFlags.as_view()),
    path('verify/<str:name>/', VerifyChallenge.as_view()),
    path('<slug:slug>/', IndividualUserFlags.as_view()),
]
