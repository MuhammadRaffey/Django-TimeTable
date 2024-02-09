from .forms import TimetableForm
from django.shortcuts import render,redirect,get_object_or_404
from .models import Lecture
from datetime import datetime
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from django import forms


def daily_timetable(request):
    # Get today's day (e.g., Monday)
    today = datetime.today().strftime('%A')
    
    # Get lectures for today
    lectures_today = Lecture.objects.filter(day=today).order_by('start_time')

    context = {'lectures_today': lectures_today}
    return render(request, 'app/daily_timetable.html', context)

def lecture_detail(request, pk):
    lecture = get_object_or_404(Lecture, pk=pk)
    return render(request, 'app/lecture_detail.html', {'lecture': lecture})
def create_timetable(request):
    if request.method == 'POST':
        form = TimetableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daily_timetable')  # Redirect to daily timetable page or any other page
    else:
        form = TimetableForm()
    return render(request, 'app/create_timetable.html', {'form': form})

class LectureUpdateView(UpdateView):
    model = Lecture
    fields = ['course', 'professor', 'classroom', 'day', 'name', 'start_time', 'end_time']
    template_name = 'app/lecture_update.html'  # Create a template named 'lecture_update.html' for rendering the update form

    def get_success_url(self):
        return reverse_lazy('lecture_detail', kwargs={'pk': self.object.pk})

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['start_time'].widget = forms.TimeInput(attrs={'type': 'time'})
        form.fields['end_time'].widget = forms.TimeInput(attrs={'type': 'time'})
        return form
class LectureDeleteView(DeleteView):
    model = Lecture
    success_url = reverse_lazy('daily_timetable')  # Redirect to 'lecture_list' URL after successful deletion
    template_name = 'app/lecture_confirm_delete.html'  # Create a template named 'lecture_confirm_delete.html' for rendering the delete confirmation page