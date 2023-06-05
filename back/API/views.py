from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import *
from .models import *
from rest_framework.filters import SearchFilter
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly



class RegistrationAPIView(APIView):
    @action(detail=False, methods=['get'], permission_classes=[IsAdminUser], filter_backends=[SearchFilter],
            search_fields=['username'])
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class OrdersParentView(viewsets.ModelViewSet):
    lookup_field = 'user'
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, user__username=self.kwargs['user'])
        self.check_object_permissions(self.request, obj)
        return obj
    

class OrderAPIView(OrdersParentView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [SearchFilter]
    search_fields = ['user__username']
    lookup_field = 'user'
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]
    def get(self, requset):
        orders = Orders.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def retrieve(self, request, *args, **kwargs):
        username = kwargs.get('user')
        order = get_object_or_404(Orders, user__username__icontains=username)
        serializer = self.get_serializer(order)
        return Response(serializer.data)
    
    def put(self, request, id=None):
        orders = Orders.objects.filter(user__username=request.data['user']).first()
        serializer = OrderSerializer(orders, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return None


class ServicesAPIView(APIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']
    def get(self, requset):
        service = Services.objects.all()
        serializer = ServicesSerializer(service, many=True)
        return Response(serializer.data)

class SuccessOrderAPIView(OrdersParentView):
    queryset = SuccessedOrders.objects.all()
    serializer_class = SuccessOrderSerializer
    filter_backend = [SearchFilter]
    search_fields = ['user__username']
    lookup_field = 'user'
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]
    def post(self, request):
        serializer = SuccessOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def get(self, request):
        sOrder = SuccessedOrders.objects.all()
        serializer = SuccessOrderSerializer(sOrder, many=True)
        return Response(serializer.data)
    
class DetailAPIView(APIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]
    def get(self, request):
        detail = Detail.objects.all()
        serializer = DetailSerializer(detail, many=True)
        return Response(serializer.data)