from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime ,timedelta
from .models import Question ,Choice
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    now = datetime.now()
    new_time = now + timedelta(hours=2)
    current_hour = new_time.strftime("%I")
    current_minute = now.strftime("%M")
    am_pm = now.strftime("%p")
    day_of_week = now.strftime("%A")
    
    context = {
        'latest_question_list' : latest_question_list,
        'current_hour': current_hour,
        'current_minute': current_minute,
        'am_pm': am_pm,
        'day_of_week': day_of_week,
        }
    return render (request, 'poll.html',context)

@login_required
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render (request, 'detail.html',{'question':question})
    
@login_required
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render (request, 'results.html',{'question':question})


def votes(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
       selected_choice = question.choice_set.get(pk=request.POST['choice'])
    
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'polls/detail.html', {'question': question,
        'error_message': "You didn't select a choice."
        })
   
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(
            reverse('polls:results', args=(question_id,))

            )
