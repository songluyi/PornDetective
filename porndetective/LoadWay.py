# -*- coding: utf-8 -*-
# 2017/1/2 10:40
"""
-------------------------------------------------------------------------------
Function:   add some load way to convenient guys
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
import os
import os.path
import requests
import multiprocessing
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from porndetective import PornDetective
def folder_way(folder_path):
    pic_list=[]
    root_dir=folder_path
    print('Detective is working...')
    print('If the disk is too large to scan, it may cost hundreds hours')
    for parent,dir_names,file_names in os.walk(root_dir):    #Three parameters：return 1.parent path 2.folder name 3.file name
        for f in file_names:
            # support mainstream pic format you can add as you want
            if (f.find('.jpg') != -1 or f.find('.png') != -1 or f.find('.gif') != -1 or f.find('.bmp') != -1) and (f.find('$')==-1)\
                    and (parent.find('$')==-1):
                    pic_list.append(os.path.join(parent,f))
    if len(pic_list)>1000:
        new_pic_list=cut_list(pic_list)
        pool_size=multiprocessing.cpu_count()*2
        pool=ThreadPool(pool_size)
        for part_url_list in new_pic_list:
            new = list(map(PornDetective, part_url_list))
            pool.map(PornDetective.parse, new)
        pool.close()
        pool.join()
    else:
        pool=ThreadPool(4)
        new=list(map(PornDetective, pic_list))
        pool.map(PornDetective.parse, new)
        pool.close()
        pool.join()

def url_pic_list(url_list):

    if not os.path.exists('porn_url_pic'):
        os.mkdir('porn_url_pic')
    current_path=os.path.join(os.getcwd(),'porn_url_pic')
    store_pic_list=list(map(lambda x:current_path+'\\'+x.split('/')[-1],url_list))
    count=0
    for url in url_list:
        f=requests.get(url)
        try:
            with open(store_pic_list[count],'wb') as temp:
                temp.write(f.content)
            count += 1
            print('Finish one pic download mission, please wait...')
        except NameError:
            break
    folder_way('porn_url_pic')
# if u can chase me, I will HeiHeiHei
def HeiHeiHei():
    print('This pic lists are too large, if u can scan all ,I will heiheihei')

def cut_list(large_url_list):
    new_list=[]
    cut_count=len(large_url_list)//100
    for i in range(cut_count):
        new_list.append(large_url_list[i*100:(i+1)*100])
    list_tail_num = len(large_url_list)-cut_count*100
    new_list.append(large_url_list[-list_tail_num:-1])
    return new_list


def _download_schedule(a,b,c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print('%.2f%%' % per)
