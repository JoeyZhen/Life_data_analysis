"""
file:ranking.py
author: Joey Zhen
created: 12/09/2017
"""
from utils import *

from jxz5374.utils import CountryValue, read_data, filter_region, filter_income


def expectancy(country):
    """
     This function returns the key for sorting the life expectancy of countries in a typically year.
    :param country:
    :return:
    """
    return country.value

def sorted_ranking_data(data,year):
    """
     This function returns a list of CountryValue structures, sorted in descending order (highest to lowest).
    :param data:
    :param year:
    :return:
    """
    lst=[]
    index=year-1960
    country1=data[0]
    for i in country1:
        if country1[i].expectancy[index] != "":
            country=CountryValue(i,float(country1[i].expectancy[index]))
            lst.append(country)
    lst=sorted(lst,key=expectancy,reverse=True)
    return lst

def main():
    """
    This main function run the function above and return data which contains data for the specified year are included in the sorted
list.
    :return:
    """
    dabase= read_data("worldbank_life_expectancy")
    while True:
        years=int(input("Enter year of interest: "))
        if years>2015 or years<1960:
            print("inalid years")
        elif years==-1:
            break
        else:
            region1=str(input("Enter region: "))
            data=filter_region(dabase,region1)
            if data == None:
                pass
            else:
                region2=str(input("Enter income category: "))
                data=filter_income(data,region2)
                if data == None:
                    pass
                else:
                    data=sorted_ranking_data(data,years)
                    if len(data)<11-1:
                        num=1
                        print("\nTop 10 Life Expectancy for",str(years))
                        for i in data:
                            print(str(num)+":",i.country,str(i.value))
                            num+=1
                        num=len(data)
                        print("\nBottom 10 Life Expectancy for",str(years))
                        for i in range(len(data)-1,-1,-1):
                            print(str(num)+":",data[i].country,str(data[i].value))
                            num=num-1
                    else:
                        num=1
                        print("\nTop 10 Life Expectancy for",str(years))
                        for i in range(0,10):
                            print(str(num)+":",data[i].country,str(data[i].value))
                            num=num+1
                        num=len(data)
                        print("\nBottom 10 Life Expectancy for", str(years))
                        for i in range(len(data) - 1,len(data)-11,-1):
                            print(str(num)+":",data[i].country, str(data[i].value))
                            num=num-1
        print()
main()