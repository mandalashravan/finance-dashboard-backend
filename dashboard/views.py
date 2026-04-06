# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from records.models import Record
from django.db.models import Sum


class DashboardSummaryView(APIView):

    def get(self, request):
        income = Record.objects.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
        expense = Record.objects.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0

        category_data = Record.objects.values('category').annotate(total=Sum('amount'))
        recent = Record.objects.order_by('-date')[:5].values()

        return Response({
            "total_income": income,
            "total_expense": expense,
            "net_balance": income - expense,
            "category_totals": category_data,
            "recent_activity": recent
        })

