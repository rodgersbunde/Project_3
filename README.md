[![Version](https://img.shields.io/badge/Version-1.0-green.svg)](https://github.com/username/repo/releases/tag/v1.0)



![2024v1](https://github.com/Beatrice-Kariuki/Sharing-Project-Phase-3/assets/144832651/fe0a1157-c1b4-491d-9d91-773098dee14e)


# Patient Treatment Classification


The project aims to leverage a comprehensive dataset containing various hematologic parameters such as haematocrit, haemoglobin, erythrocyte count, leucocyte count, thrombocyte count, MCH, MCHC, and MCV to develop machine learning models for classifying patients as either requiring in-patient or out-patient care. The dataset utilized in this study represents electronic health records collected from a private hospital in Indonesia. The project targets the healthcare sector;specifically, in planning and resource allocation for clinics and hospitals, where accurate classification of patients is crucial for optimizing staffing operations, ward capacity management as well as providing optimal medical care to patients.


## Documentation

[Dataset from Kaggle](https://www.kaggle.com/datasets/saurabhshahane/patient-treatment-classification)


## Business Problem

Healthcare providers often encounter challenges in efficiently classifying patients based on their care needs, particularly when relying solely on manual assessments of laboratory test results. The lack of a streamlined process for determining whether a patient requires inpatient or outpatient care poses a significant hurdle in optimizing resource allocation and enhancing operational efficiency within medical facilities.
In the dynamic healthcare landscape, VitaHealth-254 seeks to apply machine learning and AI to redefine patient management by empowering healthcare providers with data-driven tools that facilitate informed decision-making.
Envision a patient named Sarah, whose test results indicate the need for medical attention. However, Sarah's healthcare provider faces challenges in accurately determining the appropriate level of care based on the provided data alone.
Through Sarah's journey in navigating patient care classifications, VitaHealth-254 aims to revolutionize the patient experience by providing healthcare professionals with predictive tools that optimize resource allocation and enhance operational efficiency.
## Business Objectives

1.Improve Patient Care Classification:Develop a model that automates the process of categorizing patients based on their laboratory test results to ensure timely and appropriate treatment.Develop machine learning models to identify and quantify the influence of various hematologic parameters (e.g., haematocrit, haemoglobin, erythrocyte count) on the classification of patients

2.Optimize Resource Allocation:By accurately predicting patient classifications, optimize resource allocation within the hospital, including beds, staffing, and other medical resources.Ensure that the right resources are available to meet the needs of different patient categories, leading to improved efficiency and cost-effectiveness in resource utilization.

## Attribute/Feature Description

- HAEMATOCRIT /Continuous /35.1 / Patient laboratory - - test that measures the proportion of red blood cells in your blood


- HAEMOGLOBINS/Continuous/11.8 / Patient laboratory - test that measures the levels of hemoglobin in your blood

- ERYTHROCYTE/Continuous/4.65 / Patient laboratory -  test that measures how many red blood cells (RBCs) your blood contains.

- LEUCOCYTE /Continuous /6.3 / Patient laboratory - measures the number of white blood cells in your body

- THROMBOCYTE - measurement of platelets count in your blood.

- MCH-Mean corpuscular hemoglobin - measurement of the amount of hemoglobin in a red blood cell.

- MCHC/Continuous/33.6/ Patient laboratory - evaluate whether RBC are carrying an appropriate amount of hemoglobin(mean corpuscular hemoglobin concentration)

- MCV/Continuous /75.5/ Patient laboratory - help diagnose or monitor certain blood disorders, including anemia(mean corpuscular volume)

- AGE - Patient age

- SEX - Patient gender

- SOURCE - the class target in care patient and out care patient.
  
## Data Modelling

The models used for the project:
 - Baseline logistic model
 - Decision tree model
 - Random forest model

 The performance of the models are as shown below;
 
   | No | Model | AUC Score |
   |-|-|-|
   | 01 | Logistic Model | 77% |
   | 02 | Decision Tree  | 67% |
   | 03 | Random Forest  | 81% |

   Therefore proceeded with random forest as our best model.Random Forest has the highest AUC score, indicating its effectiveness in distinguishing between positive and negative instances.

## Recommendations
- Introduction of intermediate checkup station for all patients classified as inpatient(0) by the chosen model. This will allow for further evaluation by medical professionals who will ultimately determine whether overnight hospitalisation is required. This maintains the human touch in the process while accounting for the model's inaccuracy

- Equip the suggested intermediate station with a mix general practitioners and lab specialists and equipment for efficient human resource alolocation.

- Equip the intermediate station with state-of-the-art blood screening equipment. This will enable more fine-tuned diagnosis due to the increase of blood parameters tested for anomalies. Moreover, this will provide additional data that can be fed into he model to improve its performance over time.

- When planning for the overall patient capacity as well as appropriate staffing of the medical facility, the assumption of a 40% admission rate can be used to distribute resources appropriately.
   
## Conclusion
- Leveraging the dataset obtained in research, this project developed a predictive model (with 75% accuracy) for the classification of patients based on haematological features.​

- Furthermore, we we able to identify the need for an intermediate checkup station that would be used to provide additional specialized medical care for patients classified as needing overnight hospitalization.​

- This would have the two-fold effect of providing extra medical attention to high-risk patients while accounting for any misclassification by the model.
  
## Authors
- Rodgers Odhiambo
- Mohamed Ali
- David Kirianja
- Beatrice Kariuki
