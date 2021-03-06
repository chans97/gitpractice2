from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Content
from .forms import ContentForm, ContentEditForm
from django.shortcuts import get_object_or_404

# Create your views here.


def home(request):
    posts = Content.objects.all().order_by('-pub_date')
    return render(request, "mydiary/home.html", {"posts_list": posts})


def new(request):
    if request.method == "POST":
        form = ContentForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("home")
    else:
        form = ContentForm()
    return render(request, "mydiary/new.html", {"form": form})


def detail(request, pk):
    post = get_object_or_404(Content, pk=pk)
    return render(request, "mydiary/detail.html", {"post": post})



def edit(request, pk):
    post = get_object_or_404(Content, pk=pk)
    if request.method == "POST":
        form = ContentEditForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("detail", pk=post.pk)
    else:
        form = ContentEditForm(instance=post)
        return render(request, "mydiary/edit.html", {"post":post, "form": form})


def delete(request, pk):
    post = get_object_or_404(Content, pk=pk)
    post.delete()
    return redirect("home")

def deleteensure(request, pk):
    post = get_object_or_404(Content, pk=pk)
    return render(request, "mydiary/deleteensure.html", {"post": post})
