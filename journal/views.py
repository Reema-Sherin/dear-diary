from django.shortcuts import render, redirect, get_object_or_404
from .models import DiaryEntry
from django.db.models import Q
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    total_entries = DiaryEntry.objects.filter(
        user=request.user
    ).count()

    latest_entry = DiaryEntry.objects.filter(
        user=request.user
    ).order_by('-created_at').first()

    return render(request, 'journal/home.html', {
        'total_entries': total_entries,
        'latest_entry': latest_entry
    })

@login_required
def write_entry(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        mood = request.POST.get('mood', '')

        DiaryEntry.objects.create(
            title=title,
            content=content,
            user=request.user,
            mood=mood
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
            entry.title = title
            entry.content = content
            entry.mood = mood
            entry.save()

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