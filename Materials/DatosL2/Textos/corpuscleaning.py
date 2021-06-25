import os
import glob
import re
import sys

#ifile = open("data/en_sp_14_19_0.5_14_gfh.txt", mode='r', encoding='utf-8')
#texto = ifile.read()
#ifile.close()
#print(texto)

def cleaner(word):
  #word = re.sub(r'^https?:\/\/.*[\r\n]*', '', word, flags=re.MULTILINE)
  word = re.sub(r'((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*', '', word, flags=re.MULTILINE)
  #word = re.sub(r'(?::|;|=)(?:-)?(?:\)|\(|D|P)', "", word)
  word = re.sub(r'ee.uu', 'eeuu', word)
  word = re.sub(r'\#\.', '', word)
  word = re.sub(r'#', '', word)
  word = re.sub(r'\n', '', word)
  word = re.sub(r',,', ' ', word)
  #word = re.sub(r'\-', ' ', word)
  word = re.sub(r'\.{3*}', ' ', word)
  word = re.sub(r'a{2,}', 'a', word)
  word = re.sub(r'é{2,}', 'é', word)
  word = re.sub(r'i{2,}', 'i', word)
  word = re.sub(r'ja{2,}', 'ja', word)
  word = re.sub(r'á', 'á', word)
  word = re.sub(r'é', 'é', word)
  word = re.sub(r'í', 'í', word)
  word = re.sub(r'ó', 'ó', word)
  word = re.sub(r'ú', 'ú', word)
  #word = re.sub('[^a-zA-Z]', ' ', word)
  word = re.sub('xx+', '', word)
  word = re.sub('hh+', '', word)
  word = re.sub('/', '', word)
  word = re.sub(' +', ' ', word)
  word = re.sub('<br>', '', word)
  word = re.sub(r'\S+=', r'', word)
  #list_word_clean = []
  return word

save_path = '/mnt/c/Users/desun/IU_OneDrive/4thSemester/LING715_CLSeminar/Project/L715SpanishNLPPipeline/Data/CompleteData/output'

for file in glob.glob("*.txt"):
    #print(file)
    myfile = open(file,"r")
    lines = myfile.readlines()
    lines = [x.rstrip("\n") for x in lines]
    lines = [' '.join(lines)]
    #print(lines)
    for line in lines:
        #print(line.strip())
        texto = cleaner(line)
        print(texto)
        fullname = os.path.join(save_path, file)
        filex = open(fullname, 'w', encoding='utf-8')
        filex.write(texto)
