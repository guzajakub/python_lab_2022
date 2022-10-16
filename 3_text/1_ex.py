# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os


def delete_given_words(file, outfile, words_to_delete=["się", "i", "oraz", "nigdy", "dlaczego"]):
    fin = open(file, encoding='utf')
    fout = open(outfile, "w+", encoding='utf')
    for line in fin:
        new_line = " ".join([word for word in line.split() if word not in words_to_delete])
        fout.write(new_line)
        fout.write("\n")
    fin.close()
    fout.close()


current_path = os.path.abspath(os.getcwd())
file_to_delete = f"{current_path}\\examples\\words"
delete_given_words(file_to_delete, outfile=f"{current_path}\\examples\\words_clear")