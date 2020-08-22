# -*- coding: utf-8 -*-
import urllib.request
import json
import time
import random

#刘征轩部分

dict1 = {
    'A': {
        'A': '.', 'B': '.', 'C': '.', 'D': '.', 'E': '.', 'F': '.', 'G': '.', 'H': '.', 'I': '.', 'J': '.', 'K': '.', 'L': '.', 'M': '.', 'N': '.', 'O': '.',
    },
    'B': {
        'A': '.', 'B': '.', 'C': '.', 'D': '.', 'E': '.', 'F': '.', 'G': '.', 'H': '.', 'I': '.', 'J': '.', 'K': '.', 'L': '.', 'M': '.', 'N': '.', 'O': '.',
    },
    'C': {
        'A': '.', 'B': '.', 'C': '.', 'D': '.', 'E': '.', 'F': '.', 'G': '.', 'H': '.', 'I': '.', 'J': '.', 'K': '.', 'L': '.', 'M': '.', 'N': '.', 'O': '.',
    },
    'D': {
        'A': '.', 'B': '.', 'C': '.', 'D': '.', 'E': '.', 'F': '.', 'G': '.', 'H': '.', 'I': '.', 'J': '.', 'K': '.', 'L': '.', 'M': '.', 'N': '.', 'O': '.',
    },
    'E': {
        'A': '.', 'B': '.', 'C': '.', 'D': '.', 'E': '.', 'F': '.', 'G': '.', 'H': '.', 'I': '.', 'J': '.', 'K': '.', 'L': '.', 'M': '.', 'N': '.', 'O': '.',
    },
    'F': {
        'A': '.', 'B': '.', 'C': '.', 'D': '.', 'E': '.', 'F': '.', 'G': '.', 'H': '.', 'I': '.', 'J': '.', 'K': '.', 'L': '.', 'M': '.', 'N': '.', 'O': '.',
    },
    'G': {
        'A': '.', 'B': '.', 'C': '.', 'D': '.', 'E': '.', 'F': '.', 'G': '.', 'H': '.', 'I': '.', 'J': '.', 'K': '.', 'L': '.', 'M': '.', 'N': '.', 'O': '.',
    },
    'H': {
        'A': '.', 'B': '.', 'C': '.', 'D': '.', 'E': '.', 'F': '.', 'G': '.', 'H': '.', 'I': '.', 'J': '.', 'K': '.', 'L': '.', 'M': '.', 'N': '.', 'O': '.',
    },
    'I': {
        'A': '.', 'B': '.', 'C': '.', 'D': '.', 'E': '.', 'F': '.', 'G': '.', 'H': '.', 'I': '.', 'J': '.', 'K': '.', 'L': '.', 'M': '.', 'N': '.', 'O': '.',
    },
    'J': {
        'A': '.', 'B': '.', 'C': '.', 'D': '.', 'E': '.', 'F': '.', 'G': '.', 'H': '.', 'I': '.', 'J': '.', 'K': '.', 'L': '.', 'M': '.', 'N': '.', 'O': '.',
    },
    'K': {
        'A': '.', 'B': '.', 'C': '.', 'D': '.', 'E': '.', 'F': '.', 'G': '.', 'H': '.', 'I': '.', 'J': '.', 'K': '.', 'L': '.', 'M': '.', 'N': '.', 'O': '.',
    },
    'L': {
        'A': '.', 'B': '.', 'C': '.', 'D': '.', 'E': '.', 'F': '.', 'G': '.', 'H': '.', 'I': '.', 'J': '.', 'K': '.', 'L': '.', 'M': '.', 'N': '.', 'O': '.',
    },
    'M': {
        'A': '.', 'B': '.', 'C': '.', 'D': '.', 'E': '.', 'F': '.', 'G': '.', 'H': '.', 'I': '.', 'J': '.', 'K': '.', 'L': '.', 'M': '.', 'N': '.', 'O': '.',
    },
    'N': {
        'A': '.', 'B': '.', 'C': '.', 'D': '.', 'E': '.', 'F': '.', 'G': '.', 'H': '.', 'I': '.', 'J': '.', 'K': '.', 'L': '.', 'M': '.', 'N': '.', 'O': '.',
    },
    'O': {
        'A': '.', 'B': '.', 'C': '.', 'D': '.', 'E': '.', 'F': '.', 'G': '.', 'H': '.', 'I': '.', 'J': '.', 'K': '.', 'L': '.', 'M': '.', 'N': '.', 'O': '.',
    }
}

dictscore1 = {
    'A': {
        'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
    },
    'B': {
        'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
    },
    'C': {
        'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
    },
    'D': {
        'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
    },
    'E': {
        'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
    },
    'F': {
        'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
    },
    'G': {
        'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
    },
    'H': {
        'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
    },
    'I': {
        'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
    },
    'J': {
        'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
    },
    'K': {
        'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
    },
    'L': {
        'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
    },
    'M': {
        'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
    },
    'N': {
        'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
    },
    'O': {
        'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
    }
}

