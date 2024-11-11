// script.js

// Sorted list of symptoms
const symptoms = [
    'abdominal_pain', 'abnormal_menstruation', 'acute_liver_failure', 'anxiety', 'back_pain',
    'blackheads', 'blister', 'blood_in_sputum', 'bruising', 'burning_micturition', 'brittle_nails',
    'chest_pain', 'chills', 'cough', 'congestion', 'continuous_feel_of_urine', 'continuous_sneezing',
    'coma', 'constipation', 'cramps', 'dark_urine', 'dehydration', 'depression', 'diarrhoea',
    'dizziness', 'drying_and_tingling_lips', 'fluid_overload', 'fluid_overload.1', 'foul_smell_of_urine',
    'family_history', 'fast_heart_rate', 'fatigue', 'headache', 'high_fever', 'history_of_alcohol_consumption',
    'hip_joint_pain', 'hyperglycemia', 'irregular_sugar_level', 'irritability', 'irritation_in_anus',
    'lack_of_concentration', 'lethargy', 'malaise', 'mild_fever', 'mood_swings', 'movement_stiffness',
    'muscle_pain', 'muscle_weakness', 'muscle_wasting', 'nausea', 'nodal_skin_eruptions', 'neck_pain',
    'obesity', 'pain_during_bowel_movements', 'pain_in_anal_region', 'pain_behind_the_eyes', 'palpitations',
    'patches_in_throat', 'pus_filled_pimples', 'red_sore_around_nose', 'red_spots_over_body',
    'redness_of_eyes', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'restlessness',
    'rusty_sputum', 'scurring', 'skin_peeling', 'skin_rash', 'slurred_speech', 'small_dents_in_nails',
    'sinus_pressure', 'shivering', 'silver_like_dusting', 'stiff_neck', 'stomach_bleeding',
    'stomach_pain', 'swelling_of_stomach', 'swelled_lymph_nodes', 'swollen_blood_vessels',
    'swollen_extremeties', 'swollen_legs', 'toxic_look_(typhos)', 'ulcers_on_tongue', 'unsteadiness',
    'vomiting', 'water_retentio', 'watering_from_eyes', 'weight_gain', 'weight_loss',
    'weakness_in_limbs', 'weakness_of_one_body_side', 'yellow_crust_ooze', 'yellow_urine',
    'yellowing_of_eyes', 'yellowish_skin'
];

// Function to create checkboxes
const createCheckboxes = () => {
    const container = document.getElementById('checkboxContainer');
    symptoms.forEach(symptom => {
        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.name = 'symptoms';
        checkbox.value = symptom;
        checkbox.id = symptom;

        const label = document.createElement('label');
        label.htmlFor = symptom;
        label.appendChild(document.createTextNode(symptom.replace(/_/g, ' ')));

        const div = document.createElement('div');
        div.appendChild(checkbox);
        div.appendChild(label);
        container.appendChild(div);
    });
};

// Call function to create checkboxes
createCheckboxes();
