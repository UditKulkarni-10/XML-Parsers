#Udit Kulkarni
#Xml parser that takes files in from a folder edits some of the values and then
#places them in an output folder while still keeping the intial input file
#05-27-2019


import xml.etree.ElementTree as et
import os
from shutil import copyfile, copy2
from pathlib import Path

start_directory = "C:\\Users\\kulkudi\\Documents\\trialxml"
end_directory = "C:\\Users\\kulkudi\\Documents\\outputxml"

if not os.path.exists(end_directory):
    os.makedirs(end_directory)


#Copies the initial files into the output directory
for file in os.listdir(start_directory):
    filename = os.fsdecode(file)
    if filename.endswith(".xml"):
        file_new = os.path.join(start_directory, filename)
        copy2(file_new, end_directory)
        #os.remove(file_new) ----> deletes the files placed in the input folder
        #file_to_edit = os.path.join(end_directory, file_new)

    else:
        print("there are some files that are not in the .xml format")
        continue
        

#edits the copied files in the output directory

for file in os.listdir(end_directory):
    filename2 = os.fsdecode(file)
    if filename2.endswith(".xml"):
        file_new2 = os.path.join(end_directory, filename2)
        tree = et.parse(file_new2)
        root = tree.getroot()


        #--------------------------------------------------------------------------
        #This section can be changed in terms of the xml you have and what you want
        #change in said xml
        #---------------------------------------------------------------------------

        
        chng = tree.find("./book/author").text = "udit k"

        for child in root:
            
            child.find("author").text = "udit kul"
            print(child.attrib, child.find('author').text, child.find('genre').text)
            tree.write(file_new2)

        #----------------------------------------------------------------------------

        #Renaming the file in the output folder
        p = Path(file_new2)
        file_name = p.stem
        ext = p.suffix
        new_name = "{}_{}".format(file_name, "edited")
        p.rename(Path(p.parent,new_name + ext))
        
    else:
        print("There are files in the folder that are not in the xml format")
        continue


