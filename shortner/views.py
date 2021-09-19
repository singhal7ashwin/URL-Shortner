from django.shortcuts import render, redirect
import uuid
import json
from .models import Url
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def create(request):
    # print("Hit create endpoint")
    if request.method == 'POST':
        # import pdb
        # pdb.set_trace()
        url = None
        if 'link' in request.POST:
            url = request.POST['link']
        else:
            urlJson = json.loads(request.body)
            if 'link' in urlJson:
                url = urlJson['link']
        shorten_id = str(uuid.uuid4())[:5]
        new_shorten = Url(original_url=url,shortened_url=shorten_id)
        new_shorten.save()
        return HttpResponse(shorten_id)

def handleShortenedUrl(request,pk):
    shorten_details = Url.objects.get(shortened_url=pk)
    return redirect(shorten_details.original_url)


