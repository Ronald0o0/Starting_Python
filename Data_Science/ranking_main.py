from functions.ranking_file import *

selected_content = selecting_and_separenting_content('c:/Users/Dalmira/Desktop/Starting_Python/Data_Science/archives/FINAL.txt', 'CIÊNCIAS ECONÔMICAS (BACHARELADO)', 'CIÊNCIAS SOCIAIS')

splited_content = opening_and_spliting_content(selected_content, '/')

new_file = creating_new_file('c:/Users/Dalmira/Desktop/Starting_Python/Data_Science/archives/New_file.txt', splited_content)

ranking_generator(new_file, 4, 12, 426, 'c:/Users/Dalmira/Desktop/Starting_Python/Data_Science/archives/ranked_final_file.txt')