from django.shortcuts import render
import logging
from .ai import AI  # Corrected import: Use relative import

logger = logging.getLogger(__name__)

def index(request):
    path_db = "news/models" #define the path_db here, so it is accessible within the function.
    obj = AI(path_db, query=None) #define the AI object here.
    if request.method == 'POST':
        obj.load_db() #load the db before querying.
        news_text = request.POST.get('news_text', '')
        logger.info(f"News text received: {news_text}")
        print(f"News text received: {news_text}")
        obj.query = news_text
        obj.Search_document()
        obj.Promt()
        obj.model()

        return render(request, 'index.html', {'news_text': news_text})

    return render(request, 'index.html')