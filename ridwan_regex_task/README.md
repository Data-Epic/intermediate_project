# WEEK ONE TASK

## Extracting "COVID-19" Mentions Using Regex

The task script use a regular expression (regex) pattern in Python to extract all occurrences of the keyword "COVID-19" from the given text in a case-insensitive manner. The script scans through the text for any place mentions of "COVID-19" and captures all the instances, regardless of letter casing.

The regex pattern that was used is **"(?i)\bCOVID-19\b"**

- **"(?i)"** enables case-insensitive matching.
- **"\b"** matches a word boundary to ensure "COVID-19" is matched as a whole word.
- **"COVID-19"** exact string to match, case-insensitively.
- **"\b:"** Another word boundary to ensure "COVID-19" is captured as a whole word.

When the script run, it a list all occurrences of "COVID-19" found in the text. 

These was the output:

['COVID-19', 'COVID-19', 'COVID-19', 'COVID-19', 'COVID-19', 'COVID-19', 'COVID-19', 'COVID-19', 'COVID-19', 'COVID-19', 'COVID-19', 'COVID-19', 'COVID-19', 'COVID-19', 'COVID-19', 'covid-19', 'COVID-19', 'COVID-19', 'COVID-19', 'COVID-19', 'covid-19', 'COVID-19']
