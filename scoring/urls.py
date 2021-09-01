from django.urls import path
from .views import *

urlpatterns = [
    path('', ScoreList.as_view()),
    path('highscore/', HighScoreList.as_view()),
    path('ind_score/', UserHighScoreList.as_view()),
    path('score_flag/', VerifyFlag.as_view()),
    path('<slug:slug>/', UserScore.as_view()),
    
]
