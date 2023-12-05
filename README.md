
# Sentiment Analyzer

Analyze the sentiment of a text stored in a string or text file and understand the reason why your blogs and posts are not ranking up.
This Model is developed using Python3 programming language without using nltk package.



## How to use it ?
 - If you want to use it from online api, then visit "https://sentimentanalyzer.vercel.app/analyze?text=your+text+here" and it will return you a json object which contains output.
 - or you can download the source code of this model on your system and use it as you want.
 - Install Python3 on your system from [here](https://www.python.org/downloads/).
 - Download this repository from [here](https://github.com/saksham-joshi/Sentiment_Analyzer/archive/refs/heads/main.zip).
 - After downloading, extract the zip file and open the extracted folder.
## Files & Folders:
1. "app.py": It is a python file which is used to handle request on backend.
2. "Model" : This folder contains the main API. It contains files like :
    - "support_files": this folder is used by "Corrector_generator.ipynb" to generate "Corrector.json". 
    - "Corrector.json": this file contains all the words required to clean your given text which eventually increases accuracy and quality of output.
    - "Corrector_generator.ipynb": this is a jupyter notebook file of a python script which helps you to generate and update "Corrector.json".
    - "AnalystUtility.py": this file contains the implementation of neccesary formula required to create outputs.
    -  "Analyzer.py": this is the main file which contains the implementation and logic of this Analyzer. It contains two functions :
      
         1. Analyze_String(val : str) : this function takes string as input as returns a dictionary as output.
            
         2. Analyze_File(file_name : str) : this function takes file address as a input and returns a dictionary as output.
## Developer Info:
- Developed by Saksham Joshi.
- [@Portfolio](https://sakshamjoshi.netlify.app/)
- [@Linkedin](https://www.linkedin.com/in/sakshamjoshi27)
- [@GitHub](https://github.com/saksham-joshi)
- [@X(Twitter)](https://twitter.com/sakshamjoshi27/)

