from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect
from .models import Fantasy
from .forms import FantasyForm
from django.contrib import messages


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):  # new
    template_name = "about.html"


def form_page(request):
    if request.method == "POST":
        fantasy_form = FantasyForm(request.POST, request.FILES)
        if fantasy_form.is_valid():
            instance = fantasy_form.save(commit=False)
            instance.student = request.user
            instance.save()
            messages.success(request, 'Your choices were successfully added!')
        else:
            messages.error(request, 'Error saving form')

        return redirect("home")
    fantasy_form = FantasyForm()
    choices = Fantasy.objects.all()
    return render(request=request, template_name="form.html",
                  context={'fantasy_form': fantasy_form, 'choices': choices})


class FantasyView(ListView):
    model = Fantasy
