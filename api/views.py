import json

from django.http import HttpResponse
from .apidata.home import Homepage
from .apidata.details import DetailsPage


def home(request):
    """
    Representing data for aptstore homepage
    :param request:
    :return:
    """
    hp = Homepage()
    data = hp.get_data()

    return HttpResponse(json.dumps(data))


def details(request, appid):
    """
    Representing data for aptstore details page
    :param request:
    :return:
    """
    dp = DetailsPage(appid)
    data = dp.get_app_data()

    return HttpResponse(json.dumps(data))
