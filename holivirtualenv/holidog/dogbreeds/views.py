from django.shortcuts import render
import requests
import json
# Create your views here.



def home(request):

	response = json.loads(requests.get("https://dog.ceo/api/breeds/list/all").content)
	print (response['message'])
	dog_breed_list = []
	for key,val in response['message'].items():
		if response['message'][key]:
			print (key,val , len(response['message'][key]))
			for x in response['message'][key]:
				dog_breed_list.append(key+"-"+x)
		else:
			print (key,val)
			dog_breed_list.append(key)

	context = {
		"dog_breed_list" : dog_breed_list,
	}

	return render(request,"home.html",context)
