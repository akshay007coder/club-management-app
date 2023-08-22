# clubs/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in
            return redirect('clubs:home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
# clubs/views.py
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    pass
    # Your view logic here
# clubs/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Club, MembershipRequest, Task, Announcement
from .forms import MembershipRequestForm, TaskForm, AnnouncementForm

@login_required
def join_club(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    if request.method == 'POST':
        # Process the form submission
        request = MembershipRequest.objects.create(club=club, student=request.user)
        return redirect('clubs:club_detail', club_id=club_id)
    return render(request, 'clubs/club_detail.html', {'club': club})

@login_required
def add_task(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.club = club
            task.save()
            return redirect('clubs:club_detail', club_id=club_id)
    else:
        form = TaskForm()
    return render(request, 'clubs/add_task.html', {'club': club, 'form': form})
# clubs/views.py
from django.contrib.auth.decorators import login_required, user_passes_test

def is_faculty(user):
    return user.groups.filter(name='Faculty').exists()

@login_required
def faculty_only_view(request):
    pass
    # This view can only be accessed by faculty members
    # Use the @user_passes_test decorator to restrict access
    # For example: @user_passes_test(is_faculty)
# clubs/views.py
from rest_framework import generics
from .models import Club, MembershipRequest, Task, Announcement
from .serializers import ClubSerializer, MembershipRequestSerializer, TaskSerializer, AnnouncementSerializer

class ClubList(generics.ListCreateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class ClubDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class MembershipRequestList(generics.ListCreateAPIView):
    queryset = MembershipRequest.objects.all()
    serializer_class = MembershipRequestSerializer

# Create similar views for Task and Announcement models
