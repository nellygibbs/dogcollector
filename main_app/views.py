from django.shortcuts import render
from django.http import HttpResponse

#fake database
class Dog:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

#List of Dogs
dogs = [
    Dog('Jazzy', 'Yorkie', 'heaven sent', 5),
    Dog('Blacky', 'Unknown', 'worst nightmare', 13),
    Dog('Storm', 'Pit Bull', 'ball of energy', 1),
]        

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', {'dogs': dogs})   