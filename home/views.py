from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json

from .models import Text, TypingResult


def home(request):
    texts = Text.objects.all().order_by('-created_at')
    return render(request, 'home/index.html', {'texts': texts})


def typing_view(request, pk):
    text = get_object_or_404(Text, pk=pk)
    return render(request, 'home/typing.html', {'text': text})


@require_POST
def save_result(request, pk):
    text = get_object_or_404(Text, pk=pk)
    data = json.loads(request.body)
    result = TypingResult.objects.create(
        text=text,
        wpm=data['wpm'],
        accuracy=data['accuracy'],
        time_taken=data['time_taken'],
    )
    return JsonResponse({
        'id': result.id,
        'wpm': result.wpm,
        'accuracy': result.accuracy,
        'time_taken': result.time_taken,
    })


def leaderboard(request):
    results = TypingResult.objects.select_related('text').order_by('-wpm')[:20]
    return render(request, 'home/leaderboard.html', {'results': results})
