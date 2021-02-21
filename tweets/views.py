from django.shortcuts import render


def home_view(request, *args, **kwargs):
    context = {}

    return render(request, "tweets/index.html", context)
