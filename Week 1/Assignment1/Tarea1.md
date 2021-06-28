## ¡La práctica es clave!

**Datos**: LowerBeginner.txt

1.  ¿Cuántas líneas, palabras y caracteres tiene el texto?
2. ¿Qué hace la siguiente línea de código? Explica la función de cada comando. <br/>
  `$ sed 's/[^a-zA-Z]\+/\n/g' < LowerBeginner.txt | sort | uniq -c | sort -nr | sed 10q`
  
3. ¿Cuáles son las 20 palabras más frecuentes del corpus?
4. Escoge cualquier tipo de afijo gramátical o léxico que te interese. ¿Cuántas veces lo utilizaron los estudiantes?
5. ¿Qué hace la siguiente línea de código? Explica la función de cada comando.<br/>
  `$ grep --color '\<a\w*a\>' LowerBeginner.txt`
6. Remueve los saltos de línea html que se copiaron al texto `<br/>)`

#### Github 
Vamos a descargar el repositorio del curso en GitHub. Con él ustedes tendrán los materiales más actualizados cada vez que yo actualice el repositorio. 
- Si no sabes qué es Github, aquí hay un video ilustrativo:  <br/>
<a href="https://www.youtube.com/embed/w3jLJU7DT5E
" target="_blank"><img src="http://img.youtube.com/vi/w3jLJU7DT5E/0.jpg"  
alt="GitHub" width="240" height="180" border="10" /></a>
- Descarga [Github Desktop](https://desktop.github.com/)
- Clona el repositorio: <br/>
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")