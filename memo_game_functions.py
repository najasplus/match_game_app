# -*- coding: utf-8 -*-
#!/usr/bin/python3
import random
import pandas
import os

def analyze_list_files():
    vocabulary_buttons = []
    wordlist_dir = "static/word_lists/"
    filenames = os.listdir(wordlist_dir)
    
    filelist = [ filename for filename in filenames if filename.endswith( ".tsv" ) ]
    
    for item in filelist:
#        print(item)
        list1,list2 = parse_tab_delimited(wordlist_dir + item)
        dict_item = {
            "vocab": item[:-4],
            "num_words": len(list1),
            "list1": list1,
            "list2":list2
            }
        vocabulary_buttons.append(dict_item)
    return vocabulary_buttons

def parse_tab_delimited(input_tsv):
    """Read tab-delimited text file, 
    return first two columns as lists,
    store them in global variables list1 and list2"""
    global list1
    global list2
    input_df = pandas.read_csv(input_tsv, sep='\t', encoding='utf-8', header=None)
    list1 = list(input_df[input_df.columns[0]])
    list2 = list(input_df[input_df.columns[1]])
    return list1, list2

def draw_elements(total_l1, total_l2, num_elements):
    zipped_lists = list(zip(total_l1, total_l2))
    #dedup lists
    sorted_zipped = sorted(zipped_lists, key = lambda x: x[1])
    deduped_indices = [i for i in range(0, len(total_l1)) if sorted_zipped[i][1] != sorted_zipped[i-1][1] ]
    dedup_lists =  [ sorted_zipped[j] for j in deduped_indices ]
    print(dedup_lists)
    print(len(dedup_lists))
    print(num_elements)
        
    draw_indices = random.sample(range(0, len(dedup_lists)), num_elements)

    list_subset = [dedup_lists[i] for i in draw_indices] 

    out_list1, out_list2 = zip(*list_subset)
#    print(out_list1)
    return out_list1, out_list2
