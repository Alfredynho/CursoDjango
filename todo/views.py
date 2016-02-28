from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from todo.models import Todo, TodoArticulo
# Create your views here.

def index(request):
	todo = Todo.objects.all() # select * from Todo
	return render_to_response('index.html',
								RequestContext(request.locals()))


def ver_detalle(request, id):
		#ver2 = Todo.objects.filter(id = id) esta es otra forma
	ver = get_object_or_404(Todo,id=id)
	return render_to_response('todo/ver.html',
								RequestContext(request.locals()))
