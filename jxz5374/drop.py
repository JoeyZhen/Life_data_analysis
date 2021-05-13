"""
file:drop.py
author: Joey Zhen
created: 12/09/2017
"""

from utils import *

from jxz5374.utils import Range, read_data, filter_region


def difference(country):
    """
    This function returns the key for sorting the countries largest number of drop of life expectancy
    :param country object
    :return: key
    """
    return country.value2-country.value1
def sorted_drop_data(data):
    """
    This function figures out the largest number in drop of life expectancy for all countries and sorts in a list.
    :param large dictory
    pre-conditions:
    post-conditons:
    :return:
    """
    list = []
    country1 = data[0]
    for i in country1:
        lst=country1[i].expectancy
        s=0
        check=chcountry(lst)
        if check == True:
            while True:
                if lst[s] == "":
                    s+=1
                    if s>=len(lst):
                        break
                else:
                    break
            e=s+1
            while True:
                if lst[e]=="":
                    e+=1
                    if e>=len(lst):
                        break
                else:
                    break
            drop=float(lst[s])-float(lst[e])
            year1=s
            year2=e
            for num in range(s,len(lst)-1):
                if lst[num] != "":
                    v1 = float(lst[num])
                    for num1 in range(num+1, len(lst)):
                        if lst[num1] != "":
                            v2=float(lst[num1])
                            diffence=v1-v2
                            if drop < diffence:
                                drop = diffence
                                year1=num
                                year2=num1
            country = Range(i,year1+1960,year2+1960,float(lst[year1]),float(lst[year2]))
            list.append(country)
    list = sorted(list,key=difference,reverse=False)
    return list

def chcountry(lst):
    """
    This function checks the country contains at least 2 years of life expectancy or not.
    :param lst: list of life expectancy data for a country
    :return:
    """
    count=0
    for num in lst:
        if num != "":
            count += 1
            if count >= 2:
                return True
    return False

def main():
    """
    This function will output the worst ten life expectancy drops.
    :return: NoneType
    """
    dabase=read_data("worldbank_life_expectancy")
    data=filter_region(dabase, "all")
    data=sorted_drop_data(data)
    print("Worst life expectancy drops: 1960 to 2015")
    num=1
    for i in range(0,10):
        print(str(num)+":",data[i].country,"from",str(data[i].year1),"("+str(data[i].value1)+")","to",str(data[i].year2),
              "("+str(data[i].value2)+"):",str(data[i].value2-data[i].value1))
        num+=1
main()