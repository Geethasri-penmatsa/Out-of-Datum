
# Tagging data via characteristics and structures

This repository is created for Capstone project DAEN 690. Team Name - Out of Datum. Our project scope is around extracting meta data via characteristics and structures.

## Abstract

The extensive use of personally identifiable information (PII), which has caused widespread concern, has accelerated the development of information and technology. Being able to identify PII is now more crucial than ever with the implementation of GDPR and CCPA, as well as the trend of individuals being more aware of how their personal information is being used and privacy concerns growing in several sectors. Businesses keep a lot of data and information on hand, both sensitive and non-sensitive. Therefore, we utilize regular expression to uncover patterns in order to determine which data includes Personally Identifiable Information (PII). Only in this way can PII be tagged to comprehend which is PII and non-PII. We take into account privacy factors before determining if the data contains PII and categorize the findings as sensitive or non-sensitive. We are focused on automatizing tagging for PII, or personally identifying information. We gathered structured, semi-structured, and unstructured data for analysis, as well as visualization and natural language processing (NLP) algorithm analysis to combine the regular expression and spaCy, Steam to detect PII. After scanning and carefully examining the data, and using privacy rules as a guide, our process will provide findings.


# Architecture Diagram

![Alt text](images/schematic.png?raw=true "Title")


### Bussines objective

The primary objective of this project is automation of tags that will identify the PII data. Apart from this, the value we intend to provide is the security of PII. We believe this will help the users and organizations to be aware of the existence of PII in their data and in turn, take necessary measures to protect this sensitive PII from unauthorized access.


### Solution Space

Our process helps users and organizations identify if any personal information is stored in the data by using meta data tags. Whenever a survey data is collected, user information is stored, medical/insurance records are collected there are chances of personal information being shared externally. This solution is for data protection and privacy. It helps us scan, detect and automatically tag data and columns that contain PII data.


### RESULTS 

Figure below shows us the data parsed to the routine. The regex identifies if there are any email id, ssn, phone numbers, credit card details, drivers in the text file that has been passed to the routine.

![Alt text](images/input.png?raw=true "Title")

Figure below  shows the function used to return the PII data in the text file. As a result, the text file contains the PII information such as the email address, phone number, and credit card.

![Alt text](images/output.png?raw=true "Title")


### Information about the files.

- The file umap patients dataset.ipynb script for UMAP of patients dataset.
- The file unstructregex.py contains script for functioning of the regex.
- The file  unstructregex.ipynb imports function from unstructregex.py to detect and scan the PII in the text.

### Steps to detect PII in unstructured dataset.

- Download any text file  which has PII such as SNN, Drivers, Credit card etc. 
- Downlaod unstructregex.py and unstructregex.ipynb. 
- Run the unstructregex.ipynb by providing input as your text file. 
- Voila, you can now see the PII detected in your file. 

![Alt text](images/web page.png?raw=true "Title")
