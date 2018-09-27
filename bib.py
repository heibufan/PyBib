# Parse Mendeley Bib file and retrieve link key to use in markdown to cite

from pprint import pprint 
import re 

folder_path = 'C:\\Users\\cinep\\Desktop\\Lanbufan-Razer\\1_ACADEMIC-LIFE\\1_UBC-PhD-PROGRAM_2014-2019 (m)\\3_DOCTORAL-DISSERTATION (M)\\4_PhD-Proposal\\1_Writing\\1_Memoing\\'

file_string = 'PHDD-BIB.bib'
f = open(folder_path + file_string, 'rb')

neirong = f.read()
neirong = neirong.decode('utf8')

neirong_list = neirong.split('\n')

ref_list = []
author_list = []
ref_list_raw = []

for article in neirong_list:
    ref_content = []
    if (article.startswith('@article') or article.startswith('@book') or article.startswith('@misc')):
        # clean string
        article = article.replace('@article{', '')
        article = article.replace('@book{', '')
        article = article.replace('@misc{', '')
        article = article.replace(',' , '')
     
        if len(article) != 0:
        
            ref_list_raw.append(article)
            
            
            # need to split alpha from num to facilitate searchability
            # beta
            # three basic string structure
            # 1. Long2007
            # 2. Long
            # 3. Long2007a
            
            if article[-1].isnumeric():
                # case 1
                year  = article[-4:]
                name = article[:-4]
          
            else:
                # last symbol is not numeric, so we are left with either 2. or 3.
                if article[-2].isnumeric():
                    # case 3
                    year = article[-5:]
                    name = article[:-5]
                    
                else:
                    # we are left with case 2
                    year = 'XXXX'
                    name = article
                    
            ref_content = [name, year]
            ref_list.append(ref_content)
            author_list.append(name)
                    
                
#pprint(ref_list)

# gui menu to change information

print('adam pick option 3 to start')

print('1-find ref, 2-format red, 3-check if R MARKDOWN ref is accurate')

choice = input()

if choice  == "1":

    print('1-full name search\n2-first letter only\n')
    
    choice_1_name = input()
    
    if choice_1_name == '1':
        
        print('what author are you looking for?')
        
        author_to_find = input()
        
        if author_to_find in author_list:
            print('found him')
            
    else:
    
        print('enter author first letter?')
        
        author_first_letter = input()
        
        for name in author_list:
        
            if name.startswith(author_first_letter):
                print(name)
        
        
       
if choice  == "3":

    print('enter markdown format ref?\n')
    
    markdown_ref = input()
    
    print('\n')
    
    if markdown_ref in ref_list_raw:
        print('current entry is accurate\n')
        
    else:
        print('current entry not found\n')
        print('what to do next?\n 1-print full list of raw ref\n 2-print full list of author\n 3-print full list of author and year\n')
        
        choice_2 = input()
        
        if choice_2 == '1':

            pprint(ref_list_raw)
            
        elif choice_2 == '2':
            # print list of author starting with first letter only
            
            pprint('1-print only author that start with first letter of scholar you entered? y or n\n')
            
            author_name_choice = input()
            
            if author_name_choice == 'y':
                
                for name in author_list:
                    if name.startswith(markdown_ref[0:1]):
                        print(name)
                        
            if author_name_choice == 'n':
            
                pprint(author_list)
            
        elif choice_2 == '3':
            # only print the ones starting with first letter of ref entered
            for ref_content in ref_list:
                if ref_content[0].startswith(markdown_ref[0:1]):
                    print(ref_content)
                    
            #pprint(ref_list)
        
        else:
            print('invalid selection')
        
            
    




        
