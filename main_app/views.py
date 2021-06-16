from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.views import View  
from django.views.generic.base import TemplateView 
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Profile, Exercise, Tracker, Entry, Workout 
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm 
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse 
from django.contrib.auth.models import User
from django.core.paginator import Paginator 

def error_404_view(request, exception):
    return render(request, "404.html")

class Home(TemplateView):
    template_name = "home.html" 

class About(TemplateView):
    template_name = "about.html"

class SignUp(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user) 
            login(request,user)
            return redirect("/entries")
        else:
            return redirect("/")

class Workouts(View):
    def get(self, request):
        all_workouts = Workout.objects.all()
        boxing_exercises = Exercise.objects.filter(category="Boxing")
        yoga_exercises = Exercise.objects.filter(category="Yoga")
        bodyweight_exercises = Exercise.objects.filter(category="Bodyweight")
        context = {"all_workouts": all_workouts, "box_exercises":boxing_exercises, "yoga_exercises":yoga_exercises, "bodyweight_exercises": bodyweight_exercises }
        return render(request, "workouts.html", context)
    
class Workouts_Detail(View):

    def get(self, request, type):        
        if type == "boxing":
            newType = type.capitalize()
            workout = Workout.objects.filter(name="Boxing")[0]
            exercises = Exercise.objects.filter(category="Boxing")
            workoutHTML = "workouts/boxing.html"
            context = {"workout":workout, "exercises":exercises, "type":newType, "workoutHTML":workoutHTML}
            return render(request, "workouts-detail.html", context)

        elif type == "yoga":
            newType = type.capitalize()
            workout = Workout.objects.filter(name="Yoga")[0]
            exercises = Exercise.objects.filter(category="Yoga")
            workoutHTML = "workouts/yoga.html"
            context = {"workout":workout, "exercises":exercises, "type":newType, "workoutHTML":workoutHTML}
            return render(request, "workouts-detail.html", context)

        elif type == "bodyweight":
            newType = type.capitalize()
            workout = Workout.objects.filter(name="Bodyweight")[0]
            exercises = Exercise.objects.filter(category="Bodyweight")
            workoutHTML = "workouts/bodyweight.html"
            context = {"workout":workout, "exercises":exercises, "type":newType, "workoutHTML":workoutHTML}
            return render(request, "workouts-detail.html", context)

class Entries(View):
    def get(self, request):
        usersID = request.user 
        userProfile = Profile.objects.get(user_id=usersID)

        all_entries = Entry.objects.all()

        paginator = Paginator(all_entries, 16)
        page = request.GET.get('pg')
        all_entries = paginator.get_page(page)

        context = {"all_entries":all_entries, "userProfile":userProfile}
        return render(request, 'entries/entries.html', context)

class EntryCreate(CreateView):
    model = Entry 
    fields = ['exercise','set1', 'set2', 'set3', 'set4', 'set5', 'notes', 'tracker']
    template_name = "entries/entry-create.html"
    
    def get_success_url(self):
        return reverse('entry-detail', kwargs={'pk': self.object.pk})


class EntryDetail(DetailView):
    model = Entry 
    template_name = "entries/entry-detail.html"


class EntryUpdate(UpdateView):
    model = Entry 
    fields = ['exercise','set1', 'set2', 'set3', 'set4', 'set5', 'notes', 'tracker']
    template_name = "entries/entry-update.html"

    def get_success_url(self):
        return reverse('entry-detail', kwargs={'pk': self.object.pk})

class EntryDelete(DeleteView):
    model = Entry 
    template_name = "entries/entry-delete.html"
    
    def get_success_url(self):
        return reverse('entries-page')
    

class Tracker_Page(View):
    def get(self, request):
        all_entries = Entry.objects.all()
        context = {"all_entries":all_entries}
        return render(request, 'tracker.html', context)

