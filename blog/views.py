from django.shortcuts import render
from django.http import HttpResponse, Http404
from datetime import date

# Create your views here.

my_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Ayush",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And"
                   "I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
                   " Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,"
                   " when an unknown printer took a galley of type and scrambled it to make a type specimen book."

    },

    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Ayush",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code?"
                   " Yep - that's what happened to me yesterday...",
        "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
                   " Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,"
                   " when an unknown printer took a galley of type and scrambled it to make a type specimen book."
    },

    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Ayush",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
                   " Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,"
                   " when an unknown printer took a galley of type and scrambled it to make a type specimen book."
    }

]


def get_date(post):
    return post["date"]


def starting_page(request):
    sorted_posts = sorted(my_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(
        request=request,
        template_name="blog/index.html",
        context={
            "posts": latest_posts
            }
        )


def posts(request):
    return render(
        request=request,
        template_name="blog/all-posts.html",
        context={
            "posts": my_posts
        }
    )


def post_detail(request, slug):
    for post in my_posts:
        if post["slug"] == slug:
            return render(
                request=request,
                template_name="blog/post-detail.html",
                context={
                    "title": post["title"],
                    "image": post["image"],
                    "author": post["author"],
                    "date": post["date"],
                    "content": post["content"]
                }

                )
    raise Http404()
