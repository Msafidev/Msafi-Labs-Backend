from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Welcome to the Msafi Labs API",
        "status": "running"
    })