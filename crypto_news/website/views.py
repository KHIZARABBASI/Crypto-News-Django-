from django.shortcuts import render,HttpResponse, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from .models import CryptoArticalModel, CreateNews, Comment
from .forms import CommentForm,CreateNewsForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    news = CreateNews.objects.all().order_by('-created_at')
    articles = CryptoArticalModel.objects.all().order_by('-created_at')
    # print(news)
    return render(request, 'main_page.html', {'news' : news,'articles':articles })

def home(request):
    posts = CreateNews.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'posts': posts})

def about(request):
    return render(request, 'about_us.html')

def news(request):
    range_for_loop = range(19)
    news = CreateNews.objects.all().order_by('-created_at')
    return render(request, 'news.html', {'range_for_loop': range_for_loop, 'news': news})

def analysis(request):
    range_for_loop = range(19)
    articles = CryptoArticalModel.objects.all().order_by('-created_at')
    return render(request, 'analysis.html', {'range_for_loop': range_for_loop, 'articles':articles })

#----------------------------------------------------------------

def create_news(request):
    if request.method == 'POST':
        form = CreateNewsForm(request.POST, request.FILES)  # Handle file uploads with request.FILES
        if form.is_valid():
            form.save()
            return redirect('news_list')  # Redirect to the news list page after saving
    else:
        form = CreateNewsForm()
    
    return render(request, 'create_news.html', {'form': form})


def news_list(request):
    posts = CreateNews.objects.all().order_by('-created_at')
    return render(request, 'news.html', {"posts" : posts})

def view_full_News(request,pk):
    news_item = get_object_or_404(CreateNews, pk=pk)
    return render(request, 'full_news.html', {'news_item': news_item})

def view_full_Article(request,pk):
    artical_item = get_object_or_404(CryptoArticalModel, pk=pk)
    # comments = artical_item.comments.all()
     # Fetch all comments for the article
    comments = Comment.objects.filter(article=artical_item).order_by('-created_at')  # 
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.article = artical_item
                comment.author = request.user
                comment.save()
                return redirect('view_full_Article', pk=artical_item.pk)
        else:
            return redirect('login')
    else:
        form = CommentForm()

    context = {
        'artical_item': artical_item,
        'comments': comments,
        'form': form,
    }
    return render(request, 'full_artical.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/signup.html', {'form': form})