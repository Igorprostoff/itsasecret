#from googletrans import Translator
#from google.cloud import translate
import io
import pandas as pd 
import csv
import os 
#from translate import Translator
from yandex_translate import YandexTranslate
translate = YandexTranslate('trnsl.1.1.20190725T204932Z.576c25374e2316c8.3213b309961fe264e1ca2ef1feedee26c8300aa6')
#resTable = io.open("res.csv", "w", encoding="UTF-8")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/igorp/Desktop/mobdev-project-45b1e704b3fa.json"
benchOrig = io.open("bench.txt", "r", encoding="UTF-8")
#translate_client = translate.Client()
#resTable = pd.read_csv("res.csv")
bench=""
for line in benchOrig:
    bench+=line
#translator = Translator(to_lang='ru')
res = [[],[]]
print(len(bench))
with open('res.csv', 'w', newline='') as csvfile:
    while(True):
        if(bench.find("Description:")!=-1):
            rationaleIndex = bench.find("Rationale:")+10
            descriptionText = bench[bench.find("Description:")+12:rationaleIndex-10]
            #print("DESCRIPTION INDEX ", bench.find("Description:"))
            #print("RATIONALE INDEX ", rationaleIndex)
            #print("AUDIT INDEX", bench.find("Audit:"))
            rationaleText = bench[rationaleIndex:bench.find("Audit:")]
            #print("///", translator.translate(descriptionText, dest='ru').text, "***", translator.translate(rationaleText,dest="ru").text, "\\\\\\")
            bench = bench[bench.find("Audit:")+6:]
            transDescription = translate.translate(descriptionText, 'en-ru')['text']
                                #translator.translate(descriptionText, dest='ru').text
            transRationale = translate.translate(rationaleText, 'en-ru')['text']
            
            spamwriter = csv.writer(csvfile, delimiter=';')
            spamwriter.writerow([transDescription, transRationale])
        else:
            break
﻿Игорь Простов приглашает вас на запланированную конференцию: Zoom.

Тема: Зал персональной конференции Игорь Простов

Подключиться к конференции Zoom
https://us04web.zoom.us/j/5668823751?pwd=ZzNVSlZRTk93Rm1lYUN2SG1XNHp5QT09

Идентификатор конференции: 566 882 3751
Код доступа: 4v05q2


