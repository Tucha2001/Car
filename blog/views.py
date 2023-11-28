from django.shortcuts import render, redirect, get_object_or_404

from .models import Blog, Feedback, Callback, Car, Description
from .forms import CallbackForm


def index(request):
    blogs = Blog.objects.all()
    feedbacks = Feedback.objects.all()
    cars = Car.objects.all()
    descriptions = Description.objects.all()
    if request.method == "POST":
        form = CallbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CallbackForm()

    context = {
        'blog_list': blogs,
        'feedback_list': feedbacks,
        'form': form,
        'car_list': cars,
        'description_list': descriptions,

    }

    return render(request, 'blog/index.html', context)


def about(request):
    return render(request, 'blog/about.html')


def cars(request):
    cars = Car.objects.all()
    context = {
        'car_list': cars
    }
    return render(request, 'blog/car.html', context=context)


def blog(request):
    blogs = Blog.objects.all()
    context = {
        'blog_list': blogs
    }
    return render(request, 'blog/blog.html', context=context)


def contact_us(request):
    return render(request, 'blog/contact.html')


def detail_car(request, car_id):
    cars = get_object_or_404(Car, pk=car_id)
    context = {
        'car_list': cars
    }
    return render(request, 'blog/detail_car.html', context)


def description_car(request):
    descriptions = Description.objects.all()
    context = {
        'description_list': descriptions
    }
    return render(request, 'blog/description_car.html', context)
