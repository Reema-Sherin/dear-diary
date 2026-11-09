from django.shortcuts import render, redirect, get_object_or_404
from .models import DiaryEntry

def home(request):
    return render(request, 'journal/home.html')

def write_entry(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        DiaryEntry.objects.create(
            title=title,
            content=content
        )

        return redirect('entries')

    return render(request, 'journal/write.html')

def diary_entries(request):
    entries = DiaryEntry.objects.all().order_by('-created_at')

    return render(
        request,
        'journal/entries.html',
        {'entries': entries}
    )

def entry_detail(request, entry_id):
    entry = get_object_or_404(DiaryEntry, id=entry_id)

    return render(request, 'journal/entry_detail.html', {
        'entry': entry
    })