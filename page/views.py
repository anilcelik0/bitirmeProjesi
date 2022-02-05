from django.shortcuts import render
from django.shortcuts import redirect
from page.models import yer
import requests, json

# Create your views here.
def index(request):
    if yer.objects.first():
        yerData = yer.objects.first().yerVeri
        neredeData = yer.objects.first().neredeVeri

        url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query="+yerData+"%20in%20"+neredeData+"&key=YourApiKey"

        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        a = json.loads(response.text)
        names = []
        adresss = []
        lats = []
        lngs = []
        ratings = []
        for b in a["results"]:
            adress = b['formatted_address']
            adresss.append(adress)
            name = b['name']
            names.append(name)
            location = b['geometry']["location"]
            lat = location["lat"]
            lat = str(lat).split(",")
            lat = lat[0]
            lats.append(lat)
            lng = location["lng"]
            lng = str(lng).split(",")
            lng = lng[0]
            lngs.append(lng)
            b["name"]
            rating = b["rating"]
            ratings.append(rating)

        liste = zip(names,adresss,lats,lngs,ratings)
            
        
        context = {
            "yer":yerData,
            "liste":liste
        }
        return render(request,'index.html',context)
    return render(request,'index.html')


def direct(request):
    if request.method == "POST":
        yerPost = request.POST["yer"]
        neredePost = request.POST["nerede"]
        a=yer.objects.all()
        a.delete()
        yer.objects.create(yerVeri=yerPost,neredeVeri=neredePost)
        return redirect('/index/')
    return render(request,'direct.html') 