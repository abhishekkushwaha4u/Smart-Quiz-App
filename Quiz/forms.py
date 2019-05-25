from django.forms import ModelForm
from Quiz.models import quiz


class QuizForm(ModelForm):
    class Meta:
        model = quiz
        fields = "__all__"