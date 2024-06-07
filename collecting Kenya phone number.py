#seaching the keyword COVID-19 From the variable pattern below
import re

pattern='''Contact our customer service at +254712345678 for inquiries. You can also reach our support team at 0723456789 or our Nairobi office at +254701234567. In case of emergencies, dial +254798765432. Our WhatsApp number is 0709876543. If you need to contact our Mombasa branch, call +254723456789. Additionally, our Eldoret office can be reached at 0745123456. Don't forget to save our Kericho office number, which is +254765432123, in case you need assistance. For those in Kisumu, call +254745678912. Our customer feedback line is 0708123456. For bulk orders, contact our sales team at +254709876543. In case you have any issues with our products, please reach out to our technical support at 0712345678. You can also contact our accounting department at +254798123456 for billing inquiries. Our customer care in Nakuru can be reached at 0712345678. For general inquiries, use the number +254702345678. Our hotline for urgent issues is +254711234567. Thank you for choosing our services.
'''
#search= re.compile(r"[+254]\d\d\d\d\d\d\d\d\d\d\d\d")
#search= re.compile(r"[+254]\d{12}")
search= re.compile(r"[+254]+\d{9}")
matches=search.finditer(pattern)

for match in matches:
    print(match)

