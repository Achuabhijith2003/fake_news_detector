import json

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
        factors = result_json.get("factors") #add default factors.
        return {"news_text": news_text,"result":True, "is_real": is_real, "explanation": explanation, "confidence": confidence, "factors": factors}
        # return {"news_text": news_text,"result":True, "is_real": is_real, "explanation": explanation}

    except (json.JSONDecodeError, AttributeError, TypeError) as e:
        print(f"Error processing result: {e}")
        return {"news_text": "", "is_real": False, "explanation": "Error: Could not process the model's response.", "confidence": 0, "factors": []}