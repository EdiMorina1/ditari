from django.shortcuts import render, redirect
from .forms import lenda,profesori,klasa,nxenesi,nota,mungesa,oraMesimore
from django.contrib import messages

def register(request):
	if request.method == "POST":
		form = lenda(request.POST)
		if form.is_valid():
			form.save()
			emri=form.cleaned_data.get('emri')
			return redirect("regjistro-lenden")
	else:
		form=lenda()
	return render(request,'home/home.html',{'form':form})
def regjistroProfesorin(request):
	if request.method == 'POST':
		form = profesori(request.POST)
		if form.is_valid():
			form.save()
			return redirect('Regjistro-Profin')
	else:
		form = profesori()
	return render(request,'home/profesori.html',{'form':form})
def regjistroKlasen(request):
	if request.method == 'POST':
		form = klasa(request.POST)
		if form.is_valid():
			form.save()
			return redirect('regjistro-klasen')
	else:
		form = klasa()
	return render(request,'home/klasa.html',{'form':form})
def regjistroNxenesin(request):
	if request.method == 'POST':
		form = nxenesi(request.POST)
		if form.is_valid():
			form.save()
			return redirect('Regjistro - nxenesin')
	else:
		form = nxenesi()
	return render(request,'home/nxenesi.html',{'form':form})
def regjistroNoten(request):
	if request.method == 'POST':
		form = nota(request.POST)
		if form.is_valid():
			form.save()
			return redirect('regjistro-noten')
	else:
		form = nota()
	return render(request,'home/notat.html',{'form':form})
def regjistroMungesen(request):
	if request.method == 'POST':
		form = mungesa(request.POST)
		if form.is_valid():
			form.save()
			return redirect('regjistro-noten')
	else:
		form = mungesa()
	return render(request,'home/mungesat.html',{'form':form})
def regjistroOrenMesimore(request):
	if request.method == 'POST':
		form = oraMesimore(request.POST)
		if form.is_valid():
			form.save()
			return redirect('regjistro-noten')
	else:
		form = oraMesimore()
	return render(request,'home/oraMesimore.html',{'form':form})

	
	
# Create your views here.
