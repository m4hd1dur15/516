
#vowels
IPA_dict = {
    "CMU":"IPA",
    "AA":"ɑ",
    #"AH":"ʌ",
    "AE":"æ",
    "AO":"ɔ",
    "AW":"aʊ",
    "AH":"ə",
    "AX":"ə",
    "AXR":"ɚ",
    "AY":"aɪ",
    "EH":"ɛ",
    "ER":"ɝ",
    "IH":"ɪ",
    "IY":"i",
    "IX":"ɨ",
    "UH":"ʊ",
    "UW":"u",
    "EY":"eɪ",
    "OW":"oʊ",
    "OY":"ɔɪ",
    "UX":"ʉ",
#consonants
    "B":"b",
    "CH":"tʃ",
    "D":"d",
    "DH":"ð",
    "DX":"ɾ",
    "EL":"l̩",
    "EM":"m̩",
    "EN":"n̩",
    "F":"f",
    "G":"g",
    "HH":"h",
    "H":"h",
    "JH":"dʒ",
    "K":"k",
    "L":"l",
    "M":"m",
    "N":"n",
    "NX":"ŋ",
    "NG":"ŋ",
    "NX":"ɾ̃",
    "P":"p",
    "Q":"ʔ",
    "R":"ɹ",
    "S":"s",
    "SH":"ʃ",
    "T":"t",
    "TH":"θ",
    "V":"v",
    "W":"w",
    "WH":"ʍ",
    "Y":"j",
    "Z":"z",
    "ZH":"ʒ"
}

# Step 1: open the text file

inputtext = open('inputstress.txt', 'r').read() #open and then read the text file

# print(inputtext)
# # Step 2: word tokenization

split_text = inputtext.split(',') # tokenize the words

# Step 3&4: converting the Arphabet to IPA

import re
import nltk
entries = nltk.corpus.cmudict.entries() #bring the CMU transcription in this variable

def findword(word):
    for entry in entries: 
        if word in entry:
            return list(entry)
final_list = []
ipa_words = []

for w in split_text: 
    current_word = findword(w)
    ipa_words.append(current_word)
for w in range(len(ipa_words)):#######
    final = [] ######
    if ipa_words[w] != None:
        for i in range(len(ipa_words[w][1])): ######
            if ipa_words[w][1][i] in IPA_dict:
                ipa = IPA_dict[ipa_words[w][1][i]]
                final.append(ipa)
            else:
                num = ipa_words[w][1][i][-1]
                cleaned = re.sub("[0-9]", "", ipa_words[w][1][i])
                ipa = IPA_dict[cleaned]
                back = ipa + num
                if num == '1':
                    back = f"""<font color = "red"> {ipa} </font>"""
                    final.append(back)
                elif num == '2':
                    back = f"""<font color = "blue"> {ipa} </font>"""
                    final.append(back)
                elif num == '0':
                    back = f"""<font color = "black"> {ipa} </font>"""
                    final.append(back)
    final_list.append(final)

with open("output.html", 'w') as output: #creat html where the output goes
    for item in final_list:
        item = "".join(item)
        output.write(f"""<h1>{item}<h1>""")

# # Step 5: Output the IPA transcription to a text file
# with open("output.html", 'w') as output:
    # output.write(input)


    
