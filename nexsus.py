# Admission-related responses
admission_responses = {
    "admission procedures": "The admission procedure includes filling out the application form, submitting required documents, and attending an interview.",
    "admission requirements": "The admission requirements typically include a completed application form, high school transcripts, standardized test scores, and letters of recommendation.",
    "application deadlines": "The application deadlines are as follows: Early Decision - November 1, Regular Decision - January 15, and Transfer - March 1.",
    "scholarships": "We offer a variety of scholarships based on merit, need, and specific talents. Please visit our scholarship page for more details.",
    "contact admission office": "You can contact our admission office via email at admissions@college.edu or call us at (123) 456-7890."
}

def get_response(query):
    query = query.lower()
    for key in admission_responses:
        if key in query:
            return admission_responses[key]
    return "I'm not sure how to respond to that. Can you please rephrase or ask another question?"

def chatbot():
    print("Welcome to the College Admission Chatbot!")
    print("How can I assist you with your admission queries today?")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! If you have any more questions, feel free to ask anytime.")
            break
        
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()