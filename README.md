# Tool-getData
- This project contain all the tool python file to get the photo, change the data form and some small change in VOC form.
## 1.dataGet.py
- This file is to get the photo data by using the web crawler.
## 2. changeXMLfile.py
- This file is to change the VOC's xml file after you changing the data path, and you can rewrite the folder, class name, path by using this py file.
## 3. deleteXMLLabel.py
- This file should use after you use the changeXMLfile.py to delete the title of the xml, but it also works without using this py file.
- We just want the xml file looks good, so we write this file.

## 4. imageSetCreate.py
- This file is to create the ImageSet for Voc data form.This is a necessary step for format conversion. 

## 5.reFileName.py
- This file is to change the photo file name to pure number file name. Just to make the file look comfortable.

## 6. VocToCOCO.py
- This file is to change our data form, from VOC to COCO by imageSet we created before.


