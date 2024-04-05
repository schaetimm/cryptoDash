from django.shortcuts import render
import requests


# Create your views here.
def home(request):
    try:
        response = requests.get('http://localhost:3000/api/price-feed')
        if response.status_code == 200:
            data = response.json()
        else:
            data = {'error': 'Could not retrieve data from API'}
    except requests.exceptions.RequestException as e:
        data = {'error': str(e)}
    return render(request, 'home.html', {'data': data})
