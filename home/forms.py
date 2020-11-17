from django import forms
from home.models import lenda,profesori,klasa,nxenesi,nota,mungesa,oraMesimore

class lenda(forms.ModelForm):
	class Meta:
		model = lenda
		fields = ['emriLenda']
class profesori(forms.ModelForm):
	class Meta:
		model = profesori
		fields = ['emriProfi','mbiemriProfi','nrPersonalProfi','emailProfi','pas','idLenda']
class klasa(forms.ModelForm):
	class Meta:
		model = klasa
		fields = ['emriKlasa','paralelja','vitiShkollor','idProfi']
class nxenesi(forms.ModelForm):
	class Meta:
		model = nxenesi
		fields = ['emriNx','mbiemriNx','emriPrindit','NrTelPr','idKlasa']
class nota(forms.ModelForm):
	class Meta:
		model = nota
		fields = ['vlera','idNx','idProfesori','idLenda','IdPerioda']
class mungesa(forms.ModelForm):
	class Meta:
		model = mungesa
		fields = ['idNx','idProfesori','dataNota','ora','arsyeja']
class oraMesimore(forms.ModelForm):
	class Meta:
		model = oraMesimore
		fields = ['idProfesori','idLenda','dataOres','titulliOres','pershkrimiOres','nrOra']
		
			
	
		
		
	