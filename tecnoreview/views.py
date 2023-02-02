from django.shortcuts import render

def home(request):
    return render(
        request=request,
        template_name='tecnoreview/home.html',
    )

def about(request):
    return render(
        request=request,
        template_name='tecnoreview/about.html',
    )