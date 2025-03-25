from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from .ai import AI
from .utils import process_result

def evaluate_model(test_data,is_process):  # test_data is a list of dictionaries.
    if is_process:
        path_db = "news/models"
        obj = AI(path_db, query=None)
        obj.load_db()
        actual_labels = []
        predicted_labels = []

        for item in test_data:  # Corrected: use 'item' instead of 'i'
            print(f"Text_data: {item}")  # Corrected: use 'item' instead of 'i'
            news_text = item["news_text"]
            actual_label = item["is_real"]

        # Run your model's prediction logic here
            obj.query = news_text
            obj.Search_document()
            obj.Promt()
            result = obj.model()
            final_result = process_result(result)
            predicted_label = final_result["is_real"]

            actual_labels.append(actual_label)
            predicted_labels.append(predicted_label)

        accuracy = accuracy_score(actual_labels, predicted_labels)
        precision = precision_score(actual_labels, predicted_labels)
        recall = recall_score(actual_labels, predicted_labels)
        f1 = f1_score(actual_labels, predicted_labels)

        print(f"Accuracy: {accuracy}")
        print(f"Precision: {precision}")
        print(f"Recall: {recall}")
        print(f"F1-Score: {f1}")