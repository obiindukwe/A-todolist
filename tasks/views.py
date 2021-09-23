from django.shortcuts import render
from django.http import HttpResponse

from.models import * 


# Create your views here and in addition this is views
def index(request):
	tasks = Task.objects.all()
	


	context = {'tasks':tasks}

	return render(request, 'tasks/list.html', context)




def updateTask(request, pk):
	task =Task.objects.get(id=pk)
	form = TaskForm(instance=task)


	if request.method == "POST":
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('/')



	context = {'form':form}
	return rendeer(request, 'tasks/update_task.html', context)



def deleteTask(request, pk):
	item = Task.objects.get(id=pk)



	if request.metrhod == "POST":
		item.delete()
		return redirect('/')

		context = {'item': item}

		return render(request, 'task/delete.html', context)








	



