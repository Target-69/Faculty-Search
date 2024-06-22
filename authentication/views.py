from django.shortcuts import render
from .models import Faculty
from .forms import FacultySearchForm
def home(request):
    return render(request, 'home.html')

def faculty_search(request):
    if request.method == 'POST':
        form = FacultySearchForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            results = Faculty.objects.filter(name__icontains=search_query)
            return render(request, 'search_results.html', {'results': results})
    else:
        form = FacultySearchForm()
    return render(request, 'search_form.html', {'form': form})

def contact(request):
    return render(request, 'contact.html')


