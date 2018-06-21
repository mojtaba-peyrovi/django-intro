django:
part2- making a project
terminal:  django-admin startproject <project_name>
mange.py never edit it.
url.py   => its like routes/web.php in laravel.  registering routes.
==
to boot the server:  navigate to prject folder:  python manage.py runserver
---------------------
part3:  make an app in the project:   in terminal :  python manage.py startapp <app_name>
---------------------
part4:  
admin.py contains all the admin functionalities
models.py where we can add models, database migrations, schema, etc.
----------------------------------

part 9:
in order to run the shell( like Tinker in Laravel)  we just have to get into the app folder then say; Python manage.py shell.
when we want to work with database we need to import the models like this:  from music.models import Album, Song (these 2 are the models we made before)
- when we want to see objects we have stored in models we need to say;   Album.objects.all( )
- in order to add objects to the model ==> a = Album(field1="value1", field2="value2", ..........)      and at the end we say   a.save( )
-if you want to see any object of the record we can say;  a.title  and it returns it.
------------------------
part 10:
in order for us to define any specific representation of the model in command line we need to add it to the model as a method like this:

def __str__(sef):
     return self.<field_name1> + <field_name2> + ....  

if we want to see any specific value record based on a criteria we can use <model_name>.filter(<field_name> criteria)
it doesnt accept <> we can use =  
also we can say;   Album.filter(artist__startswith='Taylor') then it returns Taylor Swift and her album
----------------------------
part 11:
we need to make a superuser (admin)     easily we say:   python manage.py createsuperuser
and then we login to the server /admin and login. then we access the backend.
in order to add the models we made in terminal to the backend we just need to say:
          from django.contrib import admin
          from .models import Album
          admin.site.register(Album);
----------------------------
part 12,13 :
whenever we want to make a new view, we first need to add a new url:
   we go to the app we want (here is music) then open urls.py
   inside urls.py inside the urlpatterns array we say:   url(r'^$',<view_name>, name=<route_name>
r: means regular expression     ^ (carrot means the beginning)   $ (means the end)
in order to tell django that it is the id and has to be used in the view later, we say:
url(r'^(?P<album_id>[0-9]+)/$')  ==> [0-9]+  means integer between 0-9 and the the plus means any bigger integer.
that <album_id> we registered with the url now we can inject it into the view function.
 -----------------------------------
part14:
 templates:
anytime we want to work with templates we need to say:
from django.template import loader
then we need to make a directory called templates under the app directory and inside of it we make a
new folder the same name as the app.
now, inside this inner folder we can make our index,html
then in views we say: template = loader.get_template('music/index.html')   music refers to the inner app
folder we made inside templates folder.
then we need to define a dictionary and pass all variables we defined and will name is context.
and when we say return HttpResponse(template.render(context, request))
blade templating convention;
  {% for album in all_albums %}
      <li class="list-group-item"><a href="/music/{{ album.id }}">{{ album.album_title }}</a></li>
  {% endfor %}
so similar to laravel.
when we want to know if there is any record in the database using blade;
{% if all_albums %}   then we can add {%else%} and the rest is like laravel.
--------------------------------
part 15:
another way of doing the templating:
form django.shortcuts import render

then we say return render(request, 'music/index.html', context)
--------------------------------------

pat16:
 in order to get 404 error for worng music id numbers we can import it to views.py as:
from django.httml import Http44
then we need to write a try-except error handling and in except part we say:
raise Http404("<message_we_want_to_display")
---------------------------
part 17:
after making each model we need to define the string representation of the records by writing a method like this:
edf __str__(self):
      return self.<the_field_we_want>  e.g. return self.song_title
IMPORTANT: everytime we add/remove/change any field in a model we need to migrate the models again.
for adding a song we can do it from terminal by instantiating a Song() object, adding fields one by one and at the end save().
---------------------------
part18:
because we have made a one to many relationship between album and songs we can access songs through the album.
we can say: album1.song_set.all() ====> this shows all the songs inside album1
anoher way to add a song is:   album1.song_set.create(<pass_all_key_value_pairs_here>)
- if we want to know how many songs are saved in an album:
album1.song_set.count()
--------------------------
part19:
making the details page is similar to Laravel. nothing new.

---------------------------
part20:
we can make this url dynamic: /music/{{ album.id }}
like this:  in the urls page we name each route and now we can use those names to make the routes in html dynamic.
{% url 'detail' album.id %}     -->detail is the name of the route we put at urls.py.   and album.id is the dynamic part of the url.

--------------------------
part 21 :
we need to namespace our app on the top of urls.py for each app like this:
app_name = 'music'    and anytim we want to link to a specific route in html we can mention like this:    <app_nam>:<route_name>
e.g. music:detail
- there is a shortcut for doing the try/except we made for detail function at views.py, to return 404 message there is a pre-built function
called get_object_or_404() and we just need to pass the model name and the primary key.
-----------------------
part 22:
we want to add favorites radio button to star songs. we added a boolean field for Song model and run migrate:
1) python manage.py makemigrations <app_name>  e.g. python manage.py makemigrations music
2) python manage.py migrate
IMPORTANT: anytime we make any changes on the database we need to restart the server.
-------------------------
part 23:
the way we do error message flashing in django is like this:
{% if error_message %}
     <p class="alert alert-danger"></p>
 {% endif %}
- like laravel we need to have action of the form pointing out the url we defined in urls.py.
- like laravel we have to add csrf token  for any form ===> {% csrf_token %}
- in django anytime inside for loop we need to have the auto increment object we can fetch it like this:  {{ forloop.counter }}
 - we can add a start next to the songs with simply checking if their is_favorite field is true or not. like this:
 {% if song.is_favorite %}  

---------------------------
part 24:
we need to add favorite() function to the view because we already made the form, and it mentioned favorite function. (like controller methods in laravel)
first we need to get the selected_song id from request and then we need to change the is_favorite attribute of it to True.
then we save() it.
-----------------------------
part 25:
in order to add styles, images, etc. inside the app folder we add a folder called static, inside static we make a folder same name as the
app name and inside that folder we can have css, js, images, etc. folders.
- in order to reference the stylesheet inside static folder:
     {% load staticfiles %}
         <link rel="stylesheet" type="text/css" href="{% static 'music/style.css' %}">

- we added navbar and linked the brand to homepage.
<a class="navbar-brand" href="{% url 'music:index' %}">My-Playlist</a>
-------------------------------
