from django.conf.urls import patterns, include, url
from links.views import UserProfileDetailView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from news.views import LinkListView

urlpatterns = patterns('',
	url(r'^$', LinkListView.as_view(), name='home'),
	url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name="login"),
	url(r'^logout/$', 'django.contrib.auth.views.logout_then_login',name="logout"),

	url(r'^users/(?P<slug>\w+)/$', UserProfileDetailView.as_view(), name="profile"),
    # Examples:
    # url(r'^$', 'hacker.views.home', name='home'),
    # url(r'^hacker/', include('hacker.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
