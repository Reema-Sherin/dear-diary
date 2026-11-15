from django.shortcuts import render, redirect, get_object_or_404
from .models import DiaryEntry
from django.db.models import Q

def home(request):
     return render(request, 'journal/home.html')

def write_entry(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        mood = request.POST.get('mood', '')

        DiaryEntry.objects.create(
            title=title,
            content=content,
            mood=mood
        )

        return redirect('entries')

    return render(request, 'journal/write.html')

def diary_entries(request):
    query = request.GET.get('q', '').strip()
    entries = DiaryEntry.objects.all().order_by('-created_at')

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

def entry_detail(request, entry_id):
    entry = get_object_or_404(DiaryEntry, id=entry_id)

    return render(request, 'journal/entry_detail.html', {
        'entry': entry
    })


def edit_entry(request, entry_id):
    entry = get_object_or_404(DiaryEntry, id=entry_id)

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

def delete_entry(request, entry_id):
    entry = get_object_or_404(DiaryEntry, id=entry_id)

    if request.method == 'POST':
        entry.delete()
        return redirect('entries')

    return render(request, 'journal/confirm_delete.html', {
        'entry': entry
    })