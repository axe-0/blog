from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime ,timedelta
from .models import Question ,Choice
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    """
    Render the description of the polls on a page.

    This function retrieves the five most recently published questions and passes
    them to the 'poll.html' template along with additional context data
    including the current time, hour, minute, AM/PM, and day of the week.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page.

    Template:
        'poll.html'
    """
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
    """
    Render the poll details to make a chhoice selection and submit the poll.

    This view retrieves a specific question by its ID and renders the 'detail.html'
    template with the question data.

    Args:
        request (HttpRequest): The HTTP request object.
        question_id (int): The ID of the question to display.

    Returns:
        HttpResponse: The rendered HTML page.

    Template:
        'detail.html'

    """
    question = get_object_or_404(Question, pk=question_id)
    return render (request, 'detail.html',{'question':question})
    
@login_required
def results(request, question_id):
    """
    Render the results of the poll after a user votes.

    This view retrieves a specific question by its ID and renders the 'results.html'
    template with the question data.

    Args:
        request (HttpRequest): The HTTP request object.
        question_id (int): The ID of the question for which to display results.

    Returns:
        HttpResponse: The rendered HTML page.

    Template:
        'results.html'
    """
    question = get_object_or_404(Question, pk=question_id)
    return render (request, 'results.html',{'question':question})


def votes(request, question_id):
    """
    This function processes the voting for a specific question.

    This view processes a vote for a specific question by retrieving the selected
    choice from the request and incrementing its vote count. If a choice is not
    selected or doesn't exist, it displays an error message. After processing the
    vote, the user is redirected to the results page for the question.

    Args:
        request (HttpRequest): The HTTP request object.
        question_id (int): The ID of the question for which to process a vote.

    Returns:
        HttpResponseRedirect: A redirection to the 'results' view for the question.

    Template:
        None (Redirects to the 'results' view)
    """
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
