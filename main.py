from googletrans import Translator
import csv


pl = "PL"
eng = "EN"

translator = Translator()


with open('in.tsv') as in_file:
    with open('out.tsv', 'w') as out_file:
        writer = csv.writer(out_file)
        for row in csv.reader(in_file):
            if row:
                translation = translator.translate(row[0], dest=eng, source=pl)
                writer.writerow([translation.text])