from django.shortcuts import render

def home(request):
    # Make sure the path reflects the actual structure
    return render(request, 'portfolio_app/index.html')



