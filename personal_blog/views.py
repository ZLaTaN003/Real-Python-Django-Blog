from django.shortcuts import render
from django.urls import reverse
from django.http import Http404,HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .models import Post,Category,Comments
from . forms import CommentForm

# Create your views here.

def blog_index(request):
    """
    Home Page with all blog posts till date
    """
    all_posts = Post.objects.all().order_by("-created")
    ctx = {"all_posts":all_posts}
    return render(request,"personal_blog/index.html",context=ctx)




def blog_detail(request,postid):
    """
    Details for a post
    """
    post = Post.objects.get(id=postid)
    comments = Comments.objects.filter(post=post)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comments(commented_by=form.cleaned_data["author"],body=form.cleaned_data["body"],post=post)
            comment.save()
            return HttpResponseRedirect(request.path_info)

    ctx = {"post":post,"comments":comments,"form":form}
    return render(request,"personal_blog/blog_details.html",context=ctx)

def blog_categories(request,category):
    """Blog posts arranged as categories"""

    post_of_a_category = Post.objects.filter(category__name=category)
   

    ctx = {
        "category": category,
        "posts": post_of_a_category,
    }
    return render(request, "personal_blog/category.html", context=ctx)