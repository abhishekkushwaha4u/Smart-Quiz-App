from django.urls import path
from Quiz.views import student_code_for_next_quiz as code,createQuiz

app_name = "quiz"

urlpatterns = [
    path('quiz/',createQuiz, name="createQuiz"),
    #path('quiz_created', quizCreated, name="quiz_created"),
]
