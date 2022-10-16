# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
change_structure = {
    "i": "oraz",
    "oraz": "i",
    "nigdy": "prawie nigdy",
    "dlaczego": "czemu",
}


def change_words(file, outfile):
    fin = open(file, mode='r', encoding='utf')
    fout = open(outfile, mode="w+", encoding='utf')
    new_line = []
    for line in fin:
        for word in line.split():
            if word in change_structure.keys():
                new_line.append(change_structure[word])
            else:
                new_line.append(word)
        fout.write(" ".join(new_line))
        new_line = []
        fout.write("\n")
    fin.close()
    fout.close()


current_path = os.path.abspath(os.getcwd())
file_to_delete = f"{current_path}\\examples\\text_for_2nd_exercise"
change_words(file_to_delete, outfile=f"{current_path}\\examples\\2nd_ex_replaced")