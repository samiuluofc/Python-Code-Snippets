
# The function calculates number of words and sentences in a paragraph
# @param 1: p is the single paragragh
# @Return 1: ns is the number of sentences
# @Return 2: nw is the number of words
def sen_word(p):
    ns = p.count(".") + p.count("!") + p.count("?") 
    words = p.split(" ")
    nw = len(words)
    return ns,nw


def main():
    str = input("Enter the file name:")
    file = open(str,"r")
    text = file.read()

    para = text.split("\n\n")
    np = len(para)
    print("# of Paragraph:", np)

    total_w = 0
    for i in range(0,np):
        print("Paragraph ",i+1,":")
        s,w = sen_word(para[i])
        total_w = total_w + w
        print("  # of sentences: ", s)
        print("  # of wordss: ", w)


    print("Total # of words: ",total_w)
main()
        

    
