#coding:utf-8

'''
    readCom(headerName):读取headerName文件中common模块中的变量
    alyCom(forPath,key)：遍历forPath中所有的文件，判断key是否是文件中的变量
'''

import os
import re

comName = []
pwdFile=''

def readCom(headerName):
    global comName
    comName = []
    fp = open(headerName,'r')
    com = []
    for line in fp:
        if(line.split()==''):continue
        if line[0] != ' ':continue
        line = line[6:]
        if line.lstrip().upper().startswith('COMMON'):
            comName.append(com)
            com =[]
            com = re.findall('[a-zA-Z]+\w*',line,re.I)[1:]
        else:
            com = com + re.findall('[a-zA-Z]+\w*',line,re.I)
    comName.append(com)
    comName = comName[1:]

def alyCom(forPath,key):
    global comName,pwdFile
    # 查找key的索引号i，j
    key = key.upper()
    ISFIND = False
    for i in range(len(comName)):
        for j in range(len(comName[i])):
            if key == comName[i][j].upper():
                ISFIND = True
                break
        if ISFIND == True:
            break
    if not ISFIND: return

    #遍历文件找出key被改变或被调用的地方
#    print('now : common /%s/ %s'%(comName[i][0],comName[i][j]))
    for p,d,f in os.walk(forPath):
        for forName in [os.path.join(p,fl) for fl in f]:
            fp = open(forName,'r')
            n_tg = 0
            ISCHANGED = False
            for line in fp:
                if line[0] != ' ':continue
                line = line.upper()
                ls = re.findall('[a-zA-Z]+\w*',line,re.I)
                if comName[i][j].upper() in ls:
                    n_tg = n_tg+1
                    if '=' in line and line.index(comName[i][j].upper()) < line.index('='):
                        ISCHANGED = True
            if n_tg >= 1:
#                if pwdFile != forName:print(forName)
                pwdFile=forName
#                print(headerName+'/'+comName[i][0]+'/'+' %s'%comName[i][j],end='')
                fw.write(forName+','+headerName+','+comName[i][0]+','+'%s'%comName[i][j])
                if(ISCHANGED):
#                    print(' changed %d times'%n_tg)
                    fw.write(','+str(n_tg)+'\n')
                else:
#                    print() #打印一个换行
                    fw.write('\n')
            fp.close()

if __name__ == "__main__":

    forPath = r'.\sourceCode'
    headerPath = '.\\coms'
    headerName = r'.\coms\CoolProperties.h'
    readCom(headerName)
#    print(comName)
    
    fw = open('rst.csv','w')
    fw.write('forName,headerName,comName,value,changed times\n')
    
#    for keys in comName:
#        for key in keys[1:]:
#            alyCom(forPath,key)
    
    for p,d,f in os.walk(headerPath):
        for headerName in [os.path.join(p,fl) for fl in f]:
            readCom(headerName)
        #    print(comName)
        #    alyCom(forPath,'nelrad')
            
            for keys in comName:
                for key in keys[1:]:
                    alyCom(forPath,key)
            
    fw.close()
