# libraries are imported
import os
# rendering the template using render
from django.shortcuts import render
# this will be used to get the path of the media folder from settings
from django.conf import settings
# for storing the file in the desired folder, FileSystemStorage is used  
from django.core.files.storage import FileSystemStorage
# this will handle MultiValueDictKeyError using try and except
from django.utils.datastructures import MultiValueDictKeyError
# using class from models.py
from . models import file_storage
from django.templatetags.static import static


# def index(request):
#     path = settings.MEDIA_ROOT
#     print(path)
#     img_list = os.listdir(path)
#     context = {'images' : img_list}
#     return render(request, "Eridium/Eridium.html", context)
	
def file_storage_to_db(request):
	file_path = os.path.join(settings.CONTENT_DIR, 'assets/img')

	if request.method == 'POST':
		try:
			myFile = request.FILES['myFile']
		except MultiValueDictKeyError:
			print("Error.......")
			myFile = "None"
		fs = FileSystemStorage(location=file_path)	
		filename = fs.save(myFile.name, myFile)
		file_url = fs.url(filename)
		file_information = file_storage()
		file_information.file_name = myFile.name
		file_information.file_url = file_url 
		file_information.save()
		
		context = {
					'filename': myFile.name, 
					'file_url': file_url
				  }
		predict(context['filename'])

		for name in os.listdir(file_path):
			if name not in ['favicon.png', 'LibrusLogo.png', context['filename'], 'bak.svg']:
				p = "/".join([file_path,name])
				os.remove(p)

		Eridium = '/img/' + context['filename']
		return render(request, 'Eridium.html', {'context': Eridium})
	else:
		return render(request, 'Eridium.html')		

def predict(name):
	pass