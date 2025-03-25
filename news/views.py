from django.shortcuts import render
import logging
from .ai import AI  # Corrected import: Use relative import
from .utils import process_result
from .tests import evaluate_model


logger = logging.getLogger(__name__)

def index(request):
    path_db = "news/models"
    obj = AI(path_db, query=None)

    if request.method == 'POST':
        obj.load_db()
        news_text = request.POST.get('news_text', '')
        logger.info(f"News text received: {news_text}")
        print(f"News text received: {news_text}")
        obj.query = news_text
        obj.Search_document()
        obj.Promt()
        result = obj.model()
        final_result = process_result(result)
        print("final_result: ", final_result)

        # Ensure these keys are present:
        if "news_text" not in final_result:
            final_result["news_text"] = news_text #add news_text to final result.

        if "confidence" not in final_result:
            final_result["confidence"] = 90 #add a default confidence.

        if "factors" not in final_result:
            final_result["factors"] = ["None"] #add default factors.
            
        test_data = [final_result] #make test_data a list containing a dict.
        evaluate_model(test_data,True)

        return render(request, 'index.html', final_result)

    return render(request, 'index.html')

