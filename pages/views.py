from django.shortcuts import render

# Create your views here.
def homePageView(request):
    return HttpResponse("{Message-Hello World!}")