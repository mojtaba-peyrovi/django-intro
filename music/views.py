from django.http import Http404
#from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    # html = ''
    # for album in all_albums:
    #     url = '/music/' + str(album.id) + '/'
    #     html += '<a href="' + url + '">' +  album.album_title +  '</a><br>'

    #template = loader.get_template('music/index.html')

    context = {'all_albums' : all_albums}

    #return HttpResponse(template.render(context,request))
    return render(request, 'music/index.html', context)

def detail(request,album_id):
    #return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")
# another way of doing the template is using: from django.shortcuts import render
    try:
        album= Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        raise Http404("Album Does Not Exist")
    return render(request, 'music/detail.html', {'album' : album})
