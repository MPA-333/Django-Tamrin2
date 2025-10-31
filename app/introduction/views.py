from django.shortcuts import render


def introView(request):
    return render(request, "introduction/intro.html")


def historyView(request):
    return render(request, "introduction/history.html")
