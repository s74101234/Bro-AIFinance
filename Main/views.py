from django.shortcuts import render

# Create your views here.
def HelloWorld_view(request):
    return render(request, "HelloWorld.html", {
            'data': "Hello World!!", 
    })