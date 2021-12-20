import json

from django.http import HttpResponse
from .apidata.home import Homepage
from .apidata.details import DetailsPage
from .apidata.teaser import Teaser


def home(request):
    """
    Representing data for aptstore homepage
    :param request:
    :return:
    """

    hp = Homepage(get_region(request))
    data = hp.get_data()

    return HttpResponse(json.dumps(data))


def teaser(request):
    """
    Teaser apps view
    :param request:
    :return:
    """
    tp = Teaser(get_region(request))
    data = tp.get_data()

    return HttpResponse(json.dumps(data))


def details(request, appid):
    """
    Representing data for aptstore details page
    :param request:
    :return:
    """
    dp = DetailsPage(appid, get_region(request))
    data = dp.get_app_data()

    return HttpResponse(json.dumps(data))


def get_region(request):
    region_string = request.META['HTTP_ACCEPT_LANGUAGE']
    region_string_parts = region_string.split(',')
    region = region_string_parts[0]
    region = region.replace('-', '_')

    return region
