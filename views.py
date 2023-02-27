from django.shortcuts import render
from .models import Todo 
from django.shortcuts import redirect

# Create your views here.
def index(request):
    todo = Todo.objects.all() # get all todos
    if request.method == 'POST': # if post request
        new_todo = Todo(title=request.POST['title']) # create new todo
        new_todo.save() # save the new todo to the database
        return redirect('/') # redirect to home page
    return render(request,'index.html', {'todos':todo}) # render the home page

def delete(request,pk): # delete a todo
    todo = Todo.objects.get(id=pk) # get the todo
    todo.delete() # delete the todo
    return redirect('/') 