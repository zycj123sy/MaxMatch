import os
import time
tmp = []
tmp_dict1 = []
tmp_dict2 = []
with open('E:\words.dict', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n')
        k,w,v = line.split(' ')
        tmp.append(len(w))
        tmp_dict1.append(w)
        tmp_dict2.append([k,w,v])
maxLength = max(tmp)

def fwdmm(wordDict, maxLen, str):#正向匹配
    wordList = []
    segStr = str
    segStrLen = len(segStr)
    while segStrLen > 0:
        if segStrLen > maxLen:
            wordLen = maxLen
        else:
            wordLen = segStrLen
        subStr = segStr[0:wordLen]
        while wordLen > 1:
            if subStr in wordDict:
                break
            else:
                wordLen = wordLen - 1
                subStr = subStr[0:wordLen]
        wordList.append(subStr)
        segStr = segStr[wordLen:]
        segStrLen = segStrLen - wordLen
    for wordstr in wordList:
        print(wordstr+'/',end="")
    return wordList

def bwdmm(wordDict, maxLen, str):#逆向匹配
    wordList = []
    segStr = str
    segStrLen = len(segStr)
    while segStrLen > 0:
        if segStrLen > maxLen:
            wordLen = maxLen
        else:
            wordLen = segStrLen
        subStr = segStr[-wordLen:None]
        while wordLen > 1:
            if subStr in wordDict:
                break
            else:
                wordLen = wordLen - 1
                subStr = subStr[-wordLen:None]
        wordList.append(subStr)
        segStr = segStr[0: -wordLen]
        segStrLen = segStrLen - wordLen
    wordList.reverse()
    for wordstr in wordList:
        print(wordstr+'/',end="")
    return wordList

if __name__ == '__main__':
    a = 1
    while a == 1:
        cho = int(input("请选择：（1-正向匹配 2-逆向匹配）"))
        #pas = input("请输入待分词的文本:\n")
        print("请输入待分词的文本，输入'00q'结束")
        stopword1 = '00q'
        pas = ''
        for line in iter(input, '00q'):
            pas = pas + line + '\n'
        #pas = pas.replace("\r", "").replace("\n", "")
        #print(pas)
        if cho == 1:
            time1 = time.time()
            fwdmm(tmp_dict1, maxLength, pas)
            time2 = time.time()
            print('总耗时：', end=' ')
            print(time2 - time1)
            a += 1
        elif cho == 2:
            time1 = time.time()
            bwdmm(tmp_dict1, maxLength, pas)
            time2 = time.time()
            print('总耗时：', end=' ')
            print(time2 - time1)
            a += 1
        else:
            print("请重新选择")
    os.system("pause")