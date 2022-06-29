import django_filters
from .models import EQUIPMENT_DB

class EquipmentFilter(django_filters.FilterSet):
    CHOICES = [
        ('ascending','Ascending'),
        ('descending','Descending'),
    ]
    ordering  = django_filters.ChoiceFilter(label='Ordering', choices= CHOICES , method='filter_by_order')

    class Meta:
        model  = EQUIPMENT_DB
        fields = {
            'BU' : ['icontains'],
            'BL' : ['icontains'],
            'description' : ['icontains'],
            'serial_num' : ['icontains'],
            'temp_location' : ['icontains'],
        }

    def filter_by_order(self,queryset, name, value):
        expression  = 'description' if value == 'ascending' else  '-description'
        return queryset.order_by(expression)
