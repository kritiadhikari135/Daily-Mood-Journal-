from django.shortcuts import render, redirect, get_object_or_404
from .models import MoodEntry
from .forms import MoodEntryForm

def mood_list(request):
    query = request.GET.get('q', '')
    moods = MoodEntry.objects.order_by('-date', '-created_at')
    if query:
        moods = moods.filter(notes__icontains=query) | moods.filter(mood__icontains=query)
    return render(request, 'journal/mood_list.html', {'moods': moods, 'query': query})

def mood_create(request):
    if request.method == 'POST':
        form = MoodEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mood_list')
    else:
        form = MoodEntryForm()
    return render(request, 'journal/mood_form.html', {'form': form})

def mood_edit(request, pk):
    mood = get_object_or_404(MoodEntry, pk=pk)
    if request.method == 'POST':
        form = MoodEntryForm(request.POST, instance=mood)
        if form.is_valid():
            form.save()
            return redirect('mood_list')
    else:
        form = MoodEntryForm(instance=mood)
    return render(request, 'journal/mood_form.html', {'form': form})

def mood_delete(request, pk):
    mood = get_object_or_404(MoodEntry, pk=pk)
    if request.method == 'POST':
        mood.delete()
        return redirect('mood_list')
    return render(request, 'journal/mood_confirm_delete.html', {'mood': mood})

def mood_detail(request, pk):
    mood = get_object_or_404(MoodEntry, pk=pk)
    return render(request, 'journal/mood_detail.html', {'mood': mood})
