from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from .models import Achievement, DiaryEntry
from django.db.models import Q
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from collections import Counter
from .forms import AchievementForm
from django.shortcuts import get_object_or_404

@login_required
def home(request):
    total_entries = DiaryEntry.objects.filter(
        user=request.user
    ).count()

    latest_entry = DiaryEntry.objects.filter(
        user=request.user
    ).order_by('-created_at').first()

    recent_entries = DiaryEntry.objects.filter(
        user=request.user
    ).order_by('-created_at')[:7]

    mood_counts = Counter(
        entry.mood
        for entry in recent_entries
        if entry.mood
    )

    mood_labels = dict(DiaryEntry.MOOD_CHOICES)

    mood_data = [
        {
            'mood': mood_labels[mood],
            'count': count
        }
        for mood, count in mood_counts.items()
    ]

    return render(request, 'journal/home.html', {
        'total_entries': total_entries,
        'latest_entry': latest_entry,
        'mood_data': mood_data
    })


@login_required
def write_entry(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        mood = request.POST.get('mood', '')

        # Receive uploaded photograph
        image = request.FILES.get('image')

        DiaryEntry.objects.create(
            title=title,
            content=content,
            user=request.user,
            mood=mood,
            image=image
        )

        return redirect('entries')

    return render(request, 'journal/write.html')


@login_required
def diary_entries(request):
    query = request.GET.get('q', '').strip()
    entries = DiaryEntry.objects.filter(user=request.user).order_by('-created_at')
    if query:
        entries = entries.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    context = {
        'entries': entries,
        'query': query
    }

    return render(
        request,
        'journal/entries.html',
        context
    )

@login_required
def entry_detail(request, entry_id):
    entry = get_object_or_404(
    DiaryEntry,
    id=entry_id,
    user=request.user
)

    return render(request, 'journal/entry_detail.html', {
        'entry': entry
    })

@login_required
def edit_entry(request, entry_id):
    entry = get_object_or_404(
        DiaryEntry,
        id=entry_id,
        user=request.user
    )

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        mood = request.POST.get('mood', '')

        if title and content:

            # Keep a reference to the previous photograph
            old_image = entry.image

            # Check for a newly uploaded photograph
            new_image = request.FILES.get('image')

            # Check whether the user wants to remove the photograph
            remove_image = request.POST.get('remove_image') == 'on'

            entry.title = title
            entry.content = content
            entry.mood = mood

            if new_image:
                entry.image = new_image

            elif remove_image:
                entry.image = None

            entry.save()

            # Delete the previous physical file if replaced or removed
            if old_image and (new_image or remove_image):
                old_image.delete(save=False)

            return redirect('entry_detail', entry_id=entry.id)

        error = "Title and content cannot be empty."

        return render(request, 'journal/edit_entry.html', {
            'entry': entry,
            'error': error
        })

    return render(request, 'journal/edit_entry.html', {
        'entry': entry
    })


@login_required
def delete_entry(request, entry_id):
    entry = get_object_or_404(
        DiaryEntry,
        id=entry_id,
        user=request.user
    )

    if request.method == 'POST':
        entry.delete()
        return redirect('entries')

    return render(request, 'journal/confirm_delete.html', {
        'entry': entry
    })

def signup(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('home')

    else:

        form = UserCreationForm()

    return render(
        request,
        'registration/signup.html',
        {'form': form}
    )

@login_required
def achievement_list(request):
    achievements = Achievement.objects.filter(
        user=request.user
    ).order_by('-achieved_on')

    return render(
        request,
        'journal/achievements.html',
        {'achievements': achievements}
    )

@login_required
def achievement_create(request):
    if request.method == 'POST':
        form = AchievementForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            achievement = form.save(commit=False)
            achievement.user = request.user
            achievement.save()

            return redirect('achievement_list')

    else:
        form = AchievementForm()

    return render(
        request,
        'journal/achievement_form.html',
        {'form': form}
    )

@login_required
def achievement_delete(request, pk):

    achievement = get_object_or_404(
        Achievement,
        pk=pk,
        user=request.user
    )

    if request.method == 'POST':
        achievement.delete()
        return redirect('achievement_list')

    return render(
        request,
        'journal/achievement_delete.html',
        {'achievement': achievement}
    )