from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LigaFutbol.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^gestionEquipos/', include('gestionEquipos.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
