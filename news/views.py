from django.shortcuts import render
import logging
from .ai import AI  # Corrected import: Use relative import
import json

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

        return render(request, 'index.html', final_result)

    return render(request, 'index.html')

def process_result(result_string):
    """Processes the result string to extract is_real and explanation."""
    try:
        json_string = result_string.replace("```json", "").replace("```", "").strip()
        result_json = json.loads(json_string)
        news_text = result_json.get("news_text")
        is_real = result_json.get("is_real")
        explanation = result_json.get("explanation")

        #add confidence and factors.
        confidence = result_json.get("confidence") #add a default confidence.
        factors = result_json.get("factors", ["None"]) #add default factors.
        return {"news_text": news_text,"result":True, "is_real": is_real, "explanation": explanation, "confidence": confidence, "factors": factors}
        # return {"news_text": news_text,"result":True, "is_real": is_real, "explanation": explanation}

    except (json.JSONDecodeError, AttributeError, TypeError) as e:
        print(f"Error processing result: {e}")
        return {"news_text": "", "is_real": False, "explanation": "Error: Could not process the model's response.", "confidence": 0, "factors": []}