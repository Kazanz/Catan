import json

from django.shortcuts import render

from map_generator.forms import MapSettingsForm
from map_generator.utils import CatanMap



def map_view(request):
    form = MapSettingsForm(request.POST or None)
    catan_map = CatanMap(players=4, version="original")
    land, numbers, width = catan_map.randomize()

    context = {
        'form': form,
        'catan_map': catan_map,
        'land': json.dumps(land),
        'numbers': json.dumps(numbers),
        'width': json.dumps(width),
    }
    return render(request, 'map_generator/map_view.html', context)
