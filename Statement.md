 ##📌 Problem Statement
Identifying diseases based on symptoms is often confusing for people without medical knowledge.  
Most individuals experience common symptoms such as fever, body pain, cough, nausea, or rashes, but they are unable to understand which disease these symptoms might indicate.  
Visiting a doctor for every small symptom is not always practical, especially for students or people living in remote areas.

There is a need for a simple *console-based tool* that allows users to:
- Enter their symptoms manually,
- Match them with common diseases,
- Get an estimate of the possible disease,
- View suggested medical tests,
- And receive a basic prescription-style output.

This helps in *early awareness* and *self-assessment*, while still recommending that only certified medical professionals provide real diagnosis.

---

## 📌 Scope of the Project
The project focuses on building a *Python-based, symptom-driven disease detection system* that includes:
- A list of 30 common diseases
- Their key symptoms
- Recommended tests
- Suggested medicines (only after tests confirm disease)
- A console-based prescription output

The project covers:
- User input handling (name, age, date, symptoms)
- Matching symptoms with disease profiles using counting logic
- Identifying the most probable disease based on symptom frequency
- Displaying a structured, readable prescription format
- Organizing code into functions for clarity  
- Fulfilling academic requirements for the VIT Yarthi flipped-course project.

*Not* included in scope:
- Real-time medical data
- Machine learning prediction
- Graphical user interface (GUI)
- Professional medical diagnosis

---

## 👥 Target Users
The system is intended for:
- *Students* learning Python and basic project development
- *Beginners* who want to understand symptom-based classification
- *Individuals* wanting a simple awareness tool
- *People in remote areas* who cannot immediately access medical consultation
- *Academic evaluators* reviewing the project as part of the course requirement

Important: This tool is *not* for real medical decisions and is meant only for educational purposes.

---

## ⭐ High-Level Features
1. *Symptom Input System*
   - User can enter multiple symptoms.
   - Program loops until the user chooses to stop.

2. *Disease Matching Logic*
   - Uses symptom-counting to compare with 30 predefined diseases.
   - Identifies the most probable disease based on maximum match.

3. *Medicine Recommendation*
   - Displays commonly used medicines for each disease.
   - Only advises taking medicine after confirming through tests.

4. *Test Suggestions*
   - Shows appropriate diagnostic tests for accurate confirmation.

5. *Prescription Generation*
   - Creates a formatted console-based prescription:
     - Patient name, age
     - Date
     - Expected disease
     - Tests and medicine suggestions
     - “TAKE CARE” message

6. *Simple and User-Friendly Console Interface*
   - No external libraries required.
   - Runs on any Python 3.x environment.
