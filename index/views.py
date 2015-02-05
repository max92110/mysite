from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from index.models import Pages
from django.http import HttpResponse
import datetime
import os

#формируем страницу со списком файлов	
def current_space(request):
    space = os.listdir('/home/max/Torrent/Movies')
    html = "<html><body>It is now %s.</body></html>" % space
    return HttpResponse(html)


#формируем страницу с временем	
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

class IndexView(generic.ListView):
    template_name = 'index/index.html'
    context_object_name = 'latest_page_name_list'
    now = datetime.datetime.now()

    def get_queryset(self):
        """Return the last five published polls."""
        return Pages.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:15]
        # return Poll.objects.order_by('-pub_date')[:5]


#class DetailView(generic.DetailView):
#    model = Poll
#    template_name = 'polls/detail.html'
#
#    def get_queryset(self):
#        return Poll.objects.filter(pub_date__lte=timezone.now())
#
#
#class ResultsView(generic.DetailView):
#    model = Poll
#    template_name = 'polls/results.html'
#
#
#def vote(request, poll_id):
#    p = get_object_or_404(Poll, pk=poll_id)
#    try:
#        selected_choice = p.choice_set.get(pk=request.POST['choice'])
#    except (KeyError, Choice.DoesNotExist):
#        return render(request, 'polls/detail.html', {'poll': p, 'error_message': "You didn't select a choice."})
#    else:
#        selected_choice.votes += 1
#        selected_choice.save()
#        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
