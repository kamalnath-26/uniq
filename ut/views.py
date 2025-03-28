from django.shortcuts import*
from ut.models import uniq 

# Create your views here.




def home(request):
    t=uniq.objects.all()
    return render(request,"home.html",{"z":t})



def store(request):
    
    if request.method=="POST":
        a=request.POST["pn"]
        b=request.POST["pc"]
        c=request.POST["p"]
        d=request.POST["g"]
        e=request.POST["f"]

        table=uniq(PRODUCT_NAME=a,PRODUCT_CODE=b,PRICE=c,GST=d,FOODPRODECT=e)
        table.save()
        return redirect("home")

    return render(request,"store.html")



def delete_app(request,id):
    d=uniq.objects.get(id=id)
    d.delete()
    return redirect('home')




def update(request,id):
    d=uniq.objects.filter(id=id)
    if request.method=="POST":
        for d in d:
            
            rn=request.POST['pn']
            sn=request.POST['pc']
            fn=request.POST['p']
            gn=request.POST['g']
            db=request.POST['f']

            d.PRODUCT_NAME=rn
            d.PRODUCT_CODE=sn
            d.PRICE=fn
            d.GST=gn
            d.FOODPRODECT=db
            d.save()
            return redirect("home")


    
    return  render(request,"update.html",{"z":d})

