from django.shortcuts import render
from django.views import View
import requests
import json


class EvaluateView(View):

	def get(self, request, *args, **kwargs):

		text1 = "teacher's answer"
		text2 = "student's answer"
		token = "27cfd17d8c6a46758b2559c2e6df3388"
		marks = 50	#set by teacher

		url = "https://api.dandelion.eu/datatxt/sim/v1/?text1=%s&text2=%s&token=%s" %(text1.replace(" ", "%20"), text2.replace(" ", "%20"), token)

		r = requests.get(url).json()

		context = {
			"similarity": r["similarity"],
			"marks": round(0.5 * round(r["similarity"] * marks / 0.5) , 1),
		}

		return render(request, "evaluate.html", context)
