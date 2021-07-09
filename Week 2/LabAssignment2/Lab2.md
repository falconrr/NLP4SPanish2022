## Lab 2: ¡Práctica de Python! 

**Goals:** 1) Create your very own python Program. 2) Replicate the tokenizer and segmenter tasks with different data

You will learn how to:
- modify python scripts to fit your needs
- run python scripts with your data

#### Suggestions: work in couples if necessary and adapt the Python scripts covered during class. Tutorial to solve any issues on Wednesday 7/14. 

### Task 1: Create a Python program that:
Instructions:
1. asks for name and year of graduation of the user. <br/>
            (Hint: for year of graduation we will need to modify the string to integer. I.e., *VARIABLE = int(input("abcde"))
2. append the input into two variables. 
3. print name and year of graduation
4. print message of congratulations if graduation is on or before 2021. <br/>
            (Hint: use the lower than sign. I.e., *if VARIABLE < 2021:*)
5. print message of encouragemnt if graduation is in the future
6. then in the same program, ask the user for a sentence in Spanish with as many characters with orthograpic accents (i.e., tildes) as possible. Asks them to be creative. 
7. Import the regular expression module
8. search if the sentence has any *tildes*. Else print a message saying that the sentence has no *tildes
9. print a message that tells the user that you need to change all the *tildes* to characters with no *tildes*. <br/>
10. substitute all the characters with tildes to no accented characters 
            (hint: you might need to use the *re.sub* function several times.
11. print the sentence without any accented characters
12. change the sentence to lower case
13. print the complete sentence with no accented nor upper case characters. 


### Task 2: Run both the tokenizer and sentence segmenter scripts
**Datos**: LowerIntermediate.txt
Were the Python programs succesful in tokenizing and segmenting the text?
Did you find any issues? If so, what type of issues? Suggest a solution. 
