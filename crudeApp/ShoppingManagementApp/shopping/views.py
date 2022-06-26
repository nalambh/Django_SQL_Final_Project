from django.shortcuts import render, redirect
from shopping.forms import ShoppingForm
from shopping.models import Shopping


# Create Shopping:

def createShopping(request):
    if request.method == "POST":
        form = ShoppingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/show')
            pass
    else:
        form = ShoppingForm()
    return render(request, "index.html", {'form': form})


def show(request):
    shoppings = Shopping.objects.all()
    return render(request, "show.html", {"shoppings": shoppings})


def edit(request, id):
    shopping = Shopping.objects.get(id=id)
    return render(request, "edit.html", {"shopping": shopping})


def update(request, id):
    shopping = Shopping.objects.get(id=id)
    form = ShoppingForm(request.POST, instance=shopping)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, "edit.html", {"shopping": shopping})


def delete(request, id):
    shopping = Shopping.objects.get(id=id)
    shopping.delete()
    return redirect('/show')

