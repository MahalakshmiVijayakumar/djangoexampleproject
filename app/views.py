from django.shortcuts import render,redirect


def get(request):
    return render(request,"index.html")