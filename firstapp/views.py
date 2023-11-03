from django.shortcuts import render
from firstapp.forms import ProfileForm
from firstapp.models import Profile
from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request,'firstapp/index.html')

def profile(request):
    form=ProfileForm()
    registration=False
    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            registration=True
            return HttpResponseRedirect(reverse('firstapp:home'))
    dict={'form':form,'registration':registration}
    return render(request,'firstapp/profile.html',context=dict)


class IndexView(ListView):
    context_object_name='student_list'
    model=Profile
    template_name='firstapp/index.html'

class StudentDetail(DetailView):
    context_object_name='students'
    model=Profile
    template_name='firstapp/student_details.html'
