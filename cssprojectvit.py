def input_list(list):
 while 1>0:
  n=input("enter syntoms name")
  list.append(n)
  k=int(input("for enter symptoms press 5 or press 1"))
  if k==1:
    break
 return list;

def disease_detector(list):
    n=0
    list1=[]
    count1=0
    count2=0
    count3=0
    count4=0
    count5=0
    count6=0
    count7=0
    count8=0
    count9=0
    count10=0
    count11=0
    count12=0
    count13=0
    count14=0
    count15=0
    count16=0
    count17=0
    count18=0
    count19=0
    count20=0
    count21=0
    count22=0
    count23=0
    count24=0
    count25=0
    count26=0
    count27=0
    count28=0
    count29=0
    count30=0
    
    for i in range(0,len(list)):
        if (list[i]=="Runny nose"):
            count1=count1+1
        if (list[i]=="Sneezing"):
            count1=count1+1
        if(list[i]=="Mild fever"):
            count1=count1+1
        if (list[i]=="High fever"):
            count2=count2+1
        if (list[i]=="Body pain"):
            count2=count2+1
        if (list[i]=="Headache"):
            count2=count2+1
        if (list[i]=="High fever"):
            count3=count3+1
        if (list[i]=="Chills and shivering"):
            count3=count3+1
        if (list[i]=="Sweating"):
            count3=count3+1
        if (list[i]=="High fever"):
            count4=count4+1
        if (list[i]=="Sneezing"):
            count4=count4+1
        if(list[i]=="Mild fever"):
            count4=count4+1
        if (list[i]=="Prolonged fever"):
            count5=count5+1
        if (list[i]=="Weakness"):
            count5=count5+1
        if (list[i]=="Stomach pain"):
            count5=count5+1
        if (list[i]=="Long-lasting cough"):
            count6=count6+1
        if (list[i]=="Chest pain"):
            count6=count6+1
        if (list[i]=="Weight loss"):
            count6=count6+1
        if (list[i]=="High fever"):
            count7=count7+1
        if (list[i]=="Difficulty breathing"):
            count7=count7+1
        if(list[i]=="Chest pain"):
            count7=count7+1
        if (list[i]=="Wheezing"):
            count8=count8+1
        if (list[i]=="Shortness of breath"):
            count8=count8+1
        if (list[i]=="Chest tightness"):
            count8=count8+1
        if (list[i]=="Fever"):
            count9=count9+1
        if (list[i]=="Cough"):
            count9=count9+1
        if (list[i]=="Loss of smell/taste"):
            count9=count9+1
        if (list[i]=="Frequent urination"):
            count10=count10+1
        if (list[i]=="Excessive thist"):
            count10=count10+1
        if(list[i]=="Fatigue"):
            count10=count10+1
        if (list[i]=="Headache"):
            count11=count11+1
        if (list[i]=="Dizziness"):
            count11=count11+1
        if (list[i]=="often no symptoms"):
            count11=count11+1
        if (list[i]=="Chest pain"):
            count12=count12+1
        if (list[i]=="Shortness of breath"):
            count12=count12+1
        if (list[i]=="Pain in left arm"):
            count12=count12+1
        if (list[i]=="Sudden weakness on one side"):
            count13=count13+1
        if (list[i]=="Dificulty speaking"):
            count13=count13+1
        if(list[i]=="Confusion"):
            count13=count13+1
        if (list[i]=="Yellow skin and eyes"):
            count14=count14+1
        if (list[i]=="Dark urin"):
            count14=count14+1
        if (list[i]=="Fatigue"):
            count14=count14+1
        if (list[i]=="Yellow skin"):
            count15=count15+1
        if (list[i]=="Abdominal pain"):
            count15=count15+1
        if (list[i]=="Loss of appetite"):
            count15=count15+1
        if(list[i]=="yellow skin"):
            count15=count15+1
        if(list[i]=="Abdominal pain"):
            count15=count15+1 
        if(list[i]=="Loss of appetite"):
            count15=count15+1

        if(list[i]=="Chickenpox"):
            count16=count16+1
        if(list[i]=="Itchy red blisters"):
            count16=count16+1
        if(list[i]=="Fever"):
            count16=count16+1

        if(list[i]=="measles"):
            count17=count17+1
        if(list[i]=="High fever"):
            count17=count17+1
        if(list[i]=="Red rash"):
            count17=count17+1   


        if(list[i]=="Mumps"):
            count18=count18+1
        if(list[i]=="Swollen salivary glands"):
            count18=count18+1
        if(list[i]=="Jaw pain"):
            count18=count18+1

        if(list[i]=="Migraine"):
            count19=count19+1
        if(list[i]=="Severe headache"):
            count19=count19+1
        if(list[i]=="sensitivity"):
            count19=count19+1

        if(list[i]=="Anemia"):
            count20=count20+1
        if(list[i]=="Fatigue"):
            count20=count20+1
        if(list[i]=="Pale skin "):
            count20=count20+1

        if(list[i]=="Arthritis"):
            count21=count21+1
        if(list[i]=="Joint pain"):
            count21=count21+1
        if(list[i]=="Swelling"):
            count21=count21+1

        if(list[i]=="Kidney Stones"):
            count22=count22+1
        if(list[i]=="Kidney Stones"):
            count22=count22+1
        if(list[i]=="Kidney Stones"):
            count22=count22+1


        if(list[i]=="Gastritis"):
            count23=count23+1
        if(list[i]=="Stomach pain"):
            count23=count23+1
        if(list[i]=="Vomiting"):
            count23=count23+1

        if(list[i]=="Hyperthyroidism"):
            count24=count24+1
        if(list[i]=="Weight loss"):
            count24=count24+1
        if(list[i]=="Fast heartbeat"):
            count24=count24+1

        if(list[i]=="Weight Gain"):
            count25=count25+1
        if(list[i]=="Fatigue"):
            count25=count25+1
        if(list[i]=="Hair loss"):
            count25=count25+1

        if(list[i]=="Cholera"):
            count26=count26+1
        if(list[i]=="Severe watery diarrhea"):
            count26=count26+1
        if(list[i]=="Dehydration"):
            count26=count26+1

        if(list[i]=="Rabies"):
            count27=count27+1
        if(list[i]=="Fever"):
            count27=count27+1
        if(list[i]=="Fear of water"):
            count27=count27+1

        if(list[i]=="Muscle weakness"):
            count28=count28+1
        if(list[i]=="Polio"):
            count28=count28+1
        if(list[i]=="Paralysis"):
            count28=count28+1

        if(list[i]=="Skin Fungal Infection"):
            count29=count29+1
        if(list[i]=="Itching"):
            count29=count29+1
        if(list[i]=="Peeling skin"):
            count29=count29+1


        if(list[i]=="food poisoning"):
            count30=count30+1
        if(list[i]=="Vomiting "):
            count30=count30+1
        if(list[i]=="Fever"):
            count30=count30+1
    list1.append(count1)
    list1.append(count2)
    list1.append(count3)
    list1.append(count4)
    list1.append(count5)
    list1.append(count6)
    list1.append(count7)
    list1.append(count8)
    list1.append(count9)
    list1.append(count10)
    list1.append(count11)
    list1.append(count12)
    list1.append(count13)
    list1.append(count14)
    list1.append(count15)
    list1.append(count16)
    list1.append(count17)
    list1.append(count18)
    list1.append(count19)
    list1.append(count20)
    list1.append(count21)
    list1.append(count22)
    list1.append(count23)
    list1.append(count24)
    list1.append(count25)
    list1.append(count26)
    list1.append(count27)
    list1.append(count28)
    list1.append(count29)
    list1.append(count30)
    list1=sorted(list1)
    m=list1[29]
    if m==count1:
        n+=1
        print("COMMON COLD")
        print("you shold take this medicine"+"--paracetamol,centrizine")
    if m==count2:
        n+=1
        print("INFLUENZA")
        print("you shold take this medicine"+"--paracetamol,antiviral,cough syrup")
    if m==count3:
        n+=1
        print("MALARIA")
        print("you shold take this medicine"+"--astemisinin-based drugs,chloroquine")
    if m==count4:
        n+=1
        print("DENGUE")
        print("you shold take this medicine"+"--paracetamol,ors,iv fluids")
    if m==count5:
        n+=1
        print("TYPHOID")
        print("you shold take this medicine"+"--azithromycin,cefixime")
    if m==count6:
        n+=1
        print("TUBERCULOSIS")
        print("you shold take this medicine"+"--isoniazid,rifampicin,pyrazinamide")
    if m==count7:
        n+=1
        print("PNEUMONIA")
        print("you shold take this medicine"+"--amoxicillin,azithromycin")
    if m==count8:
        n+=1
        print("ASTHMA")
        print("you shold take this medicine"+"--inhalers,steroid inhaler")
    if m==count9:
        n+=1
        print("COVID-19")
        print("you shold take this medicine"+"--paracetamol,cough syrup,antiviral,steam inhalation")
    if m==count10:
        n+=1
        print("DIABETES")
        print("you shold take this medicine"+"--Metformin,insulin ")
    if m==count11:
        n+=1
        print("HYPERTENSION")
        print("you shold take this medicine"+"--Amlodipine,Telmisartan,Atenolol")
    if m==count12:
        n+=1
        print("HEART ATTACK")
        print("you shold take this medicine"+"--Aspirin,nitroglycerin")
    if m==count13:
        n+=1
        print("STROKE")
        print("you shold take this medicine"+"--clot-busting durgs(tpa),aspirin")
    if m==count14:
        n+=1
        print("JAUNDIES")
        print("you shold take this medicine"+"--Depends on cause; usually supportive treatment, IV fluids")
    if m==count15:
        n+=1
        print("HEPATITIS")
        print("you shold take this medicine"+"--Antivirals (Tenofovir, Ribavirin), supportive care")
    if m==count16:
        n+=1
        print("CHICKENPOX")
        print("you shold take this medicine"+"--Paracetamol, Calamine lotion, Antiviral (Acyclovir in some cases)")
    if m==count17:
        n+=1
        print("MEASLES")
        print("you shold take this medicine"+"--Vitamin A, Paracetamol, Fluids")
    if m==count18:
        n+=1
        print("MUMPS")
        print("you shold take this medicine"+"--Paracetamol, Ice packs, Rest (no specific antiviral)")
    if m==count19:
        n+=1
        print("MIGRAINE")
        print("you shold take this medicine"+"--Ibuprofen, Sumatriptan")
    if m==count20:
        n+=1
        print("ANEMIA")
        print("you shold take this medicine"+"--Iron tablets, Folic acid, Vitamin B12")
    if m==count21:
        n+=1
        print("ARTHRITIS")
        print("you shold take this medicine"+"--Ibuprofen, Diclofenac, Steroids (doctor supervised)")
    if m==count22:
        n+=1
        print("KIDNEY STONES")
        print("you shold take this medicine"+"--Pain relievers, Tamsulosin, Increased water intake")
    if m==count23:
        n+=1
        print("GASTRITIS")
        print("you shold take this medicine"+"--Antacids, Pantoprazole, Omeprazole")
    if m==count24:
        n+=1
        print("HYPERTHYROIDISM")
        print("you shold take this medicine"+"--Methimazole, Beta-blockers")
    if m==count25:
        n+=1
        print("HYPOTHYROIDISM")
        print("you shold take this medicine"+"--Levothyroxine")
    if m==count26:
        n+=1
        print("CHOLERA")
        print("you shold take this medicine"+"--ORS, IV fluids, Doxycycline")
    if m==count27:
        n+=1
        print("RABIES")
        print("you shold take this medicine"+"--Rabies vaccine, Rabies immunoglobulin (urgent)")
    if m==count28:
        n+=1
        print("POLIO")
        print("you shold take this medicine"+"--Supportive care (No cure), Polio vaccine")
    if m==count29:
        n+=1
        print("SKIN FUNGAL INFECTION")
        print("you shold take this medicine"+"--Clotrimazole cream, Ketoconazole soap")
    if m==count30:
        n+=1
        print("FOOD POISONING")
        print("you shold take this medicine"+"--ORS, Zinc, Probiotics, Antibiotics only if bacterial (doctor advised)")
    if n>1:
        if m==count1:
         print("Physical examination,No specific test required")
         print(" Take only this medicine if test become positive--COMMON COLD")
        if m==count2:
         print("Rapid Influenza Diagnostic Test (RIDT),PCR test")
         print(" Take only this medicine if test become positive-INFLUENZA")
        if m==count3:
         print("Blood smear test,Rapid Malaria Antigen test")
         print(" Take only this medicine if test become positive-MALARIA")
        if m==count4:
         print("NS1 antigen test,Dengue IgM / IgG antibody test,CBC (platelet count)")
         print(" Take only this medicine if test become positive-DENGUE")
        if m==count5:
         print("Widal test,TyphiDot test,Blood culture")
         print(" Take only this medicine if test become positive-TYPHOID")
        if m==count6:
         print("Mantoux (Tuberculin) skin test,Chest X-ray,Sputum test (GeneXpert)")
         print(" Take only this medicine if test become positive-TUBERCULOSIS")
        if m==count7:
         print("Chest X-ray,Blood test,Sputum culture")
         print(" Take only this medicine if test become positive-PNEUMONIA")
        if m==count8:
         print("Spirometry (lung function test),Peak flow test")
         print(" Take only this medicine if test become positive-ASTHMA")
        if m==count9:
         print("RT-PCR test,Rapid Antigen Test")
         print(" Take only this medicine if test become positive-COVID-19")
        if m==count10:
         print("Fasting blood sugar (FBS),HbA1c test")
         print(" Take only this medicine if test become positive-DIABETES")
        if m==count11:
         print("Blood pressure measurement,ECG (if needed)")
         print(" Take only this medicine if test become positive-HYPERTENSION")
        if m==count12:
         print("ECG,Troponin blood test,Echocardiography")
         print(" Take only this medicine if test become positive-HEART ATTACK")
        if m==count13:
         print("CT scan,MRI scan")
         print(" Take only this medicine if test become positive-STROKE")
        if m==count14:
         print("Liver Function Test (LFT),Bilirubin test,Ultrasound")
         print(" Take only this medicine if test become positive-JAUNDIES")
        if m==count15:
         print("Hepatitis antigen/antibody blood test,LFT")
         print(" Take only this medicine if test become positive-HEPATITIS")
        if m==count16:
         print("Physical examination,VZV antibody test (sometimes)")
         print(" Take only this medicine if test become positive-CHICKENPOX")
        if m==count17:
         print("Measles IgM antibody test,Swab PCR test")
         print(" Take only this medicine if test become positive-MEASLES")
        if m==count18:
         print("Mumps IgM antibody test,Swelling check (physical exam)")
         print(" Take only this medicine if test become positive-MUMPS")
        if m==count19:
         print("Diagnosis based on symptoms,MRI/CT to rule out other causes")
         print(" Take only this medicine if test become positive-MIGRAINE")
        if m==count20:
         print("Complete Blood Count (CBC),Hemoglobin test")
         print(" Take only this medicine if test become positive-ANEMIA")
        if m==count21:
         print("X-ray,RA factor blood test,ESR/CRP")
         print(" Take only this medicine if test become positive-ARTHRITIS")
        if m==count22:
         print("Ultrasound,CT scan,Urine test")
         print(" Take only this medicine if test become positive-KIDNEY STONES")
        if m==count23:
         print("Endoscopy,H. pylori test,Stool antigen test")
         print(" Take only this medicine if test become positive-GASTRITIS")
        if m==count24:
         print("Thyroid hormones (T3, T4, TSH blood test)")
         print(" Take only this medicine if test become positive-HYPERTHYROIDISM")
        if m==count25:
         print("TSH test,T4 test")
         print(" Take only this medicine if test become positive-HYPOTHYROIDISM")
        if m==count26:
         print("Stool culture,Rapid cholera dipstick test")
         print(" Take only this medicine if test become positive-CHOLERA")
        if m==count27:
         print("Rabies antibody test,PCR test (specialized labs)")
         print(" Take only this medicine if test become positive-RABIES")
        if m==count28:
         print("Stool sample test,PCR for poliovirus")
         print(" Take only this medicine if test become positive-POLIO")
        if m==count29:
         print("KOH test (skin scraping),Fungal culture")
         print(" Take only this medicine if test become positive-SKIN FUNGAL INFECTION")
        if m==count30:
         print("Stool test,Blood count,Culture test for bacteria")
         print(" Take only this medicine if test become positive-FOOD POISONING")
       
        
    print("TAKE CARE")
    print(100*"*")
