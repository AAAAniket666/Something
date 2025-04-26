# Dictionaries of disease symptoms and treatments
disease_symptoms = {
    "Flu": ["fever", "cough", "sore throat", "body aches"],
    "Cold": ["sneezing", "runny nose", "cough", "mild headache"],
    "Malaria": ["fever", "chills", "headache", "sweating"],
    "COVID-19": ["fever", "cough", "loss of taste", "shortness of breath"],
    "Allergies": ["sneezing", "itchy eyes", "runny nose", "cough"],
    "Pneumonia": ["fever", "cough", "chest pain", "shortness of breath"],
    "Dengue": ["fever", "headache", "muscle pain", "rash", "joint pain"],
    "Strep throat": ["sore throat", "fever", "swollen lymph nodes", "headache"],
    "Asthma": ["shortness of breath", "wheezing", "chest tightness", "cough"]
}

disease_treatments = {
    "Flu": "Rest and drink fluids.",
    "Cold": "Stay warm and use cold medicine.",
    "Malaria": "Visit a doctor and take antimalarial medicine.",
    "COVID-19": "Isolate and consult a doctor.",
    "Allergies": "Take antihistamines and avoid allergens.",
    "Pneumonia": "Consult a doctor and take prescribed antibiotics.",
    "Dengue": "Stay hydrated, rest, and consult a doctor.",
    "Strep throat": "Visit a doctor and take antibiotics if confirmed.",
    "Asthma": "Use inhalers and avoid triggers. Consult a doctor if severe."
}


def get_user_symptoms():
    """
    Continue prompting the user until at least four non-empty symptoms are provided.
    """
    while True:
        user_input = input("Enter symptoms separated by commas: ").strip().lower()
        if not user_input:
            print("You have entered an empty input. Please enter at least 4 symptoms.")
            continue

        symptom_list = [s.strip() for s in user_input.split(",") if s.strip()]
        if len(symptom_list) < 4:
            print("You must enter at least 4 symptoms. Please try again.")
            continue

        return symptom_list


def compute_initial_scores(user_symptoms):
    """
    For each disease, count how many of the user's symptoms occur.
    """
    scores = {}
    for disease, symptoms in disease_symptoms.items():
        score = sum(1 for s in user_symptoms if s in symptoms)
        scores[disease] = score
    return scores


def ask_counter_questions(scores, ambiguous_diseases):
    """
    For diseases with the same maximum initial score, ask a follow-up question about a differentiating symptom.
    For each ambiguous disease, the function finds a symptom unique to that disease (i.e., not common across all ambiguous ones)
    and asks the user if they have that symptom. A "yes" adds a point to that disease's score.
    """
    # Determine the set of symptoms that are common to all ambiguous diseases.
    common_symptoms = set.intersection(*(set(disease_symptoms[d]) for d in ambiguous_diseases))
    
    # Ask for a differentiating symptom for each ambiguous disease (if available).
    for disease in ambiguous_diseases:
        # Unique symptoms for this disease among the ambiguous group
        unique_symptoms = set(disease_symptoms[disease]) - common_symptoms
        if unique_symptoms:
            # Ask about one unique symptom (if there are several, asking one is sufficient)
            symptom = unique_symptoms.pop()
            answer = input(f"For {disease}, do you also have {symptom}? (yes/no): ").strip().lower()
            if answer == "yes":
                scores[disease] += 1
    return scores


def calculate_probabilities(scores, diseases):
    """
    Calculate a probability for each disease by comparing the (updated) score to the total number of symptoms
    expected for that disease.
    """
    probabilities = {}
    for disease in diseases:
        total_possible = len(disease_symptoms[disease])
        # Prevent division by zero (should not happen given our dictionary)
        probabilities[disease] = (scores[disease] / total_possible) if total_possible else 0
    return probabilities


def main():
    user_symptoms = get_user_symptoms()

    # Compute initial matching scores.
    scores = compute_initial_scores(user_symptoms)
    
    # Check if at least one disease has a score greater than 0.
    if all(score == 0 for score in scores.values()):
        print("No matching disease found based on your symptoms.")
        return
    
    # Identify the disease(s) that scored the highest.
    max_score = max(scores.values())
    ambiguous_diseases = [d for d, score in scores.items() if score == max_score]

    # If multiple diseases are tied, ask differentiating (counter) questions.
    if len(ambiguous_diseases) > 1:
        print("\nMultiple possible diseases found. Asking a few more questions to help narrow it down...\n")
        scores = ask_counter_questions(scores, ambiguous_diseases)
        # Re-compute the ambiguous diseases after updating scores.
        max_score = max(scores.values())
        ambiguous_diseases = [d for d, score in scores.items() if score == max_score]

    # Calculate probability (score relative to the total symptom list for that disease).
    probabilities = calculate_probabilities(scores, ambiguous_diseases)
    
    # Display results
    print("\nPossible diseases and recommended treatments:")
    for disease in ambiguous_diseases:
        probability = probabilities[disease] * 100  # as percentage
        print(f"\n{disease}:")
        print(f"   - Match Probability: {probability:.1f}%")
        print(f"   - Treatment: {disease_treatments[disease]}")

        
if __name__ == "__main__":
    main()