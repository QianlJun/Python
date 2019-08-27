#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 19:24:11 2017

@author: yezi
"""
#http://www.cell.com/action/doSearch?journalCode=cell&seriesISSNFltraddfilter=0092-8674&occurrences=all&searchText=crispr&searchType=quick&searchScope=series&dateYear1field=custom&dateYearRange1field=20172017&selectedSType=range-2017&filterModify=true&contentType=articles&startPage=0#navigation



import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r = requests.get(url)
        return r.text
    except:
        return ""
    
def getInfo(slist,fpath):
    count = 0
    
    for url in slist:
#        url.append('http://www.cell.com/action/doSearch?journalCode=cell&seriesISSNFltraddfilter=0092-8674&occurrences=all&searchText=crispr&searchType=quick&searchScope=series&dateYear1field=custom&dateYearRange1field=20172017&selectedSType=range-2017&filterModify=true&contentType=articles&startPage=%d#navigation'%i)              
        html = getHTMLText(url)
        try:
            if html == "":
                continue
                    
            soup = BeautifulSoup(html,'html.parser')
            titlename = soup.find_all('h2',attrs={'class':'title'})
            
            result = []
            for i in titlename:
                result.append(i.text)
                
            with open(fpath,'a') as f:
                f.write(str(result)+'\n')
                count = count + 1
                print('\r当前进度： {:.2f}%'.format(count*100/len(slist)),end = '')
        except:
            count = count +1
            print('\r当前进度： {:.2f}%'.format(count*100/len(slist)),end = '')
            continue
    
def main():
#    first_url = 'http://www.cell.com/action/doSearch?journalCode=cell&seriesISSNFltraddfilter=0092-8674&occurrences=all&searchText=crispr&searchType=quick&searchScope=series&dateYear1field=custom&dateYearRange1field=20172017&selectedSType=range-2017&filterModify=true&contentType=articles&startPage=#navigation'
    output_file = '/Users/yezi/Desktop/01-26-cellword.txt'
    slist=[]
    for i in range(0,5):
        slist.append('http://www.cell.com/action/doSearch?searchType=quick&searchText=crispr&occurrences=all&journalCode=&searchScope=fullSite&startPage=%d#navigation'%i)     
    getInfo(slist,output_file)
    
main()