def name_():
    k=input("Name-")
    g=int(input("age-"))
    l=input("enter date")
    print(100*"*")
    print(49*" "+"PRESCRIPTION"+49*" ")
    print("@"+"VIT-BHOPAL"+"@")
    print(80*" "+"Date-"+l)
    print("Patient Name-",k)
    print("Patient Age-",g)
    print("your expected diseases--")
    
diseases_with_symptoms = [
    ''' Runny nose, Sneezing, Sore throat, Mild fever,
     High fever, Body pain, Headache, Cough,
     High fever (comes and goes), Chills, Sweating, Headache,
     High fever, Joint pain, Muscle pain, Skin rash, Low platelets,
     Prolonged fever, Weakness, Stomach pain, Constipation or diarrhea,
     Long cough, Chest pain, Weight loss, Night sweats,
     High fever, Breathing difficulty, Chest pain, Cough with phlegm,
     Wheezing, Shortness of breath, Chest tightness, Cough,
     Fever, Cough, Loss of smell, Breathing difficulty,
     Frequent urination, Excessive thirst, Fatigue, Slow wound healing,
     Headache, Dizziness, Often no symptoms,
     Chest pain, Shortness of breath, Pain in left arm, Sweating,
     Sudden weakness, Speech difficulty, Confusion, Loss of balance,
     Yellow skin, Dark urine, Fatigue, Nausea,
     Yellow skin, Abdominal pain, Appetite loss, Fatigue,
     Itchy blisters, Fever, Body ache,
     High fever, Red rash, Runny nose, Cough,
     Swollen glands, Fever, Jaw pain,
     Severe headache, Light sensitivity, Nausea,
     Fatigue, Pale skin, Weakness, Short breath,
     Joint pain, Swelling, Stiffness,
     Severe back pain, Pain while urinating, Blood in urine,
     Stomach pain, Nausea, Vomiting, Burning sensation,
     Weight loss, Fast heartbeat, Anxiety, Tremors,
     Weight gain, Fatigue, Cold intolerance, Hair loss,
     Watery diarrhea, Vomiting, Dehydration,
     Fever, Fear of water, Salivation, Confusion,
     Muscle weakness, Paralysis, Fever,
     Itching, Red patches, Peeling skin,
     Vomiting, Diarrhea, Fever, Stomach cramps'''
]
print("select your symstoms  ",diseases_with_symptoms)
list=[]
list=input_list(list)
name=name_()
s=diseaces_detector(list)
        
