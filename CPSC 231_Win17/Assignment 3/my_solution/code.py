import difftest
import tokentest
import sys


def main():
    if sys.argv[1] == 'tdiff':
        
        f1 = sys.argv[2]
        L1 = tokentest.file2tokens(f1)
        token_only1 = []
        for T in L1:
            if T[0] not in ['COMMENT','NL','NEWLINE']:
                token_only1.append(T[0])

        f2 = sys.argv[3]
        L2 = tokentest.file2tokens(f2)
        token_only2 = []
        for T in L2:
            if T[0] not in ['COMMENT','NL','NEWLINE']:
                token_only2.append(T[0])
        
        r = difftest.similarity(token_only1,token_only2)
        if r >= 0.6:
            print(r, ' => files are similar')
        else:
            print(r, ' => files are not similar')

    if sys.argv[1] == 'adiff':

        f1 = sys.argv[2]
        L1 = tokentest.file2tokens(f1)
        token_only1 = []
        for T in L1:
            if T[0] not in ['COMMENT','NL','NEWLINE']:
                token_only1.append(T[1])

        f2 = sys.argv[3]
        L2 = tokentest.file2tokens(f2)
        token_only2 = []
        for T in L2:
            if T[0] not in ['COMMENT','NL','NEWLINE']:
                token_only2.append(T[1])
        
        r = difftest.similarity(token_only1,token_only2)
        if r >= 0.6:
            print(r, ' => files are similar')
        else:
            print(r, ' => files are not similar')

    if sys.argv[1] == 'danger':
        f = sys.argv[2]
        L = tokentest.file2tokens(f)

        D={}
        for T in L:
            if T[1] in ['eval','exec','import','open'] or (T[1][:2] == '__' and T[1][-2:] == '__'):
                if T[1] in D:
                    D[T[1]] = D[T[1]] + 1
                else:
                    D[T[1]] = 1

        for k in D:
            print(k,' x ',D[k])
        
main()
