from django.shortcuts import render


def home_view(request, name, goal, discrip):
    context = {
        'for': range(1),
        'name': name,
        'goal': goal,
        'discrip': discrip,
    }
    return render(request, 'home.html', context)


def hom1_view(request, name, age, discrip):
    context = {
        'for': range(1),
        'name': name,
        'age': age,
        'discrip': discrip,
    }
    return render(request, 'hom1.html', context)


def hom2_view(request, city, country):
    context = {
        'for': range(1),
        'city': city,
        'country': country,
    }
    return render(request, 'hom2.html', context)


def hom3_view(request, name, goal, discrip, age, city, country):
    context = {
        'for': range(1),
        'name': name,
        'goal': goal,
        'discrip': discrip,
        'age': age,
        'city': city,
        'country': country,
    }
    return render(request, 'hom3.html', context)


def hom4_view(request, name, goal, discrip, age, city, country, trofai):
    context = {
        'for': range(1),
        'name': name,
        'goal': goal,
        'discrip': discrip,
        'age': age,
        'city': city,
        'country': country,
        'trofai': trofai,
    }
    return render(request, 'hom4.html', context)
