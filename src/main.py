# IMPORTS
import os, sys
import numpy as np
from PIL import Image

# SET THE NAME OF THE ART TO THE FILENAME
art_name = sys.argv[1].split('.')[0]

# SET THE PATH FOR THE GENERATED DIR
directory = os.path.join(os.getcwd(),art_name)

# IF THE ART NAME ALREADY HAS A FOLDER IN SAME RELATIVE PATH
if os.path.exists(directory):
    for f in os.listdir(directory): # DELETE ALL FILES
        os.remove(os.path.join(directory, f))
    os.removedirs(directory) # DELETE THE DIR

os.makedirs(directory) # CREATE THE TOP LEVEL DIR

# CREATE HTML
with open(os.path.join(directory,art_name+".html"), "w") as file:
    file.write('<!DOCTYPE HTML><html><head><link rel="stylesheet" href="'+art_name+'.css"></head><body><div class="'+art_name+'"></div></body></html>')

# GENERATE CSS FROM IMAGE
css_string = '{\nmargin: 0 auto;\nwidth:1px;\nheight: 1px;\nbox-shadow: '

img = Image.open(sys.argv[1]) # LOAD IMAGE FILE INTO A PIL OBJECT
arr = np.array(img.getdata()) # CREATE NP PIXEL ARRAY FROM PIL OBJECT

# ITERATE OVER THE PIXELS IN THE NP ARRAY
for i in range(img.size[0]):
        for j in range(img.size[1]):
            current = img.getpixel((i, j)) # GET THE CURRENT PIXEL
            
            if(sys.argv[1].split('.')[1] == 'png'): # IF WE NEED TRANSPARENCY / ITS A PNG
                pixel = str(i)+'px '+str(j)+'px rgb('+str(current[0])+','+str(current[1])+','+str(current[2])+','+str(current[3])+'), '
            else: # IF THE IMAGE DOES NOT HAVE TRANSPARENCY
                pixel = str(i)+'px '+str(j)+'px rgb('+str(current[0])+','+str(current[1])+','+str(current[2])+'), '
            
            css_string+=pixel # ADD THE PIXEL CSS TO THE CSS CODE

css_string = css_string[:-2] # REMOVE TRAILING SPACE AND LAST COMMA
css_string += '}' # ADD THE END BRACKET

# CREATE CSS
with open(os.path.join(directory,art_name+".css"), "w") as file:
    file.write('.' + art_name + css_string)

# FINAL OUTPUT
print(os.getcwd())
print('|__ ' + art_name + '\t\t+')
print('|____ ' + art_name + '.html' + '\t+')
print('|____ ' + art_name + '.css' + '\t+')