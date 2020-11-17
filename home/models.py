from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
class lenda (models.Model):
	emriLenda= models.CharField(max_length=50)
	def __str__(self):
		return self.emriLenda

class userpuntori(models.Model):
	user = models.OneToOneField(
		User,
		on_delete = models.CASCADE,
		primary_key = True,
		related_name = 'b'
		)
	idLenda=models.ForeignKey(lenda, on_delete=models.CASCADE)
	pozita = models.IntegerField(default=1)
	def __str__(self):
		return str(self.pozita)



		
class profesori (models.Model):
    emriProfi=models.CharField(max_length=50)
    mbiemriProfi=models.CharField(max_length=50)
    nrPersonalProfi=models.CharField(max_length=50)
    emailProfi= models.EmailField(max_length=50)
    pas= models.CharField(max_length=50)
    idLenda=models.ForeignKey(lenda, on_delete=models.CASCADE)
    def __str__(self):
    	return self.emriProfi+" "+self.mbiemriProfi
class klasa (models.Model):
	emriKlasa=models.CharField(max_length=10)
	paralelja=models.CharField(max_length=10)
	vitiShkollor=models.DateTimeField(default= datetime.now)
	idProfi=models.ForeignKey(User, on_delete=models.CASCADE,default = "Zgjedh Profesorin")
	def __str__(self):
		return self.emriKlasa+"/"+self.paralelja
class nxenesi(models.Model):
	emriNx=models.CharField(max_length=50)
	mbiemriNx=models.CharField(max_length=50)
	emriPrindit=models.CharField(max_length=50)
	NrTelPr= models.CharField(max_length=50)
	idKlasa=models.ForeignKey(klasa,on_delete=models.CASCADE)
	def __str__(self):
		return self.emriNx+" "+self.mbiemriNx
class perioda(models.Model):
	emriPerioda=models.CharField(max_length=10)
	def __str__(self):
		return self.emriPerioda
class nota(models.Model):
	vlera=models.IntegerField(default=0)
	idNx =models.ForeignKey(nxenesi,on_delete=models.CASCADE)
	idProfesori=models.ForeignKey(User,on_delete=models.CASCADE)
	idLenda=models.ForeignKey(lenda,on_delete=models.CASCADE, default=1)
	IdPerioda=models.ForeignKey(perioda,on_delete=models.CASCADE, default=1)
	def __str__(self):
		vlera = str(self.vlera)
		return vlera
class notaPerfundimtare(models.Model):
	idNx =models.ForeignKey(nxenesi,on_delete=models.CASCADE)
	idProfesori=models.ForeignKey(User,on_delete=models.CASCADE)
	idLenda=models.ForeignKey(lenda,on_delete=models.CASCADE, default=1)
	vleraNota =models.IntegerField(default=0)
	dataNota=models.DateTimeField(default=datetime.now)
	def __str__(self):
		nota=str(self.vlera)
		return nota
class mungesa(models.Model):
	idNx =models.ForeignKey(nxenesi,on_delete=models.CASCADE)
	idProfesori=models.ForeignKey(User,on_delete=models.CASCADE)
	dataNota=models.DateTimeField(default=datetime.now)
	ora=models.IntegerField(default=0)
	arsyeja =models.BooleanField()
	
	def __str__(self):
		ora=str(self.ora)

		idNx=str(self.idNx)
		a= str(self.arsyeja)

		if (a== "True"):
		
			a = " Me arsye"
		else:
		
			a = "Pa arsye"
		return idNx+",ora: "+ora+",Arsyeshmeria "+a
class oraMesimore(models.Model):
	idProfesori=models.ForeignKey(User,on_delete=models.CASCADE)
	idLenda=models.ForeignKey(lenda,on_delete=models.CASCADE, default=1)
	dataOres=models.DateTimeField(default=datetime.now)
	titulliOres=models.CharField(max_length=50)
	pershkrimiOres=models.TextField(max_length=255)
	nrOra=models.IntegerField()
	def __str__(self):
		return str(self.idProfesori)+", Titulli: "+self.titulliOres

		
	


	

	


		
	
		