from django.shortcuts import render
from django.http import HttpResponse
import requests
from datetime import date

# Create your views here.

def home(request):
	if request.method == 'POST':
		from_curr = request.POST.get('from')
		print(from_curr)
		to_curr = request.POST.get('to')
		print(to_curr)
		amt = float(request.POST.get('amt'))
		print(amt)

		ans=0

		today = date.today()
		today = today.strftime("%Y-%m-%d")
		
		#base = EUR
		url = "http://data.fixer.io/api/"+today
		access_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
		querystring = {"format":"json","access_key":access_key}

		response = requests.request("GET", url, params=querystring)

		response = response.json()	
		print(response)
		rates = response['rates']
		b1 = float(rates[from_curr])
		b2 = float(rates[to_curr])
		print(b1,b2)

		euros = amt/b1
		euros = euros*b2
		ans=round(euros,2)

		context={
			'ans':ans
		}

		return render(request, 'currency/home.html',context)

	return render(request, 'currency/home.html')
