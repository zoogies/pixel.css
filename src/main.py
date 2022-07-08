import os, sys

try:
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

    # CREATE CSS
    with open(os.path.join(directory,art_name+".css"), "w") as file:
        file.write('.' + art_name + '{}')

except Exception as e:
    print("An error has occurred.")
    print(e)