from django.urls import path

from . import views

app_name = 'notes'
urlpatterns = [
    # Index Page
    path('', views.index, name='index'),
    path('createTeam/', views.CreateTeam.as_view(), name='createTeam'),

    # Settings Page
    path('team/<slug:slug>/settings/', views.settingsView, name='settingsView'),
    path('searchUser/', views.searchUser, name='searchUser'),
    path('team/<slug:slug>/addFM/', views.addFM, name='addFM'),
    path('team/<slug:slug>/addPMember/', views.addPMember, name='addPMember'),
    path('team/<slug:slug>/settings/folder/<int:folderId>/', views.settingsFolder, name='settingsFolder'),
    path('team/<slug:slug>/addFNMember/', views.addFNMember, name='addFNMember'),

    # Layout
    path('team/<slug:slug>/', views.startupView, name='startupView'),
    path('team/<slug:slug>/note/<uuid:uuid>/', views.noteDetail, name='detail'),
    path('updateContent/<int:notebook_id>/', views.updateContent, name='updateContent'),
    path('team/<slug:slug>/addPFN/<int:oid>/', views.addPFN, name='addPFN'),
    path('renamePFN/', views.renamePFN, name='renamePFN'),
]