from django.http import HttpResponse #import httpresponse class to send an http response back to the browser
from django.template import loader #import template loader to manually load an html template
from .models import Member #imports the member model from the current app's model.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Member
from .serializers import MemberSerializer
#basically we have used member, template and httpresponse class
def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
#renders the template with the provided context data.
# Wraps the rendered HTML inside HttpResponse
#send the final html response back to the browser
#view function that handles request to display one specific member by their ID.  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
 #view function for the homepage 
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render()) 
# Define a view function named 'testing'
# This function handles HTTP requests sent to this route
def testing(request):
  mydata = Member.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
  return HttpResponse(template.render(context, request))

#filter the data based on the first name and return the result to the template
def testing1(request):
  mydata = Member.objects.filter(firstname='Emil').values()
  template = loader.get_template('template1.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))

#fetch only the first name of all members and return it to the template
def testing2(request):
  mydata = Member.objects.values_list('firstname')
  template = loader.get_template('template2.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))

#filter the data based on the last name and id and return the result to the template
"""
AND
The filter() method takes the arguments as **kwargs (keyword arguments), 
so you can filter on more than one field by separating them by a comma.
"""

def testing3(request):
  mydata = Member.objects.filter(lastname ='Refsnes', id=2).values()
  template = loader.get_template('kwargsfilt.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))

"""
OR
To return records where firstname is Emil or firstname is Tobias,
(meaning: returning records that matches either query, not necessarily both).
We can use multiple filter() methods, separated by a pipe | character. 
"""
def testing4(request):
  mydata = Member.objects.filter(firstname='Emil').values() | Member.objects.filter(firstname='Tobias').values()
  template = loader.get_template('template3.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
"""
field lookups
Use the __startswith keyword:
"""
def testing5(request):
  mydata = Member.objects.filter(firstname__startswith='L').values()
  template = loader.get_template('template4.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
"""
order_by() method is used to sort the result in ascending or descending order.
here we order the result by the firstname.
"""
def testing6(request):
  mydata = Member.objects.all().order_by('firstname').values()
  template = loader.get_template('template5.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))

"""
descending order :
By default, the result is sorted ascending (the lowest value first),
to change the direction to descending (the highest value first),
use the minus sign (NOT), - in front of the field name:
"""
def testing7(request):
  mydata = Member.objects.all().order_by('-firstname').values()
  template = loader.get_template('template6.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
"""
multiple order bys:
to order by more than one field,
separate the field names by a comma in the order_by() method:
"""
def testing8(request):
  #lastname is ordered in ascending order and id is ordered in descending order
  mydata = Member.objects.all().order_by('lastname', '-id').values()
  template = loader.get_template('template7.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))

#basic testing template view for test
def testing9(request):
  template = loader.get_template('basictemplate.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))

#global static files testing
def testing10(request):
  template = loader.get_template('globalstatic.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
  }
  return HttpResponse(template.render(context, request))

@api_view(['GET','POST'])
def members_list(request):

    if request.method == 'GET':
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)