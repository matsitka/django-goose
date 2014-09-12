from django.shortcuts import render

from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect, HttpResponse, QueryDict
from django.shortcuts import render, render_to_response, get_object_or_404, redirect


from models import Article
from forms import ArticleForm

#message
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# Create your views here.
def home(request): #home


    articles = Article.objects.all().order_by('-created_at')


    return render(request, 'index.html', {
        'all_articles': articles,
    })

def article_id(request, link_random):


    try:

        article = Article.objects.filter(random=link_random).select_related().get()
    except Article.DoesNotExist:
        raise Http404


    return render(request, 'article.html', {
        'article_details': article,

    })

def add_article(request):


    if request.method == "POST":


        form = ArticleForm(data=request.POST)

        #filter user folder
        #usr = User.get_by_id(uid)
        #form.folder = Folder.objects.filter(author=usr).order_by('sort_order')

        if form.is_valid():

            messages.success(request, 'Your new article was saved!')

            #form.errors['success'] = 'Saved'

            article = form.save(commit=False)


            article.save()



            #return the last random object created
            last_random = Article.objects.values_list('random', flat=True).order_by('-created_at')[:1]
            #this returns [u'5eXB612345']

            #return the random sequence only to a strng format 5eXB6
            new_random = str(last_random)[3:13]




            return redirect('/article/%s' % new_random)



    else:
        form = ArticleForm()



    return render_to_response(
        'add_article.html',
        {
            'article_form': form,
            #'success': success,

        },
        context_instance=RequestContext(request)
    )
