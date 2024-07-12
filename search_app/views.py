from django.shortcuts import render
from .models import Dish
from .forms import DishSearchForm

def search_dishes(request):
    form = DishSearchForm()
    results = []
    if 'query' in request.GET:
        form = DishSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Dish.objects.filter(name__icontains=query)
    return render(request, 'search_app/search_results.html', {'form': form, 'results': results})
