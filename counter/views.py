from django.shortcuts import render
import json
import requests

def home(request):
    import json
    import requests
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        recipe_api_url = 'https://api.api-ninjas.com/v1/recipe?query='
        api_request = requests.get(
            api_url + query, headers={'X-Api-Key': 'alOCu5d2fF0eLYbMZRWyaQ==BAO0MMlok68gPZKT'})
        recipe_api_request = requests.get(
            recipe_api_url + query, headers={'X-Api-Key': 'alOCu5d2fF0eLYbMZRWyaQ==BAO0MMlok68gPZKT'})
        try:
            api = json.loads(api_request.content)
            recipe_api = json.loads(recipe_api_request.content)
            print(api_request.content)
            print(recipe_api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            recipe_api = "oops! There was an error"
            print(e)
        return render(request, 'home.html', {'api': api, 'recipe_api': recipe_api})
    else:
        return render(request, 'home.html', {'query': 'Enter a valid query'})
