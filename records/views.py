from rest_framework import viewsets, filters
from .models import Record
from .serializers import RecordSerializer
from users.permissions import RolePermission


class RecordViewSet(viewsets.ModelViewSet):
    serializer_class = RecordSerializer
    permission_classes = [RolePermission]

    filter_backends = [filters.SearchFilter]
    search_fields = ['category', 'note']

    def get_queryset(self):
        queryset = Record.objects.all().order_by('-date')

        category = self.request.query_params.get('category')
        record_type = self.request.query_params.get('type')
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        if category:
            queryset = queryset.filter(category=category)

        if record_type:
            queryset = queryset.filter(type=record_type)

        if start_date and end_date:
            queryset = queryset.filter(date__range=[start_date, end_date])

        if start_date and not end_date:
            queryset = queryset.filter(date__gte=start_date)
        
        if end_date and not start_date:
            queryset = queryset.filter(date__lte=end_date)
        
        return queryset
