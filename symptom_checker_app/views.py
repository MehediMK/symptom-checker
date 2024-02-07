from django.shortcuts import render
from .models import Symptom, Disease, Doctor, Patient
from .forms import SymptomCheckForm


def symptom_checker(request):
    if request.method == 'GET':
        # If it's a GET request, create a new form with symptom choices
        form = SymptomCheckForm()

        # Render the symptom checker template with the form
        return render(request, 'symptom_checker.html', {'form': form})

    form = SymptomCheckForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        gender = form.cleaned_data['gender']
        age = form.cleaned_data['age']
        selected_symptoms = form.cleaned_data['symptoms']

        # Create a new patient object
        patient = Patient.objects.create(name=name, gender=gender, age=age)

        # Get the symptom objects based on the selected symptom IDs
        selected_symptoms = Symptom.objects.filter(id__in=selected_symptoms)

        # Find diseases matching the selected symptoms
        matching_diseases = Disease.objects.filter(symptoms__in=selected_symptoms).distinct()

        # Initialize an empty list to store suggested doctors
        suggested_doctors = []

        # For each matching disease, find doctors specializing in that disease
        for disease in matching_diseases:
            doctors_for_disease = Doctor.objects.filter(specialties=disease)
            suggested_doctors.extend(doctors_for_disease)

        # Remove duplicate doctors (if any)
        suggested_doctors = list(set(suggested_doctors))

        return render(request, 'result.html', {'patient': patient, 'diseases': matching_diseases, 'doctors': suggested_doctors})
    