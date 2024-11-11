import tkinter as tk
from tkinter import messagebox
import pickle
import numpy as np
import os
import sys

# Load the pretrained model with an executable-compatible path
if getattr(sys, 'frozen', False):  # Check if running as a PyInstaller bundle
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

model_path = os.path.join(base_path, 'svc.pkl')
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Define all 132 symptoms in the order they were used during training
symptom_list = [
    "itching", "skin_rash", "nodal_skin_eruptions", "continuous_sneezing", "shivering",
    "chills", "joint_pain", "stomach_pain", "acidity", "ulcers_on_tongue",
    "muscle_wasting", "vomiting", "burning_micturition", "spotting_urination", "fatigue",
    "weight_gain", "anxiety", "cold_hands_and_feets", "mood_swings", "weight_loss",
    "restlessness", "lethargy", "patches_in_throat", "irregular_sugar_level", "cough",
    "high_fever", "sunken_eyes", "breathlessness", "sweating", "dehydration",
    "indigestion", "headache", "yellowish_skin", "dark_urine", "nausea",
    "loss_of_appetite", "pain_behind_the_eyes", "back_pain", "constipation", "abdominal_pain",
    "diarrhoea", "mild_fever", "yellow_urine", "yellowing_of_eyes", "acute_liver_failure",
    "fluid_overload", "swelling_of_stomach", "swelled_lymph_nodes", "malaise", "blurred_and_distorted_vision",
    "phlegm", "throat_irritation", "redness_of_eyes", "sinus_pressure", "runny_nose",
    "congestion", "chest_pain", "weakness_in_limbs", "fast_heart_rate", "pain_during_bowel_movements",
    "pain_in_anal_region", "bloody_stool", "irritation_in_anus", "neck_pain", "dizziness",
    "cramps", "bruising", "obesity", "swollen_legs", "swollen_blood_vessels",
    "puffy_face_and_eyes", "enlarged_thyroid", "brittle_nails", "swollen_extremeties", "excessive_hunger",
    "extra_marital_contacts", "drying_and_tingling_lips", "slurred_speech", "knee_pain", "hip_joint_pain",
    "muscle_weakness", "stiff_neck", "swelling_joints", "movement_stiffness", "spinning_movements",
    "loss_of_balance", "unsteadiness", "weakness_of_one_body_side", "loss_of_smell", "bladder_discomfort",
    "foul_smell_of_urine", "continuous_feel_of_urine", "passage_of_gases", "internal_itching", "toxic_look_(typhos)",
    "depression", "irritability", "muscle_pain", "altered_sensorium", "red_spots_over_body",
    "belly_pain", "abnormal_menstruation", "dischromic_patches", "watering_from_eyes", "increased_appetite",
    "polyuria", "family_history", "mucoid_sputum", "rusty_sputum", "lack_of_concentration",
    "visual_disturbances", "receiving_blood_transfusion", "receiving_unsterile_injections", "coma", "stomach_bleeding",
    "distention_of_abdomen", "history_of_alcohol_consumption", "fluid_overload", "blood_in_sputum", "prominent_veins_on_calf",
    "palpitations", "painful_walking", "pus_filled_pimples", "blackheads", "scurring",
    "skin_peeling", "silver_like_dusting", "small_dents_in_nails", "inflammatory_nails", "blister",
    "red_sore_around_nose", "yellow_crust_ooze"
]

# Dictionary to map index to disease name
disease_dict = {
    15: 'Fungal infection', 4: 'Allergy', 16: 'GERD', 9: 'Chronic cholestasis', 
    14: 'Drug Reaction', 33: 'Peptic ulcer disease', 1: 'AIDS', 12: 'Diabetes', 
    17: 'Gastroenteritis', 6: 'Bronchial Asthma', 23: 'Hypertension', 30: 'Migraine', 
    7: 'Cervical spondylosis', 32: 'Paralysis (brain hemorrhage)', 28: 'Jaundice', 
    29: 'Malaria', 8: 'Chicken pox', 11: 'Dengue', 37: 'Typhoid', 40: 'hepatitis A', 
    19: 'Hepatitis B', 20: 'Hepatitis C', 21: 'Hepatitis D', 22: 'Hepatitis E', 
    3: 'Alcoholic hepatitis', 36: 'Tuberculosis', 10: 'Common Cold', 34: 'Pneumonia', 
    13: 'Dimorphic hemorrhoids(piles)', 18: 'Heart attack', 39: 'Varicose veins', 
    26: 'Hypothyroidism', 24: 'Hyperthyroidism', 25: 'Hypoglycemia', 31: 'Osteoarthritis', 
    5: 'Arthritis', 0: '(vertigo) Paroxysmal Positional Vertigo', 2: 'Acne', 
    38: 'Urinary tract infection', 35: 'Psoriasis', 27: 'Impetigo'
}

class HealthApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Disease Recommendation System")
        
        # Set background color
        self.root.config(bg="#f5f5f5")
        
        # Label for instructions
        self.symptom_label = tk.Label(root, text="Enter Symptoms (comma-separated):", 
                                      font=("Arial", 14, "bold"), bg="#f5f5f5", fg="#333")
        self.symptom_label.pack(pady=10)
        
        # Smaller input box
        self.symptom_entry = tk.Entry(root, width=50, font=("Arial", 12), 
                                      bd=2, relief="solid", fg="#555", bg="#fff")
        self.symptom_entry.pack(pady=10)
        
        # Button to get recommendations with icon
        self.recommend_button = tk.Button(root, text="Get Recommendations", 
                                          font=("Arial", 12, "bold"), command=self.get_recommendations, 
                                          relief="raised", bg="#4CAF50", fg="#fff", height=2, width=20)
        self.recommend_button.pack(pady=15)
        
        # Smaller output box that adjusts to content
        self.output_text = tk.Text(root, height=3, width=50, font=("Arial", 12), 
                                   bg="#f5f5f5", fg="#333", wrap="word", bd=2)
        self.output_text.pack(pady=10)
    
    def get_recommendations(self):
        # Get symptoms from entry and convert to list
        symptom_input = self.symptom_entry.get().lower()
        
        if not symptom_input:
            messagebox.showerror("Input Error", "Please enter some symptoms!")
            return
        
        input_symptoms = [symptom.strip() for symptom in symptom_input.split(',')]
        
        # Convert text symptoms to binary vector
        symptoms = [1 if symptom in input_symptoms else 0 for symptom in symptom_list]
        
        # Ensure the vector has exactly 132 elements
        if len(symptoms) < 132:
            symptoms += [0] * (132 - len(symptoms))
        
        # Convert to a numpy array and reshape for model input
        symptoms = np.array(symptoms).reshape(1, -1)
        
        # Predict using the model
        prediction = model.predict(symptoms)[0]  # Get the first element if prediction is an array
        
        # Get the disease name from the dictionary
        disease_name = disease_dict.get(prediction, "Unknown Disease")
        
        # Display the result
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, f"Predicted Disease: {disease_name}")
        
# Create the main window and application instance
root = tk.Tk()
app = HealthApp(root)

# Run the Tkinter event loop
root.mainloop()
