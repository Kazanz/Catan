from django.shortcuts import render

from map_generator.forms import MapSettingsForm
from map_generator.utils import CatanMap



def map_view(request):
    form = MapSettingsForm(request.POST or None)
    catan_map = CatanMap(players=4, version="original", board_size=19)
    assert 0
    context = {
        'form': form,
        'catan_map': catan_map
    }
    return render(request, 'map_generator/map_view.html', context)
