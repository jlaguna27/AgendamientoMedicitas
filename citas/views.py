from django.shortcuts import render
from django.views.generic import ListView, FormView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Citamedica, Profile, Paciente, Eps, Medico, User
from .forms import Formucitamedica, Formueps, Formumedico, Formupaciente, Formuprofile, Formuuser, Formuuseredit

# Create your views here.
#View
class Viewcitamedica(PermissionRequiredMixin, ListView):
    permission_required = 'citas.view_citamedica'
    login_url = 'login'
    model = Citamedica
    template_name = 'viewcitamedica.html'

    def get_queryset(self):
        queryset = super(Viewcitamedica, self).get_queryset()

        if self.request.user.groups.filter(name="Medico").exists():
            queryset = queryset.filter(medico__user=self.request.user)
        if self.request.user.groups.filter(name="Paciente").exists():
            queryset = queryset.filter(paciente__user=self.request.user)

        return queryset


class Viewprofile(PermissionRequiredMixin, ListView):
    permission_required = 'citas.view_profile'
    login_url = 'login'
    model = Profile
    template_name = 'viewprofile.html'


class Viewpaciente(PermissionRequiredMixin, ListView):
    permission_required = 'citas.view_paciente'
    login_url = 'login'
    model = Paciente
    template_name = 'viewpaciente.html'

    def get_queryset(self):
        queryset = super(Viewpaciente, self).get_queryset()

        if self.request.user.groups.filter(name="Paciente").exists():
            queryset = queryset.filter(user=self.request.user)

        return queryset


class Vieweps(PermissionRequiredMixin, ListView):
    permission_required = 'citas.view_eps'
    login_url = 'login'
    model = Eps
    template_name = 'vieweps.html'

    def get_queryset(self):
        queryset = super(Vieweps, self).get_queryset()

        if self.request.user.groups.filter(name="Paciente").exists():
            queryset = queryset.filter(paciente__user = self.request.user)
        return queryset

class Viewmedico(PermissionRequiredMixin, ListView):
    permission_required = 'citas.view_medico'
    login_url = 'login'
    model = Medico
    template_name = 'viewmedico.html'

class Viewuser(PermissionRequiredMixin, ListView):
    permission_required = 'auth.view_user'
    login_url = 'login'
    model = User
    template_name = 'viewuser.html'

#Add

class Addcitamedica(PermissionRequiredMixin, FormView):
    permission_required = 'citas.add_citamedica'
    login_url = 'login'
    form_class = Formucitamedica
    template_name = 'addcitamedica.html'
    success_url = '/viewcita'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Addeps(PermissionRequiredMixin, FormView):
    permission_required = 'citas.add_eps'
    login_url = 'login'
    form_class = Formueps
    template_name = 'addeps.html'
    success_url = '/vieweps'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Addmedico(PermissionRequiredMixin, FormView):
    permission_required = 'citas.add_medico'
    login_url = 'login'
    form_class = Formumedico
    template_name = 'addmedico.html'
    success_url = '/viewmedico'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Addpaciente(PermissionRequiredMixin, FormView):
    permission_required = 'citas.add_paciente'
    login_url = 'login'
    form_class = Formupaciente
    template_name = 'addpaciente.html'
    success_url = '/viewpaciente'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Addprofile(PermissionRequiredMixin, FormView):
    permission_required = 'citas.add_profile'
    login_url = 'login'
    form_class = Formuuser
    template_name = 'addprofile.html'
    success_url = '/viewprofile'

    def get_context_data(self, **kwargs):
        context = super(Addprofile, self).get_context_data(**kwargs)
        context["form_profile"] = Formuprofile
        return context

    def form_valid(self, form):
        user = form.save()
        user.set_password(user.password)
        user.save()

        profileForm = Formuprofile(self.request.POST)
        if profileForm.is_valid():
            payload = profileForm.save(commit=False)
            payload.user = user
            payload.save()

        return super().form_valid(form)

#Edit

class Editcitamedica(PermissionRequiredMixin, UpdateView):
    permission_required = 'citas.change_citamedica'
    login_url = 'login'
    model = Citamedica
    form_class = Formucitamedica
    template_name = 'editcitamedica.html'
    success_url = '/viewcita'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Editeps(PermissionRequiredMixin, UpdateView):
    permission_required = 'citas.change_eps'
    login_url = 'login'
    model = Eps
    form_class = Formueps
    template_name = 'editeps.html'
    success_url = '/vieweps'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Editmedico(PermissionRequiredMixin, UpdateView):
    permission_required = 'citas.change_medico'
    login_url = 'login'
    model = Medico
    form_class = Formumedico
    template_name = 'editmedico.html'
    success_url = '/viewmedico'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Editpaciente(PermissionRequiredMixin, UpdateView):
    permission_required = 'citas.change_paciente'
    login_url = 'login'
    model = Paciente
    form_class = Formupaciente
    template_name = 'editpaciente.html'
    success_url = '/viewpaciente'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Editprofile(PermissionRequiredMixin, UpdateView):
    permission_required = 'citas.edit_profile'
    login_url = 'login'
    model = Profile
    form_class = Formuprofile
    template_name = 'editprofile.html'
    success_url = '/viewprofile'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Edituser(PermissionRequiredMixin, UpdateView):
    permission_required = 'auth.change_user'
    login_url = 'login'
    model = User
    form_class = Formuuseredit
    template_name = 'edituser.html'
    success_url = '/viewuser'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

#Delete

class Deletcitamedica(PermissionRequiredMixin, DeleteView):
    permission_required = 'citas.del_citamedica'
    login_url = 'login'
    model = Citamedica
    template_name = 'deletecitamedica.html'
    success_url = '/viewcita'


class Deletprofile(PermissionRequiredMixin, DeleteView):
    permission_required = 'citas.del_profile'
    login_url = 'login'
    model = Profile
    template_name = 'deleteprofile.html'
    success_url = '/viewprofile'


class Deletpaciente(PermissionRequiredMixin, DeleteView):
    permission_required = 'citas.del_paciente'
    login_url = 'login'
    model = Paciente
    template_name = 'deletepaciente.html'
    success_url = '/viewpaciente'


class Deleteps(PermissionRequiredMixin, DeleteView):
    permission_required = 'citas.del_eps'
    login_url = 'login'
    model = Eps
    template_name = 'deleteeps.html'
    success_url = '/vieweps'


class Deletmedico(PermissionRequiredMixin, DeleteView):
    permission_required = 'citas.del_medico'
    login_url = 'login'
    model = Medico
    template_name = 'deletemedico.html'
    success_url = '/viewmedico'


class Deletuser(PermissionRequiredMixin, DeleteView):
    permission_required = 'auth.del_user'
    login_url = 'login'
    model = User
    template_name = 'deleteuser.html'
    success_url = '/viewuser'