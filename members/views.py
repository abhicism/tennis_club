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
#view function that handles request to display one specific member by their ID.  
def details(request, id):
  #fetch single member record from the database where the ID matches the URL parameter.
  mymember = Member.objects.get(id=id)
  #load the "details.html" template file.
  template = loader.get_template('details.html')
  #create context dictionary to pass member data to the template
  context = {
    'mymember': mymember, #this variable will be used inside the template
  }
  #render the template with the member data and return the response
  return HttpResponse(template.render(context, request))
 #view function for the homepage 
def main(request):
  #load the template "main.html"
  template = loader.get_template('main.html')
  #render the template and return the response
  return HttpResponse(template.render())
# Define a view function named 'testing'
# This function handles HTTP requests sent to this route
def testing(request):
  template = loader.get_template('template.html')
  #context ={
    # You can add any data you want to pass to the template here
    # For example: 'message': 'Hello, World!'
  # }
  return HttpResponse(template.render()) 