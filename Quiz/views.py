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
    # if request.method == "POST":
    #     name = request.POST.get('name')
    #     created_by = request.POST.get('owner')
    #     date_of_starting = request.POST.get('start_date')
    #     date_of_ending = request.POST.get('end_date')
    #     no_of_questions = request.POST.get('no_of_questions')
    #     duration = request.POST.get('duration')
    #     time_of_starting = request.POST.get('starting_time')
    #     time_of_ending = request.POST.get('ending_time')
    if request.method == "POST":
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success!")
        else:
            print(form.errors) #To see the form errors in the console. 
    else:
        form = QuizForm()
        # If form is not valid, this would re-render inputtest.html with the errors in the form.
        return render(request, 'Quiz/createQuiz.html', {'form': form})
                