def change_M0rO(record,dict1):
    record = record.upper()
    #判断当前是黑棋还是白棋
    if (len(record)//2)%2==0:
        #print('我要下黑棋，检索黑棋相关棋型')
        borw = 1
    else:
        #print('我要下白棋，检索白棋相关棋型')
        borw = 0 
    #---黑棋还是白棋的标志   1代表我先手  0代表对方先手---
    #---坐标表示转换为图形表示---
    for index in range(0, len(record), 2):
        if borw == 1:
            dict1[record[index]][record[index+1]] = 'M'
            borw = 0
        else:
            dict1[record[index]][record[index+1]] = 'O'
            borw = 1
    return

def judegemodel(li,dic,i,j):
    # if "CMMMM" in li or "MCMMM" in li or "MMCMM" in li or "MMMCM" in li or "MMMMC" in li:
    #     for var in ("CMMMM","MCMMM","MMCMM","MMMCM","MMMMC"):
    #         if var in li:
    #             dic[i][j]+=100000
    # elif   "OOOOC" in li or "COOOO" in li or "OOOCO" in li or "OCOOO" in li or "OOCOO" in li:
    #     for var in ("OOOOC","COOOO","OOOCO", "OCOOO","OOCOO"):
    #         if var in li:
    #             dic[i][j]+=80000
    # elif   "MOOOOC" in li or "COOOOM" in li:
    #     for var in ("MOOOOC","COOOOM"):
    #         if var in li:
    #             dic[i][j]+=80000
    # elif   ".CMMM." in li or ".MCMM." in li or ".MMCM." in li or ".MMMC." in li:
    #     for var in (".CMMM.",".MCMM.",".MMCM.",".MMMC."):
    #         if var in li:
    #             dic[i][j]+=33000
    # elif   "M.MCM.M" in li or "M.CMM.M" in li or "M.MMC.M" in li:
    #     for var in ("M.MCM.M","M.CMM.M","M.MMC.M"):
    #         if var in li: 
    #             dic[i][j]+=33000
    # elif   "COOO." in li or ".OOOC" in li or ".OOCO." in li or ".OCOO." in li:
    #     for var in ("COOO.",".OOOC",".OOCO.",".OCOO."):
    #         if var in li:
    #             dic[i][j]+=15000
    # elif   "OCMMM." in li or "OMCMM." in li or "OMMCM." in li or "OMMMC." in li or ".CMMMO" in li or ".MCMMO" in li or ".MMCMO" in li or ".MMMCO" in li:
    #     for var in ("OCMMM.","OMCMM.","OMMCM.","OMMMC.",".CMMMO",".MCMMO",".MMCMO",".MMMCO"):
    #         if var in li: 
    #             dic[i][j]+=20000
    # elif   ".MMC." in li or ".MCM." in li or ".CMM." in li:
    #     for var in (".MMC.",".MCM.",".CMM."):
    #         if var in li:
    #             dic[i][j]+=6000
    # elif   ".MM.C." in li or ".MC.M." in li or ".M.CM." in li or ".CM.M." in li or ".C.MM." in li or ".M.MC." in li:
    #     for var in (".MM.C.",".MC.M.",".M.CM.",".CM.M.",".C.MM.",".M.MC."):
    #         if var in li: 
    #             dic[i][j]+=1200
    # elif    "MOOOC" in li or "COOOM" in li:
    #     for var in ("MOOOC","COOOM"):
    #         if var in li:
    #             dic[i][j]+=5000
    # elif   ".OOC" in li or "COO." in li:
    #     for var in (".OOC","COO."):
    #         if var in li:
    #             dic[i][j]+=1000
    # elif   ".MMCO" in li or ".MCMO" in li or ".CMMO" in li or "OMMC." in li or "OMCM." in li or "OCMM." in li or "MOOC" in li or "COOM" in li:
    #     for var in (".MMCO",".MCMO",".CMMO","OMMC.","OMCM.","OCMM.","MOOC","COOM"):
    #         if var in li:
    #             dic[i][j]+=340
    # elif   ".M.C." in li or ".C.M." in li :
    #     for var in (".M.C.",".C.M."):
    #         if var in li:
    #             dic[i][j]+=180
    # elif   ".MC." in li or ".CM." in li :
    #     for var in (".MC.",".CM."):
    #         if var in li:
    #             dic[i][j]+=160
    # elif    ".OC." in li or ".CO." in li:
    #     for var in (".OC.",".CO."):
    #         if var in li:
    #             dic[i][j]+=100
    # elif    "OMMM.C" in li or "C.MMMO" in li:
    #     for var in ("OMMM.C","C.MMMO"):
    #         if var in li:
    #             dic[i][j]+=60
    # else:
    #     dic[i][j]+=20
    if "CMMMM" in li or "MCMMM" in li or "MMCMM" in li or "MMMCM" in li or "MMMMC" in li:
        for var in ("CMMMM","MCMMM","MMCMM","MMMCM","MMMMC"):
            if var in li:
                dic[i][j]+=10000
    elif   "OOOOC" in li or "COOOO" in li or "OOOCO" in li or "OCOOO" in li or "OOCOO" in li:
        for var in ("OOOOC","COOOO","OOOCO", "OCOOO","OOCOO"):
            if var in li:
                dic[i][j]+=6000
    elif   ".CMMM." in li or ".MCMM." in li or ".MMCM." in li or ".MMMC." in li:
        for var in (".CMMM.",".MCMM.",".MMCM.",".MMMC."):
            if var in li:
                dic[i][j]+=5000
    elif   "COOO." in li or ".OOOC" in li or ".OOCO." in li or ".OCOO." in li:
        for var in ("COOO.",".OOOC",".OOCO.",".OCOO."):
            if var in li:
                dic[i][j]+=3500
    elif   "OCMMM." in li or "OMCMM." in li or "OMMCM." in li or "OMMMC." in li or ".CMMMO" in li or ".MCMMO" in li or ".MMCMO" in li or ".MMMCO" in li:
        for var in ("OCMMM.","OMCMM.","OMMCM.","OMMMC.",".CMMMO",".MCMMO",".MMCMO",".MMMCO"):
            if var in li: 
                dic[i][j]+=2000
    elif   ".MMC." in li or ".MCM." in li or ".CMM." in li:
        for var in (".MMC.",".MCM.",".CMM."):
            if var in li:
                dic[i][j]+=1700
    elif   ".MM.C." in li or ".MC.M." in li or ".M.CM." in li or ".CM.M." in li or ".C.MM." in li or ".M.MC." in li:
        for var in (".MM.C.",".MC.M.",".M.CM.",".CM.M.",".C.MM.",".M.MC."):
            if var in li: 
                dic[i][j]+=400
    elif    "MOOOC" in li or "COOOM" in li:
        for var in ("MOOOC","COOOM"):
            if var in li:
                dic[i][j]+=300
    elif   ".OOC" in li or "COO." in li:
        for var in (".OOC","COO."):
            if var in li:
                dic[i][j]+=150
    elif   ".MMCO" in li or ".MCMO" in li or ".CMMO" in li or "OMMC." in li or "OMCM." in li or "OCMM." in li or "MOOC" in li or "COOM" in li:
        for var in (".MMCO",".MCMO",".CMMO","OMMC.","OMCM.","OCMM.","MOOC","COOM"):
            if var in li:
                dic[i][j]+=170
    elif   ".M.C." in li or ".C.M." in li :
        for var in (".M.C.",".C.M."):
            if var in li:
                dic[i][j]+=90
    elif   ".MC." in li or ".CM." in li :
        for var in (".MC.",".CM."):
            if var in li:
                dic[i][j]+=80
    elif    ".OC." in li or ".CO." in li:
        for var in (".OC.",".CO."):
            if var in li:
                dic[i][j]+=50
    else:
        dic[i][j]+=20

def judegemodelo(li,dic,i,j):
    if "CMMMM" in li or "MCMMM" in li or "MMCMM" in li or "MMMCM" in li or "MMMMC" in li:
        for var in ("CMMMM","MCMMM","MMCMM","MMMCM","MMMMC"):
            if var in li:
                dic[i][j]+=10000
    elif   "OOOOC" in li or "COOOO" in li or "OOOCO" in li or "OCOOO" in li or "OOCOO" in li:
        for var in ("OOOOC","COOOO","OOOCO", "OCOOO","OOCOO"):
            if var in li:
                dic[i][j]+=6000
    elif   ".CMMM." in li or ".MCMM." in li or ".MMCM." in li or ".MMMC." in li:
        for var in (".CMMM.",".MCMM.",".MMCM.",".MMMC."):
            if var in li:
                dic[i][j]+=5000
    elif   "COOO." in li or ".OOOC" in li or ".OOCO." in li or ".OCOO." in li:
        for var in ("COOO.",".OOOC",".OOCO.",".OCOO."):
            if var in li:
                dic[i][j]+=3500
    elif   "OCMMM." in li or "OMCMM." in li or "OMMCM." in li or "OMMMC." in li or ".CMMMO" in li or ".MCMMO" in li or ".MMCMO" in li or ".MMMCO" in li:
        for var in ("OCMMM.","OMCMM.","OMMCM.","OMMMC.",".CMMMO",".MCMMO",".MMCMO",".MMMCO"):
            if var in li: 
                dic[i][j]+=2000
    elif   ".MMC." in li or ".MCM." in li or ".CMM." in li:
        for var in (".MMC.",".MCM.",".CMM."):
            if var in li:
                dic[i][j]+=1700
    elif   ".MM.C." in li or ".MC.M." in li or ".M.CM." in li or ".CM.M." in li or ".C.MM." in li or ".M.MC." in li:
        for var in (".MM.C.",".MC.M.",".M.CM.",".CM.M.",".C.MM.",".M.MC."):
            if var in li: 
                dic[i][j]+=400
    elif    "MOOOC" in li or "COOOM" in li:
        for var in ("MOOOC","COOOM"):
            if var in li:
                dic[i][j]+=300
    elif   ".OOC" in li or "COO." in li:
        for var in (".OOC","COO."):
            if var in li:
                dic[i][j]+=150
    elif   ".MMCO" in li or ".MCMO" in li or ".CMMO" in li or "OMMC." in li or "OMCM." in li or "OCMM." in li or "MOOC" in li or "COOM" in li:
        for var in (".MMCO",".MCMO",".CMMO","OMMC.","OMCM.","OCMM.","MOOC","COOM"):
            if var in li:
                dic[i][j]+=170
    elif   ".M.C." in li or ".C.M." in li :
        for var in (".M.C.",".C.M."):
            if var in li:
                dic[i][j]+=90
    elif   ".MC." in li or ".CM." in li :
        for var in (".MC.",".CM."):
            if var in li:
                dic[i][j]+=80
    elif    ".OC." in li or ".CO." in li:
        for var in (".OC.",".CO."):
            if var in li:
                dic[i][j]+=50
    else:
        dic[i][j]+=20
    # if "CMMMM" in li or "MCMMM" in li or "MMCMM" in li or "MMMCM" in li or "MMMMC" in li:
    #     for var in ("CMMMM","MCMMM","MMCMM","MMMCM","MMMMC"):
    #         if var in li:
    #             dic[i][j]+=100000
    # elif   "OOOOC" in li or "COOOO" in li or "OOOCO" in li or "OCOOO" in li or "OOCOO" in li:
    #     for var in ("OOOOC","COOOO","OOOCO", "OCOOO","OOCOO"):
    #         if var in li:
    #             dic[i][j]+=80000
    # elif   "MOOOOC" in li or "COOOOM" in li:
    #     for var in ("MOOOOC","COOOOM"):
    #         if var in li:
    #             dic[i][j]+=80000
    # elif   ".CMMM." in li or ".MCMM." in li or ".MMCM." in li or ".MMMC." in li:
    #     for var in (".CMMM.",".MCMM.",".MMCM.",".MMMC."):
    #         if var in li:
    #             dic[i][j]+=33000
    # elif   "M.MCM.M" in li or "M.CMM.M" in li or "M.MMC.M" in li:
    #     for var in ("M.MCM.M","M.CMM.M","M.MMC.M"):
    #         if var in li: 
    #             dic[i][j]+=33000
    # elif   "COOO." in li or ".OOOC" in li or ".OOCO." in li or ".OCOO." in li:
    #     for var in ("COOO.",".OOOC",".OOCO.",".OCOO."):
    #         if var in li:
    #             dic[i][j]+=15000
    # elif   "OCMMM." in li or "OMCMM." in li or "OMMCM." in li or "OMMMC." in li or ".CMMMO" in li or ".MCMMO" in li or ".MMCMO" in li or ".MMMCO" in li:
    #     for var in ("OCMMM.","OMCMM.","OMMCM.","OMMMC.",".CMMMO",".MCMMO",".MMCMO",".MMMCO"):
    #         if var in li: 
    #             dic[i][j]+=20000
    # elif   ".MMC." in li or ".MCM." in li or ".CMM." in li:
    #     for var in (".MMC.",".MCM.",".CMM."):
    #         if var in li:
    #             dic[i][j]+=6000
    # elif   ".MM.C." in li or ".MC.M." in li or ".M.CM." in li or ".CM.M." in li or ".C.MM." in li or ".M.MC." in li:
    #     for var in (".MM.C.",".MC.M.",".M.CM.",".CM.M.",".C.MM.",".M.MC."):
    #         if var in li: 
    #             dic[i][j]+=1200
    # elif    "MOOOC" in li or "COOOM" in li:
    #     for var in ("MOOOC","COOOM"):
    #         if var in li:
    #             dic[i][j]+=5000
    # elif   ".OOC" in li or "COO." in li:
    #     for var in (".OOC","COO."):
    #         if var in li:
    #             dic[i][j]+=1000
    # elif   ".MMCO" in li or ".MCMO" in li or ".CMMO" in li or "OMMC." in li or "OMCM." in li or "OCMM." in li or "MOOC" in li or "COOM" in li:
    #     for var in (".MMCO",".MCMO",".CMMO","OMMC.","OMCM.","OCMM.","MOOC","COOM"):
    #         if var in li:
    #             dic[i][j]+=340
    # elif   ".M.C." in li or ".C.M." in li :
    #     for var in (".M.C.",".C.M."):
    #         if var in li:
    #             dic[i][j]+=180
    # elif   ".MC." in li or ".CM." in li :
    #     for var in (".MC.",".CM."):
    #         if var in li:
    #             dic[i][j]+=160
    # elif    ".OC." in li or ".CO." in li:
    #     for var in (".OC.",".CO."):
    #         if var in li:
    #             dic[i][j]+=100
    # elif    "OMMM.C" in li or "C.MMMO" in li:
    #     for var in ("OMMM.C","C.MMMO"):
    #         if var in li:
    #             dic[i][j]+=60
    # else:
    #     dic[i][j]+=20
    # if "CMMMM" in li or "MCMMM" in li or "MMCMM" in li or "MMMCM" in li or "MMMMC" in li:
    #         dic[i][j]+=10000
    # elif   "OOOOC" in li or "COOOO" in li:
    #         dic[i][j]+=6000
    # elif   ".CMMM." in li or ".MCMM." in li or ".MMCM." in li or ".MMMC." in li:
    #         dic[i][j]+=5000
    # elif   "COOO." in li or ".OOOC" in li or ".OOCO." in li or ".OCOO." in li:
    #         dic[i][j]+=2500
    # elif   "OCMMM." in li or "OMCMM." in li or "OMMCM." in li or "OMMMC." in li or ".CMMMO" in li or ".MCMMO" in li or ".MMCMO" in li or ".MMMCO" in li:
    #         dic[i][j]+=2000
    # elif   ".MMC." in li or ".MCM." in li or ".CMM." in li:
    #         dic[i][j]+=400
    # elif   ".OOC" in li or "COO." in li or "MOOOC" in li or "COOOM" in li:
    #         dic[i][j]+=400
    # elif   ".MMCO" in li or ".MCMO" in li or ".CMMO" in li or "OMMC." in li or "OMCM." in li or "OCMM." in li or "MOOC" in li or "COOM" in li:
    #         dic[i][j]+=200
    # elif   ".MC." in li or ".CM." in li:
    #         dic[i][j]+=50
    # else:
    #     dic[i][j]+=20

def findmax(dic):
    max=0
    for i in 'ABCDEFGHIJKLMNO':
        for j in 'ABCDEFGHIJKLMNO':
            if dic[i][j]>max:
                max=dic[i][j]
    for i in 'ABCDEFGHIJKLMNO':
        for j in 'ABCDEFGHIJKLMNO':
            if dic[i][j]==max:
                return(i,j)
    
def countscore(dict,dictscore):
    #找到所有还空着的位置;对每一个空位子;将这个位置设为C
    for i in 'ABCDEFGHIJKLMNO':
        for j in 'ABCDEFGHIJKLMNO':
            if dict[i][j]==".":
               dict[i][j]="C"
            if dict[i][j]=="C":
                #print('YES')
                list1=[]
                list2=[]
                list3=[]
                list4=[]
                x1=i
                x2=j
                x3 = x1
                x4 = chr(ord(x2)-4)
                # 找到端点
                for index in range(0, 9, 1):
                    if chr(ord(x4)+index) <'P' and '@'< chr(ord(x4)+index) and x3 <'P' and '@'< x3:
                        list1.append(dict[x3][chr(ord(x4)+index)])
                        #print(dict[x3][chr(ord(x4)+index)], end="")
                    else:
                        print('', end='')
                        #print(',', end="")
                x3 = chr(ord(x1)-4)
                x4 = chr(ord(x2)-4)
                # 找到端点
                for index in range(0, 9, 1):
                    if chr(ord(x3)+index) <'P' and '@'< chr(ord(x3)+index) and chr(ord(x4)+index) <'P' and '@'< chr(ord(x4)+index):
                        list2.append(dict[chr(ord(x3)+index)][chr(ord(x4)+index)])
                        #print(dict[chr(ord(x3)+index)][chr(ord(x4)+index)], end="")
                    else:
                        print('', end='')
                        #print(',', end="")


                x3 = chr(ord(x1)-4)
                x4 = x2
                # 找到端点
                for index in range(0, 9, 1):
                    if chr(ord(x3)+index) <'P' and '@'< chr(ord(x3)+index) and x4 <'P' and '@'< x4:
                        list3.append(dict[chr(ord(x3)+index)][x4])
                        #print(dict[chr(ord(x3)+index)][x4], end="")
                    else:
                        print('', end='')
                        #print(',', end="")
                            
                x3 = chr(ord(x1)-4)
                x4 = chr(ord(x2)+4)
                # 找到端点
                for index in range(0, 9, 1):
                    if chr(ord(x3)+index) <'P' and '@'< chr(ord(x3)+index) and chr(ord(x4)-index) <'P' and '@'< chr(ord(x4)-index):
                        list4.append(dict[chr(ord(x3)+index)][chr(ord(x4)-index)])
                        #print(dict[chr(ord(x3)+index)][chr(ord(x4)-index)], end="")
                    else:
                        print('', end='')
                        #print(',', end="")


                li1=''.join(list1)
                li2=''.join(list2)
                li3=''.join(list3)
                li4=''.join(list4)
                #判断已有棋型中是否有得分棋型并对dictscore进行相应赋值
                judegemodel(li1,dictscore,i,j)
                judegemodel(li2,dictscore,i,j)
                judegemodel(li3,dictscore,i,j)
                judegemodel(li4,dictscore,i,j)
                list1=[]
                list2=[]
                list3=[]
                list4=[]
                dict[i][j]="." 
    return

def countscoreo(dict,dictscore):
    #找到所有还空着的位置;对每一个空位子;将这个位置设为C
    for i in 'ABCDEFGHIJKLMNO':
        for j in 'ABCDEFGHIJKLMNO':
            if dict[i][j]==".":
               dict[i][j]="C"
            if dict[i][j]=="C":
                #print('YES')
                list1=[]
                list2=[]
                list3=[]
                list4=[]
                x1=i
                x2=j
                x3 = x1
                x4 = chr(ord(x2)-4)
                # 找到端点
                for index in range(0, 9, 1):
                    if chr(ord(x4)+index) <'P' and '@'< chr(ord(x4)+index) and x3 <'P' and '@'< x3:
                        list1.append(dict[x3][chr(ord(x4)+index)])
                        #print(dict[x3][chr(ord(x4)+index)], end="")
                    else:
                        print('', end='')
                        #print(',', end="")
                x3 = chr(ord(x1)-4)
                x4 = chr(ord(x2)-4)
                # 找到端点
                for index in range(0, 9, 1):
                    if chr(ord(x3)+index) <'P' and '@'< chr(ord(x3)+index) and chr(ord(x4)+index) <'P' and '@'< chr(ord(x4)+index):
                        list2.append(dict[chr(ord(x3)+index)][chr(ord(x4)+index)])
                        #print(dict[chr(ord(x3)+index)][chr(ord(x4)+index)], end="")
                    else:
                        print('', end='')
                        #print(',', end="")


                x3 = chr(ord(x1)-4)
                x4 = x2
                # 找到端点
                for index in range(0, 9, 1):
                    if chr(ord(x3)+index) <'P' and '@'< chr(ord(x3)+index) and x4 <'P' and '@'< x4:
                        list3.append(dict[chr(ord(x3)+index)][x4])
                        #print(dict[chr(ord(x3)+index)][x4], end="")
                    else:
                        print('', end='')
                        #print(',', end="")
                            
                x3 = chr(ord(x1)-4)
                x4 = chr(ord(x2)+4)
                # 找到端点
                for index in range(0, 9, 1):
                    if chr(ord(x3)+index) <'P' and '@'< chr(ord(x3)+index) and chr(ord(x4)-index) <'P' and '@'< chr(ord(x4)-index):
                        list4.append(dict[chr(ord(x3)+index)][chr(ord(x4)-index)])
                        #print(dict[chr(ord(x3)+index)][chr(ord(x4)-index)], end="")
                    else:
                        print('', end='')
                        #print(',', end="")


                li1=''.join(list1)
                li2=''.join(list2)
                li3=''.join(list3)
                li4=''.join(list4)
                #判断已有棋型中是否有得分棋型并对dictscore进行相应赋值
                judegemodelo(li1,dictscore,i,j)
                judegemodelo(li2,dictscore,i,j)
                judegemodelo(li3,dictscore,i,j)
                judegemodelo(li4,dictscore,i,j)
                list1=[]
                list2=[]
                list3=[]
                list4=[]
                dict[i][j]="." 
    return

def quick_algorithm(a,b,c):
    a=a%c
    ans=1
    while b!=0:
        if b&1:
            ans=(ans*a)%c
        b>>=1
        a=(a*a)%c
    return ans

def encryption(sequence):
    sequence = 'hello, world!'
    index=len(sequence)-1
    out=0
    for i, j in enumerate(sequence):
        out+=ord(j)*(256**(index-i)) 
    #先将256进制密码转换为10进制数out
    #print(out)
    out=hex(quick_algorithm(out,65537,135261828916791946705313569652794581721330948863485438876915508683244111694485850733278569559191167660149469895899348939039437830613284874764820878002628686548956779897196112828969255650312573935871059275664474562666268163936821302832645284397530568872432109324825205567091066297960733513602409443790146687029))
    #将out加密后转换为16进制数
    return out

def play_chess(litest,dict,dictscore):
    li=litest
    if len(li)/2%2==0:
        change_M0rO(li,dict1)
        countscore(dict, dictscore)
        listeee=''.join(findmax(dictscore))
        #print(listeee.lower(),end='')
        # print("黑棋方法一")
        return(listeee.lower())
    else:
        if len(li)<10:
            change_M0rO(li,dict1)
            countscore(dict, dictscore)
            listeee=''.join(findmax(dictscore))
            # print("白棋方法一")
            return(listeee.lower())
        else:
            # print("白棋方法二")
            return(findmax3(dictscore,li))

def clear(dict,dictscore):
         # ---重置棋盘--
    for i in 'ABCDEFGHIJKLMNO':
        for j in 'ABCDEFGHIJKLMNO':
            dict[i][j]='.'

    # ---重置棋盘得分---
    for i in 'ABCDEFGHIJKLMNO':
        for j in 'ABCDEFGHIJKLMNO':
            dictscore[i][j]=0
    return

def findmax3(dic,litest):
    dict=dic
    board=litest

    #找到并且记录己方的最大得分位置三个
    Max=0
    for i in 'ABCDEFGHIJKLMNO':
        for j in 'ABCDEFGHIJKLMNO':
            if dict[i][j]>Max:
                Max=dict[i][j]
    max1=Max
    for i in 'ABCDEFGHIJKLMNO':
        for j in 'ABCDEFGHIJKLMNO':
            if dict[i][j]==Max:
                loc1=(i,j)
                loc1=''.join(loc1)
                loc1=loc1.lower()
                dict[i][j]=0
    Max=0
    for i in 'ABCDEFGHIJKLMNO':
        for j in 'ABCDEFGHIJKLMNO':
            if dict[i][j]>Max:
                Max=dict[i][j]
    max2=Max
    for i in 'ABCDEFGHIJKLMNO':
        for j in 'ABCDEFGHIJKLMNO':
            if dict[i][j]==Max:
                loc2=(i,j)
                loc2=''.join(loc2)
                loc2=loc2.lower()
                dict[i][j]=0
    Max=0
    for i in 'ABCDEFGHIJKLMNO':
        for j in 'ABCDEFGHIJKLMNO':
            if dict[i][j]>Max:
                Max=dict[i][j]
    max3=Max
    for i in 'ABCDEFGHIJKLMNO':
        for j in 'ABCDEFGHIJKLMNO':
            if dict[i][j]==Max:
                loc3=(i,j)
                loc3=''.join(loc3)
                loc3=loc3.lower()
                dict[i][j]=0
  
    #loc1,loc2,loc3为三个位置，max1,max2,max3为三个分数
    bloc1=board+loc1 
    bloc2=board+loc2
    bloc3=board+loc3

    #输出己方位置和分数
    # print(max1,max2,max3)
    # print(bloc1,bloc2,bloc3)

    dict = {
        'A': {
            'A': '.', 'B': '.', 'C': '.', 'D': '.', 'E': '.', 'F': '.', 'G': '.', 'H': '.', 'I': '.', 'J': '.', 'K': '.', 'L': '.', 'M': '.', 'N': '.', 'O': '.',
        },
        'B': {
            'A': '.', 'B': '.', 'C': '.', 'D': '.', 'E': '.', 'F': '.', 'G': '.', 'H': '.', 'I': '.', 'J': '.', 'K': '.', 'L': '.', 'M': '.', 'N': '.', 'O': '.',
        },
        'C': {
            'A': '.', 'B': '.', 'C': '.', 'D': '.', 'E': '.', 'F': '.', 'G': '.', 'H': '.', 'I': '.', 'J': '.', 'K': '.', 'L': '.', 'M': '.', 'N': '.', 'O': '.',
        },
        'D': {
            'A': '.', 'B': '.', 'C': '.', 'D': '.', 'E': '.', 'F': '.', 'G': '.', 'H': '.', 'I': '.', 'J': '.', 'K': '.', 'L': '.', 'M': '.', 'N': '.', 'O': '.',
        },
        'E': {
            'A': '.', 'B': '.', 'C': '.', 'D': '.', 'E': '.', 'F': '.', 'G': '.', 'H': '.', 'I': '.', 'J': '.', 'K': '.', 'L': '.', 'M': '.', 'N': '.', 'O': '.',
        },
        'F': {
            'A': '.', 'B': '.', 'C': '.', 'D': '.', 'E': '.', 'F': '.', 'G': '.', 'H': '.', 'I': '.', 'J': '.', 'K': '.', 'L': '.', 'M': '.', 'N': '.', 'O': '.',
        },
        'G': {
            'A': '.', 'B': '.', 'C': '.', 'D': '.', 'E': '.', 'F': '.', 'G': '.', 'H': '.', 'I': '.', 'J': '.', 'K': '.', 'L': '.', 'M': '.', 'N': '.', 'O': '.',
        },
        'H': {
            'A': '.', 'B': '.', 'C': '.', 'D': '.', 'E': '.', 'F': '.', 'G': '.', 'H': '.', 'I': '.', 'J': '.', 'K': '.', 'L': '.', 'M': '.', 'N': '.', 'O': '.',
        },
        'I': {
            'A': '.', 'B': '.', 'C': '.', 'D': '.', 'E': '.', 'F': '.', 'G': '.', 'H': '.', 'I': '.', 'J': '.', 'K': '.', 'L': '.', 'M': '.', 'N': '.', 'O': '.',
        },
        'J': {
            'A': '.', 'B': '.', 'C': '.', 'D': '.', 'E': '.', 'F': '.', 'G': '.', 'H': '.', 'I': '.', 'J': '.', 'K': '.', 'L': '.', 'M': '.', 'N': '.', 'O': '.',
        },
        'K': {
            'A': '.', 'B': '.', 'C': '.', 'D': '.', 'E': '.', 'F': '.', 'G': '.', 'H': '.', 'I': '.', 'J': '.', 'K': '.', 'L': '.', 'M': '.', 'N': '.', 'O': '.',
        },
        'L': {
            'A': '.', 'B': '.', 'C': '.', 'D': '.', 'E': '.', 'F': '.', 'G': '.', 'H': '.', 'I': '.', 'J': '.', 'K': '.', 'L': '.', 'M': '.', 'N': '.', 'O': '.',
        },
        'M': {
            'A': '.', 'B': '.', 'C': '.', 'D': '.', 'E': '.', 'F': '.', 'G': '.', 'H': '.', 'I': '.', 'J': '.', 'K': '.', 'L': '.', 'M': '.', 'N': '.', 'O': '.',
        },
        'N': {
            'A': '.', 'B': '.', 'C': '.', 'D': '.', 'E': '.', 'F': '.', 'G': '.', 'H': '.', 'I': '.', 'J': '.', 'K': '.', 'L': '.', 'M': '.', 'N': '.', 'O': '.',
        },
        'O': {
            'A': '.', 'B': '.', 'C': '.', 'D': '.', 'E': '.', 'F': '.', 'G': '.', 'H': '.', 'I': '.', 'J': '.', 'K': '.', 'L': '.', 'M': '.', 'N': '.', 'O': '.',
        }
        }
    
    dictscore = {
        'A': {
            'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
        },
        'B': {
            'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
        },
        'C': {
            'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
        },
        'D': {
            'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
        },
        'E': {
            'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
        },
        'F': {
            'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
        },
        'G': {
            'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
        },
        'H': {
            'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
        },
        'I': {
            'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
        },
        'J': {
            'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
        },
        'K': {
            'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
        },
        'L': {
            'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
        },
        'M': {
            'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
        },
        'N': {
            'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
        },
        'O': {
            'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
        }
        } 
    
    change_M0rO(bloc1,dict)
    countscoreo(dict, dictscore)

    # for i in 'ABCDEFGHIJKLMNO':
    #     for j in 'ABCDEFGHIJKLMNO':
    #         print(dict[i][j],end=' ')
    #     print()
    # for i in 'ABCDEFGHIJKLMNO':
    #     for j in 'ABCDEFGHIJKLMNO':
    #         print(dictscore[i][j],end=' ')
    #     print()


    #计算第一种下法地方落子得分maxo1以及位置loco1
    maxo=0
    for i in 'ABCDEFGHIJKLMNO':
        for j in 'ABCDEFGHIJKLMNO':
            if dictscore[i][j]>maxo:
                maxo=dictscore[i][j]
    for i in 'ABCDEFGHIJKLMNO':
        for j in 'ABCDEFGHIJKLMNO':
            if dictscore[i][j]==maxo:
                loco1=(i,j)
                loco1=''.join(loco1)
                loco1=loco1.lower()
    maxo1=maxo
    # print(maxo1,loco1)
    clear(dict,dictscore)


    #计算第二种下法地方落子得分maxo2以及位置loco2
    change_M0rO(bloc2,dict)
    countscoreo(dict, dictscore)
    maxo=0
    for i in 'ABCDEFGHIJKLMNO':
        for j in 'ABCDEFGHIJKLMNO':
            if dictscore[i][j]>maxo:
                maxo=dictscore[i][j]
    for i in 'ABCDEFGHIJKLMNO':
        for j in 'ABCDEFGHIJKLMNO':
            if dictscore[i][j]==maxo:
                loco2=(i,j)
                loco2=''.join(loco2)
                loco2=loco2.lower()
    maxo2=maxo
    # print(maxo2,loco2)
    clear(dict,dictscore)


    #计算第二种下法地方落子得分maxo2以及位置loco2
    change_M0rO(bloc3,dict)
    countscoreo(dict, dictscore)
    maxo=0
    for i in 'ABCDEFGHIJKLMNO':
        for j in 'ABCDEFGHIJKLMNO':
            if dictscore[i][j]>maxo:
                maxo=dictscore[i][j]
    for i in 'ABCDEFGHIJKLMNO':
        for j in 'ABCDEFGHIJKLMNO':
            if dictscore[i][j]==maxo:
                loco3=(i,j)
                loco3=''.join(loco3)
                loco3=loco3.lower()
    maxo3=maxo
    # print(maxo3,loco3)
    clear(dict,dictscore)
    
    if max(max1,max2,max3)>5000:
        if max1==max(max1,max2,max3):
            return loc1
        if max2==max(max1,max2,max3):
            return loc2
        if max3==max(max1,max2,max3):
            return loc3
    else:
        if maxo1==min(maxo1,maxo2,maxo3):
            return loco1
        if maxo2==min(maxo1,maxo2,maxo3):
            return loco2
        if maxo3==min(maxo1,maxo2,maxo3):
            return loco3





#董至彪部分

def ConvertTo256(str_str):
    ret = 0
    base = 1
    str_len = len(str_str)
    for i in range(str_len - 1, -1, -1):
        ret += base * ord(str_str[i])
        base *= 256
    return ret

def tConvertTos(int_dec):
    ret = ""
    while int_dec > 0:
        x = int_dec % 16
        int_dec //= 16
        if x > 9:
            ret = chr(x + 55) + ret
        else:
            ret = chr(x + 48) + ret
    return ret

def getMark(board):
    def chescore(subctype):
        if subctype.find("CMMMM")>-1:  
            score=10000
        elif subctype.find("MCMMM")>-1:  
            score=10000
        elif subctype.find("MMCMM")>-1:  
            score=10000
        elif subctype.find("MMMCM")>-1:  
            score=10000
        elif subctype.find("MMMMC")>-1:  
            score=10000
        else:
            if subctype.find("OOOOC")>-1:
                score=6000
            elif  subctype.find("COOOO")>-1:
                score=6000
            elif subctype.find("OCOOO")>-1:
                score=6000
            elif subctype.find("OOCOO")>-1:
                score=6000
            elif subctype.find("OOOCO")>-1:
                score=6000
            else:
                if subctype.find(".CMMM.")>-1:
                    score=5000
                elif subctype.find(".MCMM.")>-1:
                    score=5000
                elif subctype.find(".MMCM.")>-1:
                    score=5000
                elif subctype.find(".MMMC.")>-1:
                    score=5000
                else:
                    if subctype.find("COOO.")>-1:
                        score=2500
                    elif subctype.find(".OOOC")>-1:
                        score=2500
                    elif subctype.find(".OOCO.")>-1:
                        score=2500
                    elif subctype.find(".OCOO.")>-1:
                        score=2500
                    else:
                        if subctype.find("OCMMM.")>-1:
                            score=2000
                        elif subctype.find("OMCMM.")>-1:
                            score=2000
                        elif subctype.find("OMMCM.")>-1:
                            score=2000
                        elif subctype.find("OMMMC.")>-1:
                            score=2000
                        elif subctype.find(".CMMMO")>-1:
                            score=2000
                        elif subctype.find(".MCMMO")>-1:
                            score=2000
                        elif subctype.find(".MMCMO")>-1:
                            score=2000
                        elif subctype.find(".MMMCO")>-1:
                            score=2000
                    
                        elif subctype.find(".MMC.")>-1:
                            score=2000
                        elif subctype.find(".MCM.")>-1:
                            score=2000
                        elif subctype.find(".CMM.")>-1:
                            score=2000
                        elif subctype.find(".C.MM.")>-1:
                            score=2000
                        elif subctype.find(".MM.C.")>-1:
                            score=2000
                        else:
                            if subctype.find(".OOC")>-1:
                                score=400
                            elif subctype.find("COO.")>-1:
                                score=400
                            else:
                                if subctype.find(".MMCO")  > -1: 
                                    score= 200
                                elif subctype.find(".MCMO")  > -1: 
                                    score= 200
                                elif subctype.find(".CMMO")  > -1: 
                                    score= 200
                                elif subctype.find("OMMC.")  > -1: 
                                    score= 200
                                elif subctype.find("OMCM.")  > -1: 
                                    score= 200
                                elif subctype.find("OCMM.")  > -1: 
                                    score= 200
                                elif subctype.find("MOOC")   > -1: 
                                    score= 200
                                elif subctype.find("COOM")   > -1: 
                                    score= 200
                                else:
                                    if subctype.find(".MC.")>-1:
                                        score=50
                                    elif subctype.find(".CM.")>-1:
                                        score=50
                                        
                                    else:
                                        if subctype.find("CM.")>-1:
                                            score=30
                                        elif subctype.find(".CM")>-1:
                                            score=30
                                        else:
                                            if subctype.find("OMMMCO")>-1:             #新增棋型
                                                score=10
                                            elif subctype.find("OCMMMO")>-1:
                                                score=10
                                            elif subctype.find("OMCMMO")>-1:
                                                score=10
                                            elif subctype.find("OCMMMO")>-1:
                                                score=10
                                            elif subctype.find("OMMCMO")>-1:
                                                score=10
                                            else:                             
                                                score=20
        return score
    dict={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15}
    indict={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o'}
    #le=0     #控制strlist循环情况，依次遍历strlist中每个字符串
    strlist=board
    maxloc=[0,0]      #最大落子位置   ,maxlocation   
    #temploc=[0,0]     #临时存放棋子的位置
    blagather=set()   #黑棋集合
    whigather=set()   #白棋集合
    sclength=0    #strlist列表中每个字符串的长度
    blanklist=[]        #存放空白点坐标的列表
    str=""  #存放棋盘上旗子与空点数据
    strchess=""   #存放棋盘上棋子数据
    strchess=strlist
    sclength=len(strchess)
    strchessl=0  #遍历strchess中每个字母
    strchess1_2=0   #用于区分黑棋和白棋，下标为4的倍数即为黑棋
    cal_1=cal_2=0   #用于以下的计算
    while strchessl <sclength/2:        #将黑棋和白棋放到不同的集合
        strchess1_2=2*strchessl  
                                                        #在此处出现了bug，if和else里的strchess1_2竟然不一样
        if strchess1_2%4==0 and strchess1_2!=2:         #虽然二者长得一模一样，但是字母l和数字1无法区分，所以在Python中
            cal_1=dict.get(strchess[strchess1_2])       #一定要区分字母l和数字1
            cal_2=dict.get(strchess[strchess1_2+1])
            blagather.add(cal_1*10**2+cal_2)
        else:
            cal_1=dict.get(strchess[strchess1_2])
            cal_2=dict.get(strchess[strchess1_2+1])
            whigather.add(cal_1*10**2+cal_2)
        strchessl+=1
    i=j=1
    for i in range(1,16):
        for j in range(1,16):
            if i*10**2+j in blagather:
                str+="M"
            elif i*10**2+j in whigather:
                str+="O"
            else:
                str+="."
                blanklist.append(i)
                blanklist.append(j)                           
            j+=1
        str+="\n"   
        i+=1    
    str+="\n"
    blanknumber=0
    subctype=""       #存放棋子四条线上的棋型的字符串
    score=0           #记录棋型得分
    mscount=-100                       #"C"的最大得分
    while blanknumber<(len(blanklist)/2):  #(len(blanklist)/2)
        maxscore=[-10,-10,-10,-10]        #四个位置的的得分  
        subctype_1=subctype_2=1
        subctype_3=subctype_4=1        #代表某个棋子四条线上的棋型的代号
        subctype=""       #存放棋子四条线上的棋型的字符串
        for subctype_1 in range(1,10):
            if 0<=(blanklist[blanknumber*2+1]-6+subctype_1)<15:
                if subctype_1==5:
                    subctype+="C"
                else:
                    subctype+=str[16*(blanklist[blanknumber*2]-1)+blanklist[blanknumber*2+1]-6+subctype_1]
            subctype_1+=1
        score=chescore(subctype)
        maxscore[0]=score
        #print(subctype)
        #subctype+="\n"
        subctype=""       #存放棋子四条线上的棋型的字符串
        for subctype_2 in range(1,10):
            if(0<=(blanklist[blanknumber*2]-6+subctype_2)<15) and (0<=(blanklist[blanknumber*2+1]-6+subctype_2)<15):
                if subctype_2==5:
                    subctype+="C"
                else:
                    subctype+=str[16*(blanklist[blanknumber*2]-6+subctype_2)+blanklist[blanknumber*2+1]-6+subctype_2]
            subctype_2+=1
        score=chescore(subctype)
        maxscore[1]=score
        #subctype+="\n"
        #print(subctype)
        subctype=""       #存放棋子四条线上的棋型的字符串
        for subctype_3 in range(1,10):
            if 0<=(blanklist[blanknumber*2]-6+subctype_3)<15:
                if subctype_3==5:
                    subctype+="C"
                else:
                    subctype+=str[16*(blanklist[blanknumber*2]-6+subctype_3)+blanklist[blanknumber*2+1]-1]
            subctype_3+=1
        score=chescore(subctype)
        maxscore[2]=score
        #subctype+="\n"
        #print(subctype)
        subctype=""       #存放棋子四条线上的棋型的字符串
        for subctype_4 in range(1,10):
            if 0<=(blanklist[blanknumber*2]-6+subctype_4)<15 and 0<=(blanklist[blanknumber*2+1]+4-subctype_4)<15:
                if subctype_4==5:
                    subctype+="C"
                else:
                    subctype+=str[16*(blanklist[blanknumber*2]-6+subctype_4)+blanklist[blanknumber*2+1]+4-subctype_4]
            subctype_4+=1
        score=chescore(subctype)
        maxscore[3]=score
        #print(subctype)
        if mscount<(maxscore[0]+maxscore[1]+maxscore[2]+maxscore[3]):
            mscount=maxscore[0]+maxscore[1]+maxscore[2]+maxscore[3]
            maxloc.pop(-1)
            maxloc.pop(-1)
            maxloc.append(blanklist[blanknumber*2])
            maxloc.append(blanklist[blanknumber*2+1])
        blanknumber+=1
    return indict.get(maxloc[0])+indict.get(maxloc[1])





#赵谕泽部分

def numtochar(board):
    board = board.upper()
    
    if (len(board)//2)%2==0:
        borw = 1
    else:
        borw = 0 
    for index in range(0, len(board), 2):
        if borw == 1:
            dict1[board[index]][board[index+1]] = 'M'
            borw=0
        else:
            dict1[board[index]][board[index+1]] = 'O'  
            borw=1

    return

def judegemodel1(li,dic2,i,j):
    if   "OOOOC" in li or "COOOO" in li:
            dic2[i][j]+=20000
    if "CMMMM" in li or "MCMMM" in li or "MMCMM" in li or "MMMCM" in li or "MMMMC" in li :
            dic2[i][j]+=10000        
    if   "COOO." in li or ".OOOC" in li or ".OOCO." in li or ".OCOO." in li:
            dic2[i][j]+=4000
    if   ".CMMM." in li or ".MCMM." in li or ".MMCM." in li or ".MMMC." in li:
            dic2[i][j]+=3000        
    if   ".OOC" in li or "COO." in li or "MOOOC" in li or "COOOM" in li:
            dic2[i][j]+=1000
    if   "OCMMM." in li or "OMCMM." in li or "OMMCM." in li or "OMMMC." in li or ".CMMMO" in li or ".MCMMO" in li or ".MMCMO" in li or ".MMMCO" in li:
            dic2[i][j]+=2000
    if   ".MMC." in li or ".MCM." in li or ".CMM." in li:
            dic2[i][j]+=700
    if   ".MMCO" in li or ".MCMO" in li or ".CMMO" in li or "OMMC." in li or "OMCM." in li or "OCMM." in li or "MOOC" in li or "COOM" in li:
            dic2[i][j]+=500                   
    if   ".OC." in li or ".CO." in li:
            dic2[i][j]+=200        
    else:
        dic2[i][j]+=1

def judegemode2(li,dic2,i,j):
            
    if "CMMMM" in li or "MCMMM" in li or "MMCMM" in li or "MMMCM" in li or "MMMMC" in li :
            dic2[i][j]+=10000
            
    if   ".CMMM." in li or ".MCMM." in li or ".MMCM." in li or ".MMMC." in li:
            dic2[i][j]+=3000
    
    if   "OCMMM." in li or "OMCMM." in li or "OMMCM." in li or "OMMMC." in li or ".CMMMO" in li or ".MCMMO" in li or ".MMCMO" in li or ".MMMCO" in li:
            dic2[i][j]+=2000
            
    if   ".MMC." in li or ".MCM." in li or ".CMM." in li:
            dic2[i][j]+=700
            
    if   ".MMCO" in li or ".MCMO" in li or ".CMMO" in li or "OMMC." in li or "OMCM." in li or "OCMM." in li or "MOOC" in li or "COOM" in li:
            dic2[i][j]+=500
                                    
    else:
            dic2[i][j]+=1

def getmax(dic):
    max=0
    for i in 'ABCDEFGHIJKLMNO':
        for j in 'ABCDEFGHIJKLMNO':
            if dic[i][j]>max:
                max=dic[i][j]
    for i in 'ABCDEFGHIJKLMNO':
        for j in 'ABCDEFGHIJKLMNO':
            if dic[i][j]==max:
                return(i,j)

def countscore1(dict,dictscore):
    for i in 'ABCDEFGHIJKLMNO':
        for j in 'ABCDEFGHIJKLMNO':
            if dict[i][j]==".":
               dict[i][j]="C"
            if dict[i][j]=="C":
                list1=[]
                list2=[]
                list3=[]
                list4=[]
                x1=i
                x2=j
                
                x3 = x1
                x4 = chr(ord(x2)-4)
                for index in range(10):
                    if chr(ord(x4)+index) <'P' and '@'< chr(ord(x4)+index) and x3 <'P' and '@'< x3:
                        list1.append(dict[x3][chr(ord(x4)+index)])
                    
                    else:
                        #break
                        print('', end='')
                       
                x3 = chr(ord(x1)-4)
                x4 = chr(ord(x2)-4)
                for index in range(10):
                    if chr(ord(x3)+index) <'P' and '@'< chr(ord(x3)+index) and chr(ord(x4)+index) <'P' and '@'< chr(ord(x4)+index):
                        list2.append(dict[chr(ord(x3)+index)][chr(ord(x4)+index)])
                    
                    else:
                        #break
                        print('', end='')
                      
                x3 = chr(ord(x1)-4)
                x4 = x2
                for index in range(10):
                    if chr(ord(x3)+index) <'P' and '@'< chr(ord(x3)+index) and x4 <'P' and '@'< x4:
                        list3.append(dict[chr(ord(x3)+index)][x4])
                    
                    else:
                        #break
                        print('', end='')
                      
                x3 = chr(ord(x1)-4)
                x4 = chr(ord(x2)+4)
                for index in range(10):
                    if chr(ord(x3)+index) <'P' and '@'< chr(ord(x3)+index) and chr(ord(x4)-index) <'P' and '@'< chr(ord(x4)-index):
                        list4.append(dict[chr(ord(x3)+index)][chr(ord(x4)-index)])
                    
                    else:
                        #break
                        print('', end='')
                    
                li1=''.join(list1)
                li2=''.join(list2)
                li3=''.join(list3)
                li4=''.join(list4)
                '''
                if yourstone==jb['creator_stone']:
                    judegemodel(li1,dictscore1,i,j)
                    judegemodel(li2,dictscore1,i,j)
                    judegemodel(li3,dictscore1,i,j)
                    judegemodel(li4,dictscore1,i,j)
                elif yourstone==jb['opponent_stone']:
                    judegemode2(li1,dictscore1,i,j)
                    judegemode2(li2,dictscore1,i,j)
                    judegemode2(li3,dictscore1,i,j)
                    judegemode2(li4,dictscore1,i,j)
                '''
                judegemodel1(li1,dictscore1,i,j)
                judegemodel1(li2,dictscore1,i,j)
                judegemodel1(li3,dictscore1,i,j)
                judegemodel1(li4,dictscore1,i,j)
                list1=[]
                list2=[]
                list3=[]
                list4=[]
                dict[i][j]="." 
    return
    
def getboard(x):    
    litest=x
    #for index in range(0, len(litest), 2):
    li=litest#[index]+litest[index+1]
    numtochar(li)
    countscore1(dict1, dictscore1)
    lis=''.join(getmax(dictscore1))
    return lis.lower()
#zyz1
def hardcore(board):
    # print(board)
    left=[]#左边坐标
    up=[]#上边坐标
    middle=[]#转一维的数字坐标
    left1=[]
    up1=[]
    left2=[]
    up2=[]
    grade=[]
    l=[]#符号化棋盘
    ip=[]#考察点
    pl=''
    pu=''
    p=''
    e=board
    if len(e)==0:
        p='hh'
    else:
        '''
        if len(e)==2 and e!='hh':
            if ord(e[0]-96)<4 or ord(e[0]-96)>12 or ord(e[1]-96)<4 or ord(e[1]-96)>12:
                p='hh'
            
            else:
                pl=e[0]
                pu=chr(ord(e[1])+1)
                p=pl+pu
        
            
        else:
        '''
            
        w=0    
        for i in e:
            if (w%2)==0:
                left1.append(ord(i)-96)
                left.append(ord(i)-96)
            else:
                up1.append(ord(i)-96)
                up.append(ord(i)-96)
            w+=1
        while left1!=[]:
            left2.append(left1.pop())
            up2.append(up1.pop())
        while left2!=[]:
            middle.append((left2.pop()-1)*15+up2.pop())         
         
        m=''
        n=''   
           
        for i in range(0,225):
            m+='.'
            
        f1=len(e)//2
        if f1%2==0:
            for i in range(0,f1):
                for q in range(0,225):
                    if i%2==0:
                        if q==middle[i]-1:
                            n+='M'
                        else:
                            n+=m[q]
                    else:
                        if q==middle[i]-1:
                            n+='O'
                        else:
                            n+=m[q]
                m=n
                n=''
        else: 
            for i in range(0,f1):
                for q in range(0,225):
                    if i%2==0:
                        if q==middle[i]-1:
                            n+='O'
                        else:
                            n+=m[q]
                    else:
                        if q==middle[i]-1:
                            n+='M'
                        else:
                            n+=m[q]
                m=n
                n=''
        for i in range(0,225): 
            l.append(m[i])
                
        #print(l)
           
        for j in range(1,226):
            if j not in middle:
                ip.append(j)
        #print(ip)#考察点
        
        
        
        n1=''
        qixing=[]
        lenth=len(ip)
        for i in range(0,lenth):
            for j in range(ip[i]-4,ip[i]+5):
                w=(ip[i]-1)//15+1
                if w>0 and w<=15:
                    if j>(w-1)*15 and j<=w*15:
                        if j==ip[i]:
                            n1+='C'
                        else:
                            n1+=l[j-1]
            qixing.append(n1)
            n1=''
            h=-4
            for j in range(ip[i]-64,ip[i]+80,16):
                left7=(ip[i]-1)//15+1
                if ip[i]%15==0: 
                    up7=15
                else:
                    up7=ip[i]%15
                if left7+h>0 and left7+h<=15 and up7+h>0 and up7+h<=15:
                    if j==ip[i]:
                        n1+='C'
                    else:
                       n1+=l[j-1]
                h+=1
            qixing.append(n1)
            n1=''
            for j in range(ip[i]-60,ip[i]+75,15):
                if j>0 and j<=225:
                    if j==ip[i]:
                        n1+='C'
                    else:
                        n1+=l[j-1]
            qixing.append(n1)
            n1=''
            h=-4
            k=4
            for j in range(ip[i]-56,ip[i]+70,14):
                left7=(ip[i]-1)//15+1
                if ip[i]%15==0: 
                    up7=15
                else:
                    up7=ip[i]%15            
                if left7+h>0 and left7+h<=15 and up7+k>0 and up7+k<=15:
                    if j==ip[i]:
                        n1+='C'
                    else:
                        n1+=l[j-1]
                h+=1
                k-=1
            qixing.append(n1)
            n1=''
        #print(qixing[0])
        
        
        fen0=["CMMMM", "MCMMM", "MMCMM", "MMMCM","MMMMC"] 
        fen1=["OOOOC","COOOO","OOOCO","OOCOO","OCOOO"]  
        fen2=[".CMMM.",".MCMM.",".MMCM.",".MMMC.","M.MCM.M","MCM.M","M.MCM"] #"C.MMM","MMM.C 
        fen33=["COOO.M","M.OOOC"]
        fen3=["COOO.",".OOOC",".OOCO.",".OCOO."]#新增COOO.M,M.OOOC            
        fen4=["OCMMM.","OMCMM.","OMMCM.","OMMMC.",".CMMMO",".MCMMO",".MMCMO",".MMMCO"]#,
        fen5=[".MMC.",".MCM.",".CMM."]
        fen55=["O.MMC.","O.MCM."]
        fen66=[".OCO.",".MOOCO."]
        fen666=["MOOOC","COOOM"]
        fen6=[".OOC.",".COO."]
        fen7=[".MMCO",".MCMO",".CMMO","OMMC.","OMCM.","OCMM.","MOOC","COOM"]
        fen8=[".MC.",".CM."]#应提高分数
        fen9=[".OOOOC","COOOO."]
        fen10=[".OC.",".OC."]

        fen=0
        count1=0
        for j in range(0,lenth*4):
            count=0
            for k in range(0,len(fen0)):
                if fen0[k] in qixing[j]:
                    fen+=850000
                    count+=1
            for k in range(0,len(fen1)):
                if fen1[k] in qixing[j]:
                    fen+=600000
                    count+=1
            for k in range(0,len(fen2)):
                if fen2[k] in qixing[j]:
                    fen+=30000
                    count+=1
                    
            for k in range(0,len(fen33)):
                if fen33[k] in qixing[j]:
                    fen+=20
                    count+=1
                    
            for k in range(0,len(fen3)):
                if fen3[k] in qixing[j]:
                    fen+=6000
                    count+=1
            for k in range(0,len(fen4)):
                if fen4[k] in qixing[j]:
                    fen+=1500
                    count+=1
            for k in range(0,len(fen5)):
                if fen5[k] in qixing[j]:
                    fen+=1200
                    count+=1  
                    
            for k in range(0,len(fen55)):
                if fen55[k] in qixing[j]:
                    fen+=-20
                    count+=1  
                    
            for k in range(0,len(fen666)):
                if fen666[k] in qixing[j]:
                    fen+=620
                    count+=1 
            for k in range(0,len(fen66)):
                if fen66[k] in qixing[j]:
                    fen+=619
                    count+=1 
            for k in range(0,len(fen6)):
                if fen6[k] in qixing[j]:
                    fen+=621
                    count+=1
                    
            for k in range(0,len(fen7)):
                if fen7[k] in qixing[j]:
                    fen+=400
                    count+=1 
                    
            for k in range(0,len(fen8)):
                if fen8[k] in qixing[j]:
                    fen+=200
                    count+=1

                    
            for k in range(0,len(fen10)):
                if fen10[k] in qixing[j]:
                    fen+=25
                    count+=1         

            for k in range(0,len(fen9)):
                if fen9[k] in qixing[j]:
                    fen+=0
                    count+=1     

 

            if count==0:
                fen+=20
            count1+=1
            if(count1==4):
                grade.append(fen)
                fen=0
                count1=0
        #print(fzong)
        grade1=[]#存分数最大的下标
        count2=0
        sp=max(grade)
        for i in grade:
            if i==sp:
                grade1.append(count2)
            count2+=1
        lenth2=len(grade1)
        if lenth2==1:
            c=grade1[0]
        else:
            c1=random.randint(0,lenth2-1)
            c=grade1[c1]   
        #c=grade.index(max(grade))
        z=ip[c]
        zuo=(z-1)//15+1
        if z%15==0:   
            shang=15
        else:
            shang=z%15
        pl=chr(zuo+96)
        pu=chr(shang+96)
        p=pl+pu
        # print(p)
    return p




#张智煊部分

list=[['.'for i in range(1,16)] for j in range(1,16)]
def shuaxin(board,list):
    j=0
    k=2
    if (len(board)/2)%2==1:#下白棋
        for i in range(0,len(board)//4+1):
            list[ord(board[j])-97][ord(board[j+1])-97]='O'
            j+=4
        for i in range(0,len(board)//4):
            list[ord(board[k])-97][ord(board[k+1])-97]='M'
            k+=4
    if (len(board)/2)%2==0:#下黑棋
        for i in range(0,len(board)//4):
            list[ord(board[j])-97][ord(board[j+1])-97]='M'
            j+=4
        for i in range(0,len(board)//4):
            list[ord(board[k])-97][ord(board[k+1])-97]='O'
            k+=4

list1=[[['1','2','3','4','5','6',0] for i in range(1,16)] for j in range(1,16)]

def shuaxin1(list1):
    for i in range(0,15):
        for j in range(0,15):
            for k in range(0,6):
                list1[i][j][k]='1'
            list1[i][j][6]=0

def play_chess1(board,list):
    #下白棋
    if (len(board)/2)%2==1:
        for i in range(0,15):
            for j in range(0,15):
                if list[i][j]=='.':
                    list[i][j]='C'
                    #第1行
                    a=-4
                    line1=''
                    for k in range(0,9):
                        if j+a<0 or j+a>14:
                            a+=1
                            continue
                        line1=line1+list[i][j+a]
                        a+=1
                    list1[i][j][0]=line1
                    #第2行
                    a=-4
                    line2=''
                    for k in range(0,9):
                        if i+a<0 or i+a>14:
                            a+=1
                            continue
                        if j+a<0 or j+a>14:
                            a+=1
                            continue
                        line2=line2+list[i+a][j+a]
                        a+=1
                    list1[i][j][1]=line2
                    #第3行
                    a=-4
                    line3=''
                    for k in range(0,9):
                        if i+a<0 or i+a>14:
                            a+=1
                            continue
                        line3=line3+list[i+a][j]
                        a+=1
                    list1[i][j][2]=line3
                    #第4行
                    a=-4
                    b=4
                    line4=''
                    for k in range(0,9):
                        if i+a<0 or i+a>14:
                            a+=1
                            b-=1
                            continue
                        if j+b<0 or j+b>14:
                            b-=1
                            a+=1
                            continue
                        line4=line4+list[i+a][j+b]
                        a+=1
                        b-=1
                    list1[i][j][3]=line4
                    list[i][j]='.'
                else:
                    continue
        
        for i in range(0,15):
            for j in range(0,15):
                for k in range(0,4):
                    if 'CMMMM' in list1[i][j][k] or 'MCMMM' in list1[i][j][k] or 'MMCMM' in list1[i][j][k] or 'MMMCM' in list1[i][j][k] or 'MMMMC' in list1[i][j][k]:
                        list1[i][j][6]+=100000
                        list1[i][j][4]=i
                        list1[i][j][5]=j
                    if 'OOOOC' in list1[i][j][k] or 'COOOO' in list1[i][j][k] or 'OCOOO' in list1[i][j][k] or 'OOCOO' in list1[i][j][k] or 'OOOCO' in list1[i][j][k]:
                        list1[i][j][6]+=60000
                        if list1[i][j][6]==60000:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if '.CMMM.' in list1[i][j][k] or '.MCMM.' in list1[i][j][k] or '.MMCM.' in list1[i][j][k] or '.MMMC.' in list1[i][j][k]:
                        list1[i][j][6]+=8000
                        if list1[i][j][6]==8000:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if 'COOO.' in list1[i][j][k] or '.OOOC' in list1[i][j][k]:
                        list1[i][j][6]+=3500
                        if list1[i][j][6]==3500:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if '.OCOO.' in list1[i][j][k] or '.OOCO.' in list1[i][j][k]:
                        list1[i][j][6]+=3500
                        if list1[i][j][6]==3500:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if '.CO.O.' in list1[i][j][k] or '.O.OC.' in list1[i][j][k]:
                        list1[i][j][6]+=2000
                        if list1[i][j][6]==2000:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if '.CMMM' in list1[i][j][k] or '.MCMM' in list1[i][j][k] or '.MMCM' in list1[i][j][k] or '.MMMC' in list1[i][j][k] or 'MMMC.' in list1[i][j][k] or 'MMCM.' in list1[i][j][k] or 'MCMM.' in list1[i][j][k] or 'CMMM.' in list1[i][j][k]:
                        list1[i][j][6]+=3000
                        if list1[i][j][6]==3000:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if 'CM.M' in list1[i][j][k] or 'M.MC' in list1[i][j][k]:
                        list1[i][j][6]+=1500
                        if list1[i][j][6]==1500:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if '.OCOO' in list1[i][j][k] or '.OOCO' in list1[i][j][k] or 'OCOO.' in list1[i][j][k] or 'OOCO.' in list1[i][j][k]:
                        list1[i][j][6]+=2000
                        if list1[i][j][6]==2000:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if '.MMC.' in list1[i][j][k] or '.MCM.' in list1[i][j][k] or '.CMM.' in list1[i][j][k]:
                        list1[i][j][6]+=1000
                        if list1[i][j][6]==1000:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if '.CM.M.' in list1[i][j][k] or '.M.MC.' in list1[i][j][k]:
                        list1[i][j][6]+=700
                        if list1[i][j][6]==700:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if '.OOC.' in list1[i][j][k] or '.COO.' in list1[i][j][k] or '.OCO.' in list1[i][j][k]:
                        list1[i][j][6]+=650
                        if list1[i][j][6]==650:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if 'CM.M' in list1[i][j][k] or 'M.MC' in list1[i][j][k]:
                        list1[i][j][6]+=500
                        if list1[i][j][6]==500:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if 'C.OO' in list1[i][j][k] or 'OO.C' in list1[i][j][k]:
                        list1[i][j][6]+=400
                        if list1[i][j][6]==400:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if '.MMCO' in list1[i][j][k] or '.MCMO' in list1[i][j][k] or '.CMMO' in list1[i][j][k] or 'OMMC.' in list1[i][j][k] or 'OMCM.' in list1[i][j][k] or 'OCMM.' in list1[i][j][k]:
                        list1[i][j][6]+=200
                        if list1[i][j][6]==200:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if '.OOCM' in list1[i][j][k] or '.OCOM' in list1[i][j][k] or '.COOM' in list1[i][j][k] or 'MOOC.' in list1[i][j][k] or 'MOCO.' in list1[i][j][k] or 'MCOO.' in list1[i][j][k]:
                        list1[i][j][6]+=200
                        if list1[i][j][6]==200:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if '.MC.' in list1[i][j][k] or '.CM.' in list1[i][j][k]:
                        list1[i][j][6]+=50
                        if list1[i][j][6]==50:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if '.OC.' in list1[i][j][k] or '.CO.' in list1[i][j][k]:
                        list1[i][j][6]+=50
                        if list1[i][j][6]==50:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if '.MOC.' in list1[i][j][k] or '.CMO.' in list1[i][j][k] or '.COM.' in list1[i][j][k] or '.OMC.' in list1[i][j][k]:
                        list1[i][j][6]+=50
                        if list1[i][j][6]==50:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
        zuobiao=['0','0']
        score=0
        for i in range(0,15):
            for j in range(0,15):
                if i==0 and j==0:
                    continue
                if list1[i][j][6]>score:
                    score=list1[i][j][6]
                    zuobiao[0]=chr(list1[i][j][4]+97)
                    zuobiao[1]=chr(list1[i][j][5]+97)
        return zuobiao[0]+zuobiao[1]
             
    #下黑棋
    if (len(board)/2)%2==0:
        for i in range(0,15):
            for j in range(0,15):
                if list[i][j]=='.':
                    list[i][j]='C'
                    #第1行
                    a=-4
                    line1=''
                    for k in range(0,9):
                        if j+a<0 or j+a>14:
                            a+=1
                            continue
                        line1=line1+list[i][j+a]
                        a+=1
                    list1[i][j][0]=line1
                    #第2行
                    a=-4
                    line2=''
                    for k in range(0,9):
                        if i+a<0 or i+a>14:
                            a+=1
                            continue
                        if j+a<0 or j+a>14:
                            a+=1
                            continue
                        line2=line2+list[i+a][j+a]
                        a+=1
                    list1[i][j][1]=line2
                    #第3行
                    a=-4
                    line3=''
                    for k in range(0,9):
                        if i+a<0 or i+a>14:
                            a+=1
                            continue
                        line3=line3+list[i+a][j]
                        a+=1
                    list1[i][j][2]=line3
                    #第4行
                    a=-4
                    b=4
                    line4=''
                    for k in range(0,9):
                        if i+a<0 or i+a>14:
                            a+=1
                            b-=1
                            continue
                        if j+b<0 or j+b>14:
                            b-=1
                            a+=1
                            continue
                        line4=line4+list[i+a][j+b]
                        a+=1
                        b-=1
                    list1[i][j][3]=line4
                    list[i][j]='.'
                else:
                    continue
        
        for i in range(0,15):
            for j in range(0,15):
                for k in range(0,4):
                    if 'CMMMM' in list1[i][j][k] or 'MCMMM' in list1[i][j][k] or 'MMCMM' in list1[i][j][k] or 'MMMCM' in list1[i][j][k] or 'MMMMC' in list1[i][j][k]:
                        list1[i][j][6]+=100000
                        list1[i][j][4]=i
                        list1[i][j][5]=j
                    if 'OOOOC' in list1[i][j][k] or 'COOOO' in list1[i][j][k] or 'OCOOO' in list1[i][j][k] or 'OOCOO' in list1[i][j][k] or 'OOOCO' in list1[i][j][k]:
                        list1[i][j][6]+=60000
                        if list1[i][j][6]==60000:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if '.CMMM.' in list1[i][j][k] or '.MCMM.' in list1[i][j][k] or '.MMCM.' in list1[i][j][k] or '.MMMC.' in list1[i][j][k]:
                        list1[i][j][6]+=8000
                        if list1[i][j][6]==8000:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if 'COOO.' in list1[i][j][k] or '.OOOC' in list1[i][j][k]:
                        list1[i][j][6]+=3500
                        if list1[i][j][6]==3500:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if '.OCOO.' in list1[i][j][k] or '.OOCO.' in list1[i][j][k]:
                        list1[i][j][6]+=3500
                        if list1[i][j][6]==3500:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if '.CO.O.' in list1[i][j][k] or '.O.OC.' in list1[i][j][k]:
                        list1[i][j][6]+=2000
                        if list1[i][j][6]==2000:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if '.CMMM' in list1[i][j][k] or '.MCMM' in list1[i][j][k] or '.MMCM' in list1[i][j][k] or '.MMMC' in list1[i][j][k] or 'MMMC.' in list1[i][j][k] or 'MMCM.' in list1[i][j][k] or 'MCMM.' in list1[i][j][k] or 'CMMM.' in list1[i][j][k]:
                        list1[i][j][6]+=3000
                        if list1[i][j][6]==3000:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if 'CM.M' in list1[i][j][k] or 'M.MC' in list1[i][j][k]:
                        list1[i][j][6]+=1500
                        if list1[i][j][6]==1500:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if '.OCOO' in list1[i][j][k] or '.OOCO' in list1[i][j][k] or 'OCOO.' in list1[i][j][k] or 'OOCO.' in list1[i][j][k]:
                        list1[i][j][6]+=2000
                        if list1[i][j][6]==2000:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if '.MMC.' in list1[i][j][k] or '.MCM.' in list1[i][j][k] or '.CMM.' in list1[i][j][k]:
                        list1[i][j][6]+=1000
                        if list1[i][j][6]==1000:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if '.CM.M.' in list1[i][j][k] or '.M.MC.' in list1[i][j][k]:
                        list1[i][j][6]+=700
                        if list1[i][j][6]==700:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if '.OOC.' in list1[i][j][k] or '.COO.' in list1[i][j][k] or '.OCO.' in list1[i][j][k]:
                        list1[i][j][6]+=650
                        if list1[i][j][6]==650:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if 'CM.M' in list1[i][j][k] or 'M.MC' in list1[i][j][k]:
                        list1[i][j][6]+=500
                        if list1[i][j][6]==500:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if 'C.OO' in list1[i][j][k] or 'OO.C' in list1[i][j][k]:
                        list1[i][j][6]+=400
                        if list1[i][j][6]==400:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if '.MMCO' in list1[i][j][k] or '.MCMO' in list1[i][j][k] or '.CMMO' in list1[i][j][k] or 'OMMC.' in list1[i][j][k] or 'OMCM.' in list1[i][j][k] or 'OCMM.' in list1[i][j][k]:
                        list1[i][j][6]+=200
                        if list1[i][j][6]==200:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if '.OOCM' in list1[i][j][k] or '.OCOM' in list1[i][j][k] or '.COOM' in list1[i][j][k] or 'MOOC.' in list1[i][j][k] or 'MOCO.' in list1[i][j][k] or 'MCOO.' in list1[i][j][k]:
                        list1[i][j][6]+=200
                        if list1[i][j][6]==200:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if '.MC.' in list1[i][j][k] or '.CM.' in list1[i][j][k]:
                        list1[i][j][6]+=50
                        if list1[i][j][6]==50:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if '.OC.' in list1[i][j][k] or '.CO.' in list1[i][j][k]:
                        list1[i][j][6]+=50
                        if list1[i][j][6]==50:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
                    if '.MOC.' in list1[i][j][k] or '.CMO.' in list1[i][j][k] or '.COM.' in list1[i][j][k] or '.OMC.' in list1[i][j][k]:
                        list1[i][j][6]+=50
                        if list1[i][j][6]==50:
                            list1[i][j][4]=i
                            list1[i][j][5]=j
        zuobiao=['0','0']
        score=0
        for i in range(0,15):
            for j in range(0,15):
                if i==0 and j==0:
                    continue
                if list1[i][j][6]>score:
                    score=list1[i][j][6]
                    zuobiao[0]=chr(list1[i][j][4]+97)
                    zuobiao[1]=chr(list1[i][j][5]+97)
        return zuobiao[0]+zuobiao[1]









#决策部分

def decision(dict1,dict2,dict3,dict4,board):
    length=len(board)
    if length%2==0:
        #四个人落子位置相同
        if dict1["coored"]==dict2["coored"] and dict2["coored"]==dict3["coored"] and dict3["coored"]==dict4["coored"]:
            return dict1["coored"]
        #三人相同与另一人不同
        if dict1["coored"]==dict2["coored"] and dict2["coored"]==dict3["coored"] and dict3["coored"]!=dict4["coored"]:
            if dict1["bpower"]+dict2["bpower"]+dict3["bpower"] > dict4["bpower"]:
                return dict1["coored"]
            else:
                return dict4["coored"]
        if dict1["coored"]==dict2["coored"] and dict2["coored"]==dict4["coored"] and dict4["coored"]!=dict3["coored"]:
            if dict1["bpower"]+dict2["bpower"]+dict4["bpower"] > dict3["bpower"]:
                return dict1["coored"]
            else:
                return dict3["coored"]
        if dict1["coored"]==dict3["coored"] and dict3["coored"]==dict4["coored"] and dict4["coored"]!=dict2["coored"]:
            if dict1["bpower"]+dict3["bpower"]+dict4["bpower"] > dict2["bpower"]:
                return dict1["coored"]
            else:
                return dict2["coored"] 
        if dict2["coored"]==dict3["coored"] and dict3["coored"]==dict4["coored"] and dict4["coored"]!=dict1["coored"]:
            if dict2["bpower"]+dict3["bpower"]+dict4["bpower"] > dict1["bpower"]:
                return dict2["coored"]
            else:
                return dict1["coored"] 
        #两人两人相同
        if dict1["coored"]==dict2["coored"] and dict3["coored"]==dict4["coored"] and dict2["coored"]==dict3["coored"]:
            if dict1["bpower"]+dict2["bpower"] > dict3["bpower"]+dict4["bpower"]:
                return dict1["coored"]
            else:
                return dict4["coored"]
        if dict1["coored"]==dict3["coored"] and dict2["coored"]==dict4["coored"] and dict1["coored"]==dict2["coored"]:
            if dict1["bpower"]+dict3["bpower"] > dict2["bpower"]+dict4["bpower"]:
                return dict1["coored"]
            else:
                return dict2["coored"]
        if dict1["coored"]==dict4["coored"] and dict2["coored"]==dict3["coored"] and dict1["coored"]==dict2["coored"]:
            if dict1["bpower"]+dict4["bpower"] > dict2["bpower"]+dict3["bpower"]:
                return dict1["coored"]
            else:
                return dict2["coored"] 
        #两人与另两人分三组全不同
        if dict1["coored"]==dict2["coored"] and dict1["coored"]!=dict3["coored"] and dict1["coored"]!=dict4["coored"]:
            if dict1["bpower"]+dict2["bpower"] == max(dict1["bpower"]+dict2["bpower"],dict3["bpower"],dict4["bpower"]):
                return dict1["coored"]
            elif dict3["bpower"] == max(dict1["bpower"]+dict2["bpower"],dict3["bpower"],dict4["bpower"]):
                return dict3["coored"]
            else:
                return dict4["coored"]
        if dict1["coored"]==dict3["coored"] and dict1["coored"]!=dict2["coored"] and dict1["coored"]!=dict4["coored"]:
            if dict1["bpower"]+dict3["bpower"] == max(dict1["bpower"]+dict3["bpower"],dict2["bpower"],dict4["bpower"]):
                return dict1["coored"]
            elif dict2["bpower"] == max(dict1["bpower"]+dict3["bpower"],dict2["bpower"],dict4["bpower"]):
                return dict2["coored"]
            else:
                return dict4["coored"]
        if dict1["coored"]==dict4["coored"] and dict1["coored"]!=dict2["coored"] and dict1["coored"]!=dict3["coored"]:
            if dict1["bpower"]+dict4["bpower"] == max(dict1["bpower"]+dict4["bpower"],dict2["bpower"],dict3["bpower"]):
                return dict1["coored"]
            elif dict2["bpower"] == max(dict1["bpower"]+dict4["bpower"],dict2["bpower"],dict3["bpower"]):
                return dict2["coored"]
            else:
                return dict3["coored"]
        if dict2["coored"]==dict3["coored"] and dict2["coored"]!=dict1["coored"] and dict2["coored"]!=dict4["coored"]:
            if dict2["bpower"]+dict3["bpower"] == max(dict2["bpower"]+dict3["bpower"],dict1["bpower"],dict4["bpower"]):
                return dict2["coored"]
            elif dict1["bpower"] == max(dict2["bpower"]+dict3["bpower"],dict1["bpower"],dict4["bpower"]):
                return dict1["coored"]
            else:
                return dict4["coored"]
        if dict2["coored"]==dict4["coored"] and dict2["coored"]!=dict3["coored"] and dict2["coored"]!=dict1["coored"]:
            if dict2["bpower"]+dict4["bpower"] == max(dict2["bpower"]+dict4["bpower"],dict1["bpower"],dict3["bpower"]):
                return dict2["coored"]
            elif dict1["bpower"] == max(dict2["bpower"]+dict4["bpower"],dict1["bpower"],dict3["bpower"]):
                return dict1["coored"]
            else:
                return dict3["coored"]
        #四人各个不同
        if dict1["coored"]!=dict2["coored"] and dict2["coored"]!=dict3["coored"] and dict3["coored"]!=dict4["coored"] and dict1["coored"]!=dict3["coored"] and dict2["coored"]!=dict4["coored"]:
            if dict1["bpower"]==max(dict1["bpower"],dict2["bpower"],dict3["bpower"],dict4["bpower"]):
                return dict1["coored"]
            elif dict2["bpower"]==max(dict1["bpower"],dict2["bpower"],dict3["bpower"],dict4["bpower"]):
                return dict2["coored"]
            elif dict3["bpower"]==max(dict1["bpower"],dict2["bpower"],dict3["bpower"],dict4["bpower"]):
                return dict3["coored"]
            else:
                return dict4["coored"]
    else:
        #四个人落子位置相同
        if dict1["coored"]==dict2["coored"] and dict2["coored"]==dict3["coored"] and dict3["coored"]==dict4["coored"]:
            return dict1["coored"]
        #三人相同与另一人不同
        if dict1["coored"]==dict2["coored"] and dict2["coored"]==dict3["coored"] and dict3["coored"]!=dict4["coored"]:
            if dict1["wpower"]+dict2["wpower"]+dict3["wpower"] > dict4["wpower"]:
                return dict1["coored"]
            else:
                return dict4["coored"]
        if dict1["coored"]==dict2["coored"] and dict2["coored"]==dict4["coored"] and dict4["coored"]!=dict3["coored"]:
            if dict1["wpower"]+dict2["wpower"]+dict4["wpower"] > dict3["wpower"]:
                return dict1["coored"]
            else:
                return dict3["coored"]
        if dict1["coored"]==dict3["coored"] and dict3["coored"]==dict4["coored"] and dict4["coored"]!=dict2["coored"]:
            if dict1["wpower"]+dict3["wpower"]+dict4["wpower"] > dict2["wpower"]:
                return dict1["coored"]
            else:
                return dict2["coored"] 
        if dict2["coored"]==dict3["coored"] and dict3["coored"]==dict4["coored"] and dict4["coored"]!=dict1["coored"]:
            if dict2["wpower"]+dict3["wpower"]+dict4["wpower"] > dict1["wpower"]:
                return dict2["coored"]
            else:
                return dict1["coored"] 
        #两人两人相同
        if dict1["coored"]==dict2["coored"] and dict3["coored"]==dict4["coored"] and dict1["coored"]!=dict3["coored"]:
            if dict1["wpower"]+dict2["wpower"] > dict3["wpower"]+dict4["wpower"]:
                return dict1["coored"]
            else:
                return dict4["coored"]
        if dict1["coored"]==dict3["coored"] and dict2["coored"]==dict4["coored"] and dict1["coored"]!=dict2["coored"]:
            if dict1["wpower"]+dict3["wpower"] > dict2["wpower"]+dict4["wpower"]:
                return dict1["coored"]
            else:
                return dict2["coored"]
        if dict1["coored"]==dict4["coored"] and dict2["coored"]==dict3["coored"] and dict1["coored"]!=dict2["coored"]:
            if dict1["wpower"]+dict4["wpower"] > dict3["wpower"]+dict2["wpower"]:
                return dict1["coored"]
            else:
                return dict2["coored"] 
        #两人与另两人分三组全不同
        if dict1["coored"]==dict2["coored"] and dict1["coored"]!=dict3["coored"] and dict1["coored"]!=dict4["coored"]:
            if dict1["wpower"]+dict2["wpower"] == max(dict1["wpower"]+dict2["wpower"],dict3["wpower"],dict4["wpower"]):
                return dict1["coored"]
            elif dict3["wpower"] == max(dict1["wpower"]+dict2["wpower"],dict3["wpower"],dict4["wpower"]):
                return dict3["coored"]
            else:
                return dict4["coored"]
        if dict1["coored"]==dict3["coored"] and dict1["coored"]!=dict2["coored"] and dict1["coored"]!=dict4["coored"]:
            if dict1["wpower"]+dict3["wpower"] == max(dict1["wpower"]+dict3["wpower"],dict2["wpower"],dict4["wpower"]):
                return dict1["coored"]
            elif dict2["wpower"] == max(dict1["wpower"]+dict3["wpower"],dict2["wpower"],dict4["wpower"]):
                return dict2["coored"]
            else:
                return dict4["coored"]
        if dict1["coored"]==dict4["coored"] and dict1["coored"]!=dict2["coored"] and dict1["coored"]!=dict3["coored"]:
            if dict1["wpower"]+dict4["wpower"] == max(dict1["wpower"]+dict4["wpower"],dict2["wpower"],dict3["wpower"]):
                return dict1["coored"]
            elif dict2["wpower"] == max(dict1["wpower"]+dict4["wpower"],dict2["wpower"],dict3["wpower"]):
                return dict2["coored"]
            else:
                return dict3["coored"]
        if dict2["coored"]==dict3["coored"] and dict2["coored"]!=dict1["coored"] and dict2["coored"]!=dict4["coored"]:
            if dict2["wpower"]+dict3["wpower"] == max(dict2["wpower"]+dict3["wpower"],dict1["wpower"],dict4["wpower"]):
                return dict2["coored"]
            elif dict1["wpower"] == max(dict2["wpower"]+dict3["wpower"],dict1["wpower"],dict4["wpower"]):
                return dict1["coored"]
            else:
                return dict4["coored"]
        if dict2["coored"]==dict4["coored"] and dict2["coored"]!=dict3["coored"] and dict2["coored"]!=dict1["coored"]:
            if dict2["wpower"]+dict4["wpower"] == max(dict2["wpower"]+dict4["wpower"],dict1["wpower"],dict3["wpower"]):
                return dict2["coored"]
            elif dict1["wpower"] == max(dict2["wpower"]+dict4["wpower"],dict1["wpower"],dict3["wpower"]):
                return dict1["coored"]
            else:
                return dict3["coored"]
        #四人各个不同
        if dict1["coored"]!=dict2["coored"] and dict2["coored"]!=dict3["coored"] and dict3["coored"]!=dict4["coored"] and dict1["coored"]!=dict3["coored"] and dict2["coored"]!=dict4["coored"]:
            if dict1["wpower"]==max(dict1["wpower"],dict2["wpower"],dict3["wpower"],dict4["wpower"]):
                return dict1["coored"]
            elif dict2["wpower"]==max(dict1["wpower"],dict2["wpower"],dict3["wpower"],dict4["wpower"]):
                return dict2["coored"]
            elif dict3["wpower"]==max(dict1["wpower"],dict2["wpower"],dict3["wpower"],dict4["wpower"]):
                return dict3["coored"]
            else:
                return dict4["coored"]

def text_save(content,filename,mode='a'):
    # Try to save a list variable in txt file.
    file = open(filename,mode)
    for i in range(len(content)):
        file.write(str(content[i])+'\n')
    file.close()



user='gravity'
password='hello, world!'
password=encryption(password)
f1 = urllib.request.urlopen("http://183.175.12.27:8000/join_game"+"/?user="+user+"&password="+password+"&data_type="+"json")
game_id=json.loads(f1.read())["game_id"]
game_id=str(game_id)
print(game_id)
f2 = urllib.request.urlopen("http://183.175.12.27:8000/check_game/"+game_id)
chack_game=json.loads(f2.read())

current_turn=chack_game["current_turn"]
winner=chack_game["winner"]
ready=chack_game["ready"]
board=chack_game["board"]
creator=chack_game["creator"]
opponent=chack_game["opponent"]
print('是否准备好')
print(ready)

while ready=='False':
    if ready=='True':
        # print('游戏准备开始')
        break
    else:
        time.sleep( 6 )
        f2 = urllib.request.urlopen("http://183.175.12.27:8000/check_game/"+game_id)
        chack_game=json.loads(f2.read())
        ready=chack_game["ready"]

print('游戏状态')
print(ready)

a = urllib.request.urlopen("http://183.175.12.27:8000/join_game"+"/?user="+user+"&password="+password+"&data_type="+"json")
b=json.loads(a.read())
print(b['game_id'])
game_id=str(b['game_id'])

while winner=='None':    
 p = urllib.request.urlopen("http://183.175.12.27:8000/check_game/"+game_id)
 q=json.loads(p.read())
 board=str(q['board'])
 winner=str(q['winner'])
 current_turn=str(q['current_turn'])
 if current_turn=='gravity':
   if board =='':
      coord='hh'
   else:   
       dic1={"bpower": 4,"wpower": 2,"coored":'gg' }
       dic2={"bpower": 3,"wpower": 1,"coored":'gg' }
       dic3={"bpower": 2,"wpower": 3,"coored":'gg' }
       dic4={"bpower": 1,"wpower": 4,"coored":'gg' }

        #刘征轩下棋
       print("刘征轩"+play_chess(board, dict1, dictscore1))
       dic1["coored"]=play_chess(board, dict1, dictscore1)
       clear(dict1,dictscore1)

       #董至彪下棋
       print("董至彪"+getMark(board))
       dic2["coored"]=getMark(board)


       #赵谕泽下棋
       print("赵谕泽"+hardcore(board))
       dic3["coored"]=hardcore(board)
       clear(dict1,dictscore1)

       #张智煊下棋
       shuaxin(board,list)
       dic4["coored"]=play_chess1(board,list)
       print("张智煊"+play_chess1(board,list))
       shuaxin1(list1)

       print("---最终决策---",end="")
       print(decision(dic1, dic2, dic3, dic4, board))
       coord=decision(dic1, dic2, dic3, dic4, board)
       test_text = ['刘'+dic1["coored"],'董'+dic2["coored"],'赵'+dic3["coored"],'张'+dic4["coored"],'最终落子'+coord+'落子后棋局'+board]
       text_save(test_text,'name111.txt')
       clear(dict1,dictscore1)        
   i = urllib.request.urlopen("http://183.175.12.27:8000/play_game/"+game_id+"/?user="+user+"&password="+password+"&coord="+coord)
   j=json.loads(i.read())
   print(board)
 else:
   time.sleep(5)   
print(winner)








