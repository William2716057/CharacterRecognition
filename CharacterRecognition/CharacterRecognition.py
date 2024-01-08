import easyocr 

reader = easyocr.Reader(['en'])

result = reader.readtext('images/file.jpg')

print(result)

for (bbox, text, prob) in result:
    print(text)