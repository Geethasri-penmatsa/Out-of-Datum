import pandas as pd
import numpy as np
import re
from string import punctuation

# import phonenumbers

class PIIFilter:
    
    def identify_email(self, textString):
        regex = re.compile(r'[\w.+-]+@[\w-]+\.[\w.-]+')
        email_list = re.findall(regex,textString)
        email_list = [i.strip(punctuation) for i in email_list]
        return email_list
    
    def identify_ssn(self, textString):
        regex = re.compile(r'\b(?!000|.+0{4})(?:\d{9}|\d{3}-\d{2}-\d{4})\b')
        ssn_list = re.findall(regex,textString)
        return ssn_list
    
    def identify_phone_numbers(self, textString):
        regex = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
        phone_list = re.findall(regex,textString)
        
        rem = []
        for i in phone_list:
            ind = textString.index(i)
            # print(textString[ind-1], textString[ind+len(i)], i)
            res = []
            if ind-1 < len(textString):
                res.append(textString[ind-1].isalnum())
            if ind+len(i) < len(textString):
                res.append(textString[ind+len(i)].isalnum())
            if True in res:
                rem.append(i)
        for i in rem:
            phone_list.remove(i)
        
        return phone_list
    def identify_zip(self, textString):
        regex= re.compile(r"(\b\d{5}-\d{4}\b|\b\d{5}\b\s)")
        zip_list = re.findall(regex,textString)
        zip_list = [i.strip() for i in zip_list]
        return zip_list
    def identify_credit_card(self, textString):
        # needs similar treatment as phone numbers?
        regex = re.compile(r'(?:\d{4}[ \-]?){3}\d{4}')
        card_list = re.findall(regex,textString)
        return card_list
    def identify_dl(self, textString):
        # need to test if working
        regex = re.compile(r'^[A-Z](?:\d[- ]*){14}$')
        dl_list = re.findall(regex,textString)
        return dl_list
    
    def filterPii(self, inputtext):
        analysis_text = {}
        analysis_text['email'] = self.identify_email(inputtext)
        analysis_text['SSN'] = self.identify_ssn(inputtext)
        analysis_text['phone'] = self.identify_phone_numbers(inputtext)
        analysis_text['zip'] = self.identify_zip(inputtext)
        analysis_text['credit'] = self.identify_credit_card(inputtext)
        analysis_text['dl'] = self.identify_dl(inputtext)
        
        #if analysis_text == "":
            #print("This may not contain PII.")
            #return
        return analysis_text

