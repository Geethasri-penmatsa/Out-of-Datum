
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
