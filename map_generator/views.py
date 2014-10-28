from django.shortcuts import render

def map_view(request):
    context = {
    }
    return render(request, 'map_generator/map_view.html', context)
