from itertools import count
import re
from turtle import pos, position

def selecting_and_separenting_content(location, start_selection, end_selection):
    try:
        with open(location, 'r', encoding= 'UTF-8') as ranking_archive:
            content = ranking_archive.read()
            start = content.find(str(start_selection))
            final = content.find(str(end_selection))

            return content[start+len(start_selection):final]

    except: 
        print('Your location or another parameter is invalid')
        return 0

def opening_and_spliting_content(file_to_split, spliting_method):
    try:
        content = file_to_split.split(str(spliting_method))
        for line in content:
            line = line.strip()
    except: 
        print('Your file is invalid')
        return 0

    return content

def creating_new_file(location, file_content):
    try:
        with open(location, 'w', encoding='UTF-8') as new_file:
            for line in file_content:
                new_line = re.sub(r'[^a-zA-Z0-9,-áàâãéèêíïóôõöúçñÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇÑ\b]','', line)
                new_file.write(str(new_line + "\n"))
            
        return_file = open(location, 'r', encoding='UTF-8')
        return return_file.read()

    except:
        print('Your file location have a problem')
        return 0

def ranking_generator(split_and_organized_file, ranking_position, size_spliting, final_position, path_ranked):
    with open(path_ranked, 'w', encoding='UTF-8') as ranked_file:
        ranking = split_and_organized_file.split(',')
        position = 1
         
        full_rotation = 0

        while position < final_position:
            new_line = ''
            count = 0
            position_check = 0
            if full_rotation == 1:
                position = position + 1    

            for line in ranking:
                count = count + 1
                new_line = new_line + ' ' + line

                if count == size_spliting and position_check == 1:
                    print('yeah')
                    print(position)
                    ranked_file.write(new_line)
                    position = position + 1
                    position_check = 0
                    new_line = ''
                    count = 0
                    full_rotation = 0
                    break

                elif count == size_spliting:
                    count = 0
                    new_line = ''

                if count == ranking_position and int(line) == position:
                    print(line)
                    position_check = 1

                full_rotation = 1