from django.urls import path
from .views import candlestick_data, line_chart_data, bar_chart_data, pie_chart_data

urlpatterns = [
    path('candlestick-data/', candlestick_data),
    path('linechart-data/', line_chart_data),
    path('barchart-data/', bar_chart_data),
    path('piechart-data/', pie_chart_data),
]
