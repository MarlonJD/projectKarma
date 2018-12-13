from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from users.models import MyUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError

from .models import *
from .forms import TeamForm

from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'notes/index.html', 
    {'startups': Startup.objects.filter(employee=request.user), 'founder': Startup.objects.filter(employee=request.user)})

class CreateTeam(LoginRequiredMixin, FormView):
    template_name = 'notes/createTeam.html'
    form_class = TeamForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        name = form.cleaned_data['name']
        perma = form.cleaned_data['perma']

        s = Startup(name=name, perma=perma)
        try:
            s.validate_unique()
        except:
            msg = u"Team with this Perma-Link already exists."
            form._errors["perma"] = form.error_class([msg])
            del form.cleaned_data["perma"]
            raise ValidationError(msg)
        s.save()
        s.employee.add(self.request.user)
        s.founder.add(self.request.user)
        return super().form_valid(form)

@login_required
def startupView(request, slug):
    return render(request, 'notes/notes.html', 
    {'startup': Startup.objects.filter(perma=slug)[:1], 'founder': Startup.objects.get(perma=slug, employee=request.user), 'allNotes': Notebook.objects.filter(employee=request.user)[:3]})

@login_required
def settingsView(request, slug):
    return render(request, 'notes/settings.html', 
    {'startup': Startup.objects.filter(perma=slug)[:1], 'founder': Startup.objects.get(perma=slug, employee=request.user), 'allNotes': Notebook.objects.filter(employee=request.user)[:3]})

@login_required
def noteDetail(request, uuid, slug):
    return render(request, 'notes/detail.html', 
    {'startup': Startup.objects.filter(perma=slug, employee=request.user)[0:1], 'founder': Startup.objects.filter(employee=request.user), 'notebook':Notebook.objects.get(uuid=uuid, employee=request.user), 'allNotes': Notebook.objects.filter(employee=request.user)[:3] })
        
@login_required
def updateContent(request, notebook_id):
    notebook = get_object_or_404(Notebook, pk=notebook_id)
    try:
        sn = Notebook.objects.get(pk=notebook_id)
        sn.content = request.POST['doc']
    except (KeyError, Notebook.DoesNotExist):
        return JsonResponse({'failed': 'There is no content here'})
    else:
        sn.save()
        return JsonResponse({'success': 'Content Updated'})

@login_required
def addPFN(request, oid, slug):
    if oid == 0:
        try:
            startup = Startup.objects.get(employee=request.user, perma=slug)
            name = request.POST['projectName']
            p = Project(name=name, startup=startup, creator=request.user)
        except (KeyError):
            return JsonResponse({'failed': 'There is no content here'})
        else:
            p.save()
            p.employee.add(request.user)
            return JsonResponse({'success': 'Project Add'})
    elif oid == 1:
        try:
            project = Project.objects.get(pk=request.POST['id'])
            f = Folder(name="New Folder", project=project, creator=request.user)
        except (KeyError, Project.DoesNotExist):
            return JsonResponse({'failed': 'There is no content here'})
        else:
            f.save()
            f.employee.add(request.user)
            return JsonResponse({'success': 'Folder Add'})
    elif oid == 2:
        try:
            folder = Folder.objects.get(pk=request.POST['id'])
            n = Notebook(name="New Note", folder=folder, creator=request.user)
        except (KeyError, Project.DoesNotExist):
            return JsonResponse({'failed': 'There is no content here'})
        else:
            n.save()
            n.employee.add(request.user)
            return JsonResponse({'uuid': n.uuid })

