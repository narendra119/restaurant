from django.shortcuts import render
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from .models import Orders
from .serializers import OrdersSerializer


# Create your views here.

class OrdersView(GenericAPIView):

    def get(self, request, *args, **kwargs):

        response = {}
        order_id = request.query_params.get('order_id')
        order_dt = request.query_params.get('order_dt')
        order_status = request.query_params.get('order_status')
        customer_name = request.query_params.get('customer_name')

        filter_query = Q()

        if order_id:
            filter_query = Q(
                order_id = order_id
            )

        if order_dt:
            filter_query.add(
                Q(
                    order_dt = order_dt
                ),
                Q.AND
            )
        if customer_name:
            filter_query.add(
                Q(
                    customer_id__customer_name__icontains = customer_name
                ),
                Q.AND
            )
        
        if order_status:
            filter_query.add(
                Q(
                    order_status = order_status
                ),
                Q.AND
            )

        filter_data = Orders.objects.all().filter(
            filter_query
        )

        count = filter_data.count()
        serializer = OrdersSerializer(filter_data, many=True)

        response['count'] = count
        response['data'] = serializer.data
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)
