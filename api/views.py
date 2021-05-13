import json

from django.http import HttpResponse
from .apidata.home import Homepage


def home(request):
    """
    Representing data for aptstore homepage
    :param request:
    :return:
    """
    hp = Homepage()
    data = hp.get_data()

    return HttpResponse(json.dumps(data))