@login_required
def renamePFN(request):
    if request.POST['oid'] == "0":
        pfn = Project
    elif request.POST['oid'] == "1":
        pfn = Folder
    elif request.POST['oid'] == "2":
        pfn = Notebook
    else:
        return JsonResponse({'error': 'Something really wrong'})

    try:
        ipfn = int(request.POST["pfn"])
        p = pfn.objects.get(pk=ipfn)
        if request.user == p.creator:
            np = pfn.objects.get(pk=ipfn)
        else:
            return JsonResponse({'permissionError': 'Cannot do that'})
        if request.POST['did'] == "0":
            np.name=request.POST['newName']
        elif request.POST['did'] == "1":
            np.delete()
        else:
            return JsonResponse({'failed': 'Cannot do that'})
    except (KeyError, pfn.DoesNotExist):
        return JsonResponse({'failed': 'There is no content here'})
    else:
        np.save()
        if request.POST['did'] == "1":
            np.delete()
            np.save()
        return JsonResponse({'success': 'Project Renamed'})

# Settings Page
@login_required
def searchUser(request):
    try:
        userEmail = request.POST['email']
        u = MyUser.objects.get(email=userEmail)
    except (KeyError, MyUser.DoesNotExist):
        return JsonResponse({'failed': 'There is no user'})
    else:
        return JsonResponse({'success': 'User Found'})

@login_required
def addFM(request, slug):
    try:
        s = Startup.objects.get(founder=request.user, perma=slug)
        email = request.POST['userMail']
        u = MyUser.objects.get(email=email)
    except (KeyError, Startup.DoesNotExist):
        return JsonResponse({'failed': 1})
    else:
        if request.POST['oid'] == "0":
            s.founder.add(u)
            s.employee.add(u)
        elif request.POST['oid'] == "1":
            s.employee.add(u)
        elif request.POST['oid'] == "2":
            if request.user.email == request.POST['userMail']:
                return JsonResponse({'failed': 0})
            else:
                s.founder.remove(u)
        elif request.POST['oid'] == "3":
            if request.user.email == request.POST['userMail']:
                return JsonResponse({'failed': 0})
            else:
                s.employee.remove(u)
        s.save()
        return JsonResponse({'success': 'Founder/Member Add'})

@login_required
def addPMember(request, slug):
    try:
        s = Startup.objects.get(employee=request.user, perma=slug)
        try:
            Startup.objects.get(founder=request.user, perma=slug)
        except(KeyError, Startup.DoesNotExist):
            p = Project.objects.get(pk=request.POST['pid'], creator=request.user)
        else:
            p = Project.objects.get(pk=request.POST['pid'])
        email = request.POST['userMail']
        u = MyUser.objects.get(email=email)
    except (KeyError, Project.DoesNotExist):
        return JsonResponse({'failed': 'There is no content here'})
    else:
        if request.POST['oid'] == "0":
            p.employee.add(u)
        elif request.POST['oid'] == "1":
            if request.user.email == request.POST['userMail']:
                return JsonResponse({'failed': 0})
            else:
                p.employee.remove(u)
        p.save()
        return JsonResponse({'success': 'Something happened'})

@login_required
def settingsFolder(request, slug, folderId):
    return render(request, 'notes/settingsFolder.html', 
    {'startup': Startup.objects.filter(perma=slug)[:1], 'founder': Startup.objects.get(perma=slug, employee=request.user), 'allNotes': Notebook.objects.filter(employee=request.user)[:3], 'folder': Folder.objects.get(pk=folderId, employee=request.user)})

@login_required
def addFNMember(request, slug):
    if request.POST['oid'] == "0" or request.POST['oid'] == "2":
        fn = Folder
    elif request.POST['oid'] == "1" or request.POST['oid'] == "3":
        fn = Notebook
    try:
        m = fn.objects.get(pk=request.POST['fnid'], employee=request.user)
    except (KeyError, fn.DoesNotExist):
        return JsonResponse({'failed': 'There is no content here'})
    else:
        email = request.POST['userMail']
        u = MyUser.objects.get(email=email)
        if request.POST['oid'] == "2" or request.POST['oid'] == "3":
            if request.user.email == request.POST['userMail']:
                return JsonResponse({'failed': 0})
            else:
                m.employee.remove(u)
        elif request.POST['oid'] == "0" or request.POST['oid'] == "1":
            m.employee.add(u)
        m.save()
        return JsonResponse({'success': 'Something happened'})
