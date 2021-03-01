from django.http import JsonResponse
from django.shortcuts import render
from . models import page
from django.views.generic import View
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.express as px

x_data = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
y_data = [x**0.5 for x in x_data]
plot_div = plot([Scatter(x=x_data, y=y_data,
					mode='lines', name='test',
					opacity=0.8, marker_color='green')],
			output_type='div')

def index(request, pagename):
	pagename = '/' + pagename
	pg = page.objects.get(permalink=pagename)
	context = {
		'title': pg.title,
		'content': pg.bodytext,
		'last_updated': pg.update_date,
		'page_list': page.objects.all(),
		'plot_div': plot_div

	}
	return render(request, 'dashboard/page.html', context)

