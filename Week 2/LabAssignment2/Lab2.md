## Lab 2: ¡Práctica de Python! 

**Goals:** 1) Create your very own python Program. 2) Replicate the tokenizer and segmenter tasks with different data

You will learn how to:
- modify python scripts to fit your needs
- run python scripts with your data

#### Suggestions: work in couples if necessary and adapt the Python scripts covered during class. Please don't hesitate to reach out if you need help. Tutorial to solve any issues on Tuesday 7/13 - 10-11am. I will post the answer on Friday 7/16. Have fun!

### Task 1: Create a Python program that:
Instructions:
1. asks for name and year of graduation of the user. <br/>
            **(Hint: for year of graduation we will need to modify the string to integer. ---> VARIABLENUM = int(input("1234"))**
2. append the input into two variables. 
3. print name and year of graduation
4. print message of congratulations if graduation is on or before 2021. <br/>
            **(Hint: use the lower than sign. ---> *if VARIABLENUM < 2021:*)**
5. print message of encouragement if graduation is in the future
6. then in the same program, ask the user for a sentence in Spanish with as many characters with orthograpic accents (i.e., tildes) as possible. Asks them to be creative. 
7. Import the regular expression module
8. search if the sentence has any *tildes*. Print a message that tells the user that you need to change all the *tildes* to characters with no *tildes*.
10. substitute all the characters with tildes to no accented characters <br/>
           **(Hint: you might need to use the *re.sub* function several times.**
11. print the sentence without any accented characters
12. else print a message saying that the sentence has no *tildes
13. change the sentence to lower case
14. print the complete sentence with no accented nor upper case characters. 


### Task 2: Run both the tokenizer and sentence segmenter scripts and print in Linux line by line the output<br/>
**Datos**: LowerIntermediate.txt <br/>
Instructions:
1. Run the tokenizer script and save the output '>' 
2. Run the segmenter script and save the output '>'
3. Note that the output is presented by default between spaces and commas
4. Use the 'sed' or the 'tr' command to print the output line by line 

Both the tokenized and segmented files should look like this:

![alt text][logo]

[logo]: https://github.com/falconrr/NLP4SPanish/blob/main/Media/Images/howtoprinttokens.PNG?raw=true "Logo Title Text 2"

![alt text][logo2]

[logo2]: https://github.com/falconrr/NLP4SPanish/blob/main/Media/Images/howtoprintsegments.PNG?raw=true "Logo2 Title Text 2"

#### What to submit?
1. a python script for Task 1
2. Screenshots of tokenizer and segmenter in action and the printing of the output line by line.
