from django.http import HttpResponse
from django.template import loader
from .models import Member

from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import MemberSerializer
from .permissions import IsOwnerOrAdmin
from rest_framework.throttling import ScopedRateThrottle


# ================== API (ViewSet - FULLY UPDATED) ==================
class MemberViewSet(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    # ✅ Show only logged-in user's data
    def get_queryset(self):
        return Member.objects.filter(owner=self.request.user)

    # ✅ ADD FILTERING + SEARCH + ORDERING
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    # ✅ Exact filtering
    filterset_fields = ['firstname', 'lastname']

    # ✅ Search (partial match)
    search_fields = ['firstname', 'lastname']

    # ✅ Ordering
    ordering_fields = ['firstname', 'lastname', 'id']

    # ✅ Auto assign owner
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# ================== API (Function-based) ==================
@api_view(['GET', 'POST'])
def members_list(request):
    if request.method == 'GET':
        members = Member.objects.filter(owner=request.user)
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def member_detail(request, id):
    try:
        member = Member.objects.get(id=id, owner=request.user)
    except Member.DoesNotExist:
        return Response({"error": "Member not found"}, status=404)

    if request.method == 'GET':
        serializer = MemberSerializer(member)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MemberSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        member.delete()
        return Response({"message": "Member deleted"}, status=204)


# ================== TEMPLATE VIEWS ==================

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    return HttpResponse(template.render({'mymembers': mymembers}, request))


def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    return HttpResponse(template.render({'mymember': mymember}, request))


def testing(request):
    template = loader.get_template('template.html')
    return HttpResponse(template.render({'mymembers': Member.objects.all().values()}, request))


def testing1(request):
    template = loader.get_template('template1.html')
    return HttpResponse(template.render({'mymembers': Member.objects.filter(firstname='Emil').values()}, request))


def testing2(request):
    template = loader.get_template('template2.html')
    return HttpResponse(template.render({'mymembers': Member.objects.values_list('firstname')}, request))


def testing3(request):
    template = loader.get_template('kwargsfilt.html')
    return HttpResponse(template.render({'mymembers': Member.objects.filter(lastname='Refsnes', id=2).values()}, request))


def testing4(request):
    data = Member.objects.filter(firstname='Emil').values() | Member.objects.filter(firstname='Tobias').values()
    template = loader.get_template('template3.html')
    return HttpResponse(template.render({'mymembers': data}, request))


def testing5(request):
    template = loader.get_template('template4.html')
    return HttpResponse(template.render({'mymembers': Member.objects.filter(firstname__startswith='L').values()}, request))


def testing6(request):
    template = loader.get_template('template5.html')
    return HttpResponse(template.render({'mymembers': Member.objects.all().order_by('firstname').values()}, request))


def testing7(request):
    template = loader.get_template('template6.html')
    return HttpResponse(template.render({'mymembers': Member.objects.all().order_by('-firstname').values()}, request))


def testing8(request):
    template = loader.get_template('template7.html')
    return HttpResponse(template.render({'mymembers': Member.objects.all().order_by('lastname', '-id').values()}, request))


def testing9(request):
    template = loader.get_template('basictemplate.html')
    return HttpResponse(template.render({'fruits': ['Apple', 'Banana', 'Cherry']}, request))


def testing10(request):
    template = loader.get_template('globalstatic.html')
    return HttpResponse(template.render({'fruits': ['Apple', 'Banana', 'Cherry']}, request))