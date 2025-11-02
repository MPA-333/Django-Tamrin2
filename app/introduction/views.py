from django.shortcuts import render
from app.introduction.models import Place, TicketPrice
from django.conf import settings


def introView(request):
    return render(request, "introduction/intro.html")


def historyView(request):
    return render(request, "introduction/history.html")


def departmentView(request):
    context = {
        "load_media": settings.MEDIA_URL
    }
    return render(request, "introduction/department.html", context)


def museumView(request):
    context = {
        "load_media": settings.MEDIA_URL
    }
    return render(request, "introduction/museum.html", context)


def gardenView(request):
    context = {
        "load_media": settings.MEDIA_URL
    }
    return render(request, "introduction/garden.html", context)


def visit_wayView(request):
    context = {
        "load_media": settings.MEDIA_URL
    }
    return render(request, "introduction/visit_way.html", context)


def date_rule_priceView(request):
    placeData = Place.objects.all()
    result = []
    
    for item in placeData:
        prices = TicketPrice.objects.filter(place_id=item.id)
        data = [item.id, item.title, item.time, item.date, item.rule, prices]
        result.append(data)

    context = {
        "load_media": settings.MEDIA_URL,
        "data": result,
    }
    return render(request, "introduction/date_rule_price.html", context)
