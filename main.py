import requests

# URL of the APIs (make sure to adjust the ports if needed)
CLASSIFY_API_URL = "http://127.0.0.1:8000/classify-text/"
SUMMARIZE_API_URL = "http://127.0.0.1:8001/summarize/"

# Function to classify the text into categories using the classification API
def classify_text(List_text):
    response = requests.post(CLASSIFY_API_URL, json={"text": List_text})
    if response.status_code == 200:
        return response.json()  # Return the categorized clauses
    else:
        print("Error classifying text:", response.status_code)
        return None

# Function to summarize text using the summarization API
def summarize_text(text):
    response = requests.post(SUMMARIZE_API_URL, json={"text": text})
    if response.status_code == 200:
        return response.json().get("summary", "")  # Return the summary
    else:
        print("Error summarizing text:", response.status_code)
        return None

# Main function to classify and summarize the text
def classify_and_summarize(List_text):
    # Step 1: Classify the text into categories
    classified_data = classify_text(List_text)
    if not classified_data:
        print("No classified data found.")
        return

    # Step 2: Summarize each category of classified text
    summaries = {}
    for category, clauses in classified_data.items():
        category_summary = []
        for clause in clauses:
            summary = summarize_text(clause)
            if summary:
                category_summary.append(summary)
        summaries[category] = category_summary

    return summaries