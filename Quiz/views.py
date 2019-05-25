from django.shortcuts import render
import random
import string
from django.contrib import messages
from django.http import HttpResponse
from users.models import Profile
from Quiz.forms import QuizForm
# Create your views here.



def student_code_for_next_quiz(request):
    message = randomString(codelength)
    return message

def randomString(stringLength=6):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    number = random.randint(10 ** (10-stringLength), 10 ** (11-stringLength)-1)
    k = ''.join(random.choice(letters) for i in range(stringLength))
    return k+str(number)

def createQuiz(request):
    if request.user.is_authenticated:
        newUser = Profile.objects.get(email=request.user.email)
        if newUser:
            if newUser.role=="teacher":
                if request.method == "POST":
                    form = QuizForm(request.POST)
                    if form.is_valid():
                        form.save()
                        return HttpResponse("Success!")
                    else:
                        print(form.errors) 
                else:
                    form = QuizForm()
                    return render(request, 'Quiz/createQuiz.html', {'form': form})
            else:
                return HttpResponse("Response to students denied!")
        else:
            return redirect("/accounts/login")
                            
