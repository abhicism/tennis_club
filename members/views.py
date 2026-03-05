from django.http import HttpResponse #import httpresponse class to send an http response back to the browser
from django.template import loader #import template loader to manually load an html template
from .models import Member #imports the member model from the current app's model.py
#basically we have used member, template and httpresponse class
def members(request): #here member is the view function name
  mymembers = Member.objects.all().values()
  #fetches all records from the member table in the database
  #.values() converts each record into a dictionary instead of a model object
  # Example output:
    # [{'id': 1, 'firstname': 'John', 'lastname': 'Doe'}, ...]
  template = loader.get_template('all_members.html')
  #loads the html template file named (all_members.html)
  context = {
    #context is a dict that sends data from the view to the template
    #more like a bridge between frontend and backend
    'mymembers': mymembers,
    #leftside : name used in template , rightside : variable created in view
  }
  #create a context dictionary
  #this sends data to the template, in the template, we can access it using :
  #{% for x in mymembers %}
  
  return HttpResponse(template.render(context, request))
#renders the template with the provided context data.
# Wraps the rendered HTML inside HttpResponse
#send the final html response back to the browser
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
  
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))