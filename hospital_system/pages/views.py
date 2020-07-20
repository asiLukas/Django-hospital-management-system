from django.shortcuts import render


def home_view(request, *args, **kwargs):
    context = {
        'object': 'obj'
    }
    return render(request, 'home.html', context)
