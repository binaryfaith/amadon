from django.shortcuts import render, redirect


def index(request):
    return render(request, "amadon/index.html")

def process(request):
    try:
        request.session['counter']
    except KeyError:
        request.session['counter'] = 0
    
    request.session['counter'] += int(request.POST['quantity'])
    request.session.modified = True
    

    price = {
        "1" : 100,
        "2" : 88.88,
        "3" : 29.99
    }

    quantity = request.POST['quantity']
    product = request.POST['product']
    request.session["total"] = int(quantity)*price[product]

    if "total_purchase" not in request.session:
        request.session["total_purchase"] = request.session["total"]
    else:
        request.session["total"] += request.session["total"]

    return redirect("/checkout") 

def checkout(request):
    return render(request,"amadon/checkout.html")





    
    
