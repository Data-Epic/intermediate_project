# Importing re library for extracting regular expressions
import re
import pandas as pd

# The content forest
text="""
Important dates to remember include 25/12/2023 for Christmas, 01/01/2024 for New Year, and 14/02/2024 for Valentine('s Day. Additionally, 
our project deadlines are 12/25/2023 and 2023-12-25. The next meeting is scheduled for 11/11/2023 and 2023-11-11. Our quarterly review will be on 03/31/2024. 
The company picnic is planned for 06/15/2024. The annual conference will be held from 10/10/2024 to 10/12/2024. Mark your calendars for 07/04/2024, 
which is Independence Day. Our fiscal year ends on 09/30/2024. We have a training session on 08/20/2024. The mid-year review is set for 05/15/2024. 
The product launch is scheduled for 04/10/2024. The team-building retreat will be on 09/05/2024. Remember to submit your reports by 02/28/2024. 
The audit will take place on 12/01/2024. Our client meeting is on 01/15/2024. The board meeting is on 11/20/2023. Our strategy session will be held on 03/10/2024. 
The marketing campaign kicks off on 07/01/2024. The software release date is 08/01/2024. We have a vendor meeting on 06/01/2024. The contract signing is on 04/05/2024. 
Our holiday party is on 12/15/2024. The performance reviews start on 10/01/2024. The financial report is due on 11/01/2024. The sales target review is on 09/10/2024. 
The recruitment drive begins on 02/15/2024. Our CSR event is on 05/20/2024. The employee wellness program starts on 01/20/2024. 
Our internship program commences on 06/01/2024. ''The CEO')s address will be on 07/15/2024. The community outreach is scheduled for 08/25/2024.
"""

# Using findall method from re library to extract DD/MM/YY library
date_list = re.findall("[0-3][0-9]/[0-1][0-9]/[0-9]{4}", text)
print(date_list)

# Using DataFrame class from Pandas to tabulate the dates
df = pd.DataFrame(date_list, columns=["Date"], index= range(1,len(date_list)+1))
print(df)

