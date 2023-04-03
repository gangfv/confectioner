from django.views import generic
from rest_framework import generics

from home.models import Card, Review, Work
from home.serializer import NumberSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


class HomeListView(generic.ListView):
    model = Card
    context_object_name = 'Cards'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        context['Reviews'] = Review.objects.all()
        context['Works'] = Work.objects.all()
        return context


class NumberCreteApi(generics.CreateAPIView):
    serializer_class = NumberSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
