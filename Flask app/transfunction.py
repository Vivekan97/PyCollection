from requests import request
import re

# To check for date and phone numbers
re_query_date = r'\d{2,4}[-/.|]\d{2}[-/.|]\d{2,4}'
re_query_phonenums = r'^(\+\d{1,2}\s?)?1?\-?\.?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'

# Official Indian languages supported by google-inputtools
language_codes = {'kannada': 'kn', 'english': 'en', 'gujarati': 'gu', 'tamil': 'ta',
                  'hindi': 'hi', 'telugu': 'te', 'marathi': 'mr', 'assamese': 'as',
                  'bengali': 'bn', 'malayalam': 'ml', 'nepali': 'ne', 'oriya': 'or',
                  'punjabi': 'pa', 'sanskrit': 'sa', 'urdu': 'ur',
                  }


def transliteration(text, language):

    user_inputs = text.split(" ")
    user_inputs = [element for element in user_inputs if element.strip()]

    language = str(language).lower()
    # print(user_inputs)
    # Correction made here to display numbers too by adding try and removing for lang_code
    final = ''
    lang_code = language_codes[language]
    for user_input in user_inputs:
        try:
            if type(float(user_input)) == float or type(int(user_input)) == int:
                final += " "+user_input

        except:
            if re.findall(re_query_date, user_input) or re.findall(re_query_phonenums, user_input):
                final += " "+user_input
            else:
                try:
                    new_req = request(url='https://inputtools.google.com/request?text='+user_input +
                                      '&itc='
                                      + lang_code + '-t-i0-und&num=13&cp=0&cs=1&ie=utf-8&oe=utf-8&app=demopage',
                                      method='GET')
                    final += " "+new_req.json()[1][0][1][0]
                except:
                    final += " "+user_input
    return final


if __name__ == '__main__':
    print(transliteration("Good Morning 2021 Phone +91 8635261718"
                          "date is 22-09-2016 ", 'tamil'))
