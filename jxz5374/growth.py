"""
file:growth.py
author: Joey Zhen
created: 12/09/2017
"""
from utils import *
import math

from jxz5374.utils import CountryValue, read_data, filter_income, filter_region


def expectancy(country):
    """
    This function return the key for sorting the life expectancy growth of countries from largest number and smallest number
    :param country:
    :return:
    """
    return country.value

def sorted_growth_data(data, year1, year2):
    """
    This function returns data for the specified years is extracted and the growth values sorted, and the top ten
and bottom ten life expectancy growth values over the given range of years are printed.
    :param data:
    :param year1:
    :param year2:
    :return:
    """
    lst=[]
    index1=year1-1960
    index2=year2-1960
    country1=data[0]
    for i in country1:
        if country1[i].expectancy[index1] != "" and country1[i].expectancy[index2] != "":
            difference= math.fabs(float(country1[i].expectancy[index1]) - float(country1[i].expectancy[index2]))
            country=CountryValue(i,float(difference))
            lst.append(country)
    lst=sorted(lst, key=expectancy, reverse=True)
    return lst

def main():
    """
    This main function returns a list of CountryValue structures, sorted in descending order (highest to lowest).
The value stored in this structure is the absolute growth in life expectancy for the country between the starting year
and the ending year.
    :return:
    """
    dabase = read_data("worldbank_life_expectancy")
    while True:
        year1=int(input("Enter starting year of interest: "))
        if year1>2015 or year1<1960:
            print("Invalid year")
        elif year1==-1:
            break
        else:
            year2=int(input("Enter ending year of interest: "))
            if year2>2015 or year2<1960 or year2<=year1:
                print("Invalid years")
            elif year2==-1:
                break
            else:
                region1=str(input("Enter region: "))
                data=filter_region(dabase, region1)
                if data == None:
                    pass
                else:
                    region2=str(input("Enter income category: "))
                    data=filter_income(data,region2)
                    if data == None:
                        pass
                    else:
                        data=sorted_growth_data(data, year1, year2)
                        if len(data)<10:
                            num=1
                            print("\nTop 10 Life Expectancy Growth: "+str(year1)+" to "+str(year2))
                            for i in data:
                                print(str(num)+":",i.country,str(i.value))
                                num=num+1
                            num=len(data)
                            print("\nBottom 10 Life Expectancy Growth: " + str(year1)+" to "+str(year2))
                            for i in range(len(data)-1,-1,-1):
                                print(str(num) + ":", data[i].country,str(data[i].value))
                                num=num-1
                        else:
                            num=1
                            print("\nTop 10 Life Expectancy Growth: "+str(year1)+"to"+str(year2))
                            for i in range(0,10):
                                print(str(num)+":",data[i].country,str(data[i].value))
                                num=num+1
                            num=len(data)
                            print("\nBottom 10 Life Expectancy Growth: " + str(year1) + " to " + str(year2))
                            for i in range(len(data)-1,len(data)-10-1,-1):
                                print(str(num) + ":", data[i].country, str(data[i].value))
                                num=num-1
            print()
main()