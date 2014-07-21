from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'twitterClone.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'twitter_app.views.index'),
    url(r'^login$','twitter_app.views.login_view'),
    url(r'^logout$','twitter_app.views.logout_view'),
    url(r'^signup$','twitter_app.views.signup'),
    url(r'^tweets$','twitter_app.views.public'),
    url(r'^submit$','twitter_app.views.submit'),
)
