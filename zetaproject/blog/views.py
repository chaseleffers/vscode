from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Choice, BlogPost, Question, BlogComment, Project
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_posts'

    def get_queryset(self):
        return BlogPost.objects.filter(PubDate__lte=timezone.now()).order_by('-PubDate')[::]

class PollIndexView(generic.ListView):
    template_name = 'blog/pollindex.html'
    context_object_name = 'latest_questions'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    template_name = 'blog/details.html'
    model = Question


class ResultsView(generic.DetailView):
    template_name = 'blog/results.html'
    model = Question



def homepage(request):
    return render(request, 'blog/homepage.html')


def postbody(request, post_id):
    post = BlogPost.objects.get(pk=post_id)
    return render(request, 'blog/postbody.html', {'post': post})


def portfolio(request):
    portposts = Project.objects.all()
    return render(request, 'blog/portfolio.html', {'portposts': portposts})


def contact(request):
    return render(request, 'blog/contact.html')

def merch(request):
    return render(request, 'blog/merch.html')



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'blog/polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('blog:results', args=(question.id,)))



#def details(request, question_id):
#    try:
#        question = Question.objects.get(pk=question_id)
#    except:
#        raise Http404("Question does not exist.")
#    return render(request, 'polls/details.html', {'question': question})

#def results(request, question_id):
#    try:
#        question = Question.objects.get(pk=question_id)
#    except:
#        raise Http404("Question does not exist.")
#    selected_choice = question.choice_set.get(pk=question_id)
#    return render(request, 'polls/results.html', {'question' : question, 'choice': selected_choice})


#def index(request):
#    latest_questions = Question.objects.order_by('-pub_date')[:5]
#    context = {'latest_questions': latest_questions}
#    return render(request, 'polls/index.html', context)


