#from django.http import Http404  ( because we imported get_object_or_404)
#from django.http import HttpResponse
#from django.template import loader
# from django.shortcuts import render, get_object_or_404
# from .models import Album, Song
#
#
#
# def index(request):
#     all_albums = Album.objects.all()
#     # html = ''
#     # for album in all_albums:
#     #     url = '/music/' + str(album.id) + '/'
#     #     html += '<a href="' + url + '">' +  album.album_title +  '</a><br>'
#
#     #template = loader.get_template('music/index.html')
#
#     context = {'all_albums' : all_albums}
#
#     #return HttpResponse(template.render(context,request))
#     return render(request, 'music/index.html', context)
#
# def detail(request,album_id):
    #return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")
# another way of doing the template is using: from django.shortcuts import render

    #### because we imported get_object_or_404 we can comment out the following lines.
    #try
    #     album= Album.objects.get(id=album_id)
    # except Album.DoesNotExist:
    #     raise Http404("Album Does Not Exist")
    # album = get_object_or_404(Album, id=album_id)
    # return render(request, 'music/detail.html', {'album' : album})

# def favorite(request,album_id):
#     album = get_object_or_404(Album, id=album_id)
#     try:
#         selected_song = album.song_set.get(id=request.POST['song'])
#     except(KeyError, Song.DoesNotExist):
#         return render(request, 'music/detail.html', {
#             'album' : album,
#             'error_message':'Yuou did not select a valid song!'
#         })
#     else:
#         selected_song.is_favorite = True
#         selected_song.save()
#         return render(request, 'music/detail.html', {'album' : album})
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'
    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = [
        'artist',
        'album_title',
        'genre',
        'logo'
    ]
