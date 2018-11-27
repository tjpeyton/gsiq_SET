from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from .models import Client
from .forms import LoginForm
from gophish import Gophish
from gophish.models import *
from django.contrib import messages

def index(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            #process the data
            campid = form.cleaned_data['camp_id']
            camppass = form.cleaned_data['camp_pass']
            try:
                campaign = Client.objects.get(cid=campid)
                company = campaign.company

                if campaign.getCampaignPass() == camppass:
                    return results(request, campid, company)

                else:
                    messages.info(request, 'Your password is incorrect')
                    form = LoginForm()

            except Client.DoesNotExist:
                messages.info(request, 'Your credentials are incorrect')
                form = LoginForm()
    else:
        form = LoginForm()

    return render(request, 'phish/index.html', {'form': form})

def results(request, cid, company):

    template = loader.get_template('phish/results.html')
    api_key = '39c59f79333e74e64ed533abbdcf6d888dec827018878a4a0eaaa2abdc12e0d1'
    api = Gophish(api_key, host='https://18.234.146.143:3333', verify=False)
    info = api.campaigns.results(campaign_id=cid).results
    printable = []

    for result in info:
        printable.append(result.as_dict())

    context = {
        'printable': printable,
        'company': company,
    }

    return HttpResponse(template.render(context, request))
