import re

pattern='''I felt so happy today 😀! It was a wonderful day 😄, and everything went perfectly 😁. Meeting my friends made me even happier 😊. We all shared stories and laughed a lot 😃. Such a blessed day 😇. Later in the day, I received a surprise gift 😁 which made me feel ecstatic 😄. My dog was also in a playful mood, adding to the joy 😇. We decided to watch a funny movie that kept us laughing 😃. After the movie, we had a delicious dinner, and the dessert was heavenly 😁. The day ended on a high note with everyone feeling happy and content 😀. My friends and I took a lot of photos with happy emojis 😄. We also shared some of these moments on social media, receiving lots of likes and happy comments 😃. It was truly a day to remember 😊. Even the weather was perfect, which added to the overall joy 😇'''
search= re.compile(r'[\U00010000-\U0010ffff]', flags=re.UNICODE)
           
matches=search.findall(pattern)

for match in matches:
    print(match)






