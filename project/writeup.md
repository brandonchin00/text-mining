1. Project Overview [~1 paragraph] What data source(s) did you use and what technique(s) did you use analyze/process them? What did you hope to learn/create?

I used Wikipedia Democratic Party Page and Communism Page. I did a total word count for the number of words in both articles; a frequency for the number of different words in the article; a natural language analyzer for each line for both articles; and a similarity comparison for one of the articles. I used the communism page for one of the comparison functions. I hoped to understand how to convert most HTML files into text file. 

2. Implementation [~2-3 paragraphs] Describe your implementation at a system architecture level. You should NOT walk through your code line by line, or explain every function (we can get that from your docstrings). Instead, talk about the major components, algorithms, data structures and how they fit together. You should also discuss at least one design decision where you had to choose between multiple alternatives, and explain why you made the choice you did.

The data I pulled was from Wikipedia. I used two HTML articles then converted them to a text file. Since python reads text files easier, I wanted to then analyze them line by line for each article. Since the data is one lump sum, it was important that I had to split up each line for python to understand. Throughout the functions, you will see me dividing the line up for python’s functions to analyze. For situations where I need to measure the frequency of different words, I needed to divide the lines up so that I can use the dictionary to distinguish a repetitive word. But one of the complex problems I encountered was using natural_word() and similarity()

When I entered natural_word() function where it measures the sentiment, I had trouble using it to measure the overall sentiment. I created a test.py to test my code before posting it on my final version. Instead of measuring the overall sentiment, I measured the sentiment per line. 
Using similarity(), I encountered an issue with it scanning individual words for similarities and outputting 3. Overall, thefuzz attempt was not successful but nltk.sentiment was. 

3. Results [~2-3 paragraphs + figures/examples] Present what you accomplished:
If you did some text analysis, what interesting things did you find? Graphs or other visualizations may be very useful here for showing your results.
If you created a program that does something interesting (e.g. a Markov text synthesizer), be sure to provide a few interesting examples of the program's output.

I discovered that there are more words in Democratic_Party_(United_States) than Communism. 
Total number of words: 13002 (Democratic)
	Total number of words: 11349 (Communism)
I calculated the frequency of the words for each document and pprint the results but I was unable to figure out how to organize it to properly format it. I attempted to organize it in test.py but it was unsuccessful. 

After running the sentiment functions for both files. I was really intrigued to discover that the communism Wikipedia page had a higher negative sentimental by approximately 0.01 while the democratic sentimental average was around 0.0 for each line in the article.

For the similarity output, I was not able to pull any data from it but 3(s). I will double back to fix this issue once I thoroughly understand what went wrong. 

I didn’t copy and paste any of the outputs because it was unorganized and excessively long due to pprint, but each function (but similarity()) will work properly if executed.

4. Reflection [~1 paragraph] From a process point of view, what went well? What could you improve? Other possible reflection topics: Was your project appropriately scoped? Did you have a good plan for testing? How will you use what you learned going forward? What do you wish you knew before you started that would have helped you succeed?

The assignment was much more fun than the last finance assignment. I enjoyed being creative and taking the coding knowledge I learned from exercises and applying it to topics I was curious about. What I could do better next time is taking more time to learn how to organize data structures. Achieving a proper output isn’t the final step. Organizing the data afterward is the most important step because it’s difficult to analyze without organization. The project was appropriately scoped because it allowed us to test our skills and learn a few new ones through tutorials online. I used a separate test.py to test my code before implementing it into the final version. Going forward, I can use the sentiment checker to examine news articles for bais because it’s becoming difficult to detect bias newspapers. What I wish I knew was how to properly format a text file for analysis. I struggled for countless hours to attempt to format it right so the python program could analyze it. Overall I think the was a good experience. 
