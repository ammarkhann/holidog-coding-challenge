from django.shortcuts import render
import requests
import json
# Create your views here.



def home(request):

	response = json.loads(requests.get("https://dog.ceo/api/breeds/list/all").content)
	dog_breed_list = []
	for key,val in response['message'].items():
		if response['message'][key]:
			for nested_breed_types in response['message'][key]:
				dog_breed_list.append(key+"-"+nested_breed_types)
		else:
			dog_breed_list.append(key)

	context = {
		"dog_breed_list" : dog_breed_list,
	}

	template = "home.html"

	return render(request,template,context)



def breed_image(request,slug):

	response = json.loads(requests.get("https://dog.ceo/api/breed/"+slug+"/images/random").content)	
	context = {
		"breed_image": response['message']

	}

	template = "breed_image.html"

	return render(request,template ,context)
