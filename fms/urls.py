from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name="dashboard"),
    url(r'^documents/$', views.documents, name="documents"),
    url(r'^documents/for_disclosure/$', views.docs_for_disclosure, name="docs_for_disclosure"),
    url(r'^documents/non_disclosure/$', views.docs_not_disclosure, name="docs_not_disclosure"),
    url(r'^documents/exhibits/$', views.docs_exhibits, name="exhibits"),
    url(r'^identities/$', views.main_identities, name="identities"),
    url(r'^identities/add$', views.add_iden, name="add_iden"),
    url(r'^tasks/$', views.tasks, name="tasks"),
    url(r'^notebook/$', views.notebook, name="notebook"),
]
