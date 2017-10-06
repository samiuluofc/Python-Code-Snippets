def my_paragraph(full_text):
    all_para = full_text.split('\n\n')
    num_of_para = len(all_para)
    return all_para, num_of_para


def my_sentence(para):
    num_of_sen = para.count('.')+para.count('?')+para.count('!')
    return num_of_sen

def word_norm(para):
    para = para.replace(".","")
    para = para.replace("?","")
    para = para.replace("\n","")
    para = para.replace("!","")
    para = para.replace(";","")
    para = para.replace(",","")
    
    para = para.lower()
    
    return para

def word_count(para):
    word_list =  para.split(" ")
    num_of_word = len(word_list)
    return num_of_word

def main():

    word_dict = {}
    file_name = input("Enter file name (with .in extension): ")
    file_r = open(file_name,"r")
    file_w = open(file_name[:file_name.find('.')] + '.out',"w")
    text = file_r.read()
    para, n_para = my_paragraph(text)
    file_w.write('# of paragraph: ' + str(n_para) + '\n\n')

    for i in range(1,n_para+1,1):
        file_w.write('Paragraph: ' + str(i) + '\n')
        file_w.write('  # of sentences: ' + str(my_sentence(para[i-1])) + '\n')
        #print(para)
        one_para = word_norm(para[i-1])
        #print(one_para)
        w_para = word_count(one_para)
        file_w.write('  # of words: ' + str(w_para) + '\n\n')
        word_list =  one_para.split(" ")
        #print(word_list)
        for w in range(1,w_para,1):
            if word_list[w] not in word_dict.keys():
                word_dict[word_list[w]] = 1
            else:
                word_dict[word_list[w]] = word_dict[word_list[w]]+ 1

            
    print(word_dict)
    
    file_r.close()
    file_w.close()



main()
