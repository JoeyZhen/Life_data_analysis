"""
file: utils.py
author: Joey Zhen
created: 12/09/2017
"""



from rit_lib import *

CountryValue = struct_type("CountryValue", (str, "country"), (float, "value"))


Range = struct_type("Range", (str, "country"), (int, "year1"), (int, "year2"),(float, "value1"), (float, "value2"))


Country = struct_type("Country", (str, "name"), (str, "code"), (list, "expectancy"),(str, "region"), (str, "income"))


def read_data(filename):
    """
    This function read the data from two files which named worldbank life expectancy metadata.txt and worldbank life expectancy data.txt
    Also, I create one large dictory called dict1 and it contains four differents dictories named code, dict1, region and income.
    :param
    :return:
    """
    Countries = dict() #create a dictionary contains all the information from the two files
    data = open(filename+"_data.txt")
    data.readline()
    for line in data:
        info = line.split(",")
        name = info[0]
        code = info[1]
        list = []
        for i in range(2, len(info)-1):
            list.append(info[i])
        country1 = Country(name, code, list, "", "")
        Countries[name] = country1
    data.close()
    metadata = open(filename + "_metadata.txt")
    metadata.readline()
    for line in metadata:
        info = line.split(",")
        for c in Countries.values():
            if c.code == info[0]:
                c.region = info[1]
                c.income = info[2]
    metadata.close()

    Regions = dict() #create a dictionary contains regions
    for k in Countries:
        key = str(Countries[k].region)
        if key != "":
            if (key in Regions) == False:
                Regions[key] = []
                Regions[key].append(k)
            else:
                Regions[key].append(k)

    Income_cate = dict() #create a dictionary contains income categories
    for k in Countries:
        key = Countries[k].income
        if key != "":
            if (key in Income_cate) == False:
                Income_cate[key] = []
                Income_cate[key].append(k)
            else:
                Income_cate[key].append(k)

    Codes = dict() #create a dictionary contains countries's name
    for k in Countries:
        key = Countries[k].code
        Codes[key] = k

    all_data = (Countries, Regions, Income_cate, Codes)
    return all_data


def filter_region(data, region):
    """
    This function returns data that has been filtered to only retain data corresponding to the specified region
    :param data:
    :param region:
    :return:
    """
    if data == None:
        return 0
    else:
        country = data[0]
        region = data[1]
        change={}
        if region == "all":
            for i in country:
                if str(country[i].region) != "":
                    change[i] = country[i]
            data = (change, data[1], data[2], data[3])
            return data
        else:
            if (region in region) == True:
                for i in region[region]:
                    if (i in country) == True:
                        change[i] = country[i]
                data = (change, data[1], data[2], data[3])
                return data
            else:
                print("invalid region.")



def filter_income(data, income):
    """
    This function returns g data that has been filtered to only retain data corresponding to the specified income category.
    :param data:
    :param cate:
    :return:
    """
    if data == None:
        return 0
    else:
        country = data[0]
        income = data[2]
        change = {}
        if income == "all":
            for i in country:
                a = str(country[i].region)
                if a != "":
                    change[i] = country[i]
            data = (change, data[1], data[2], data[3])
            return data
        else:
            if (income in income) == True:
                for i in income[income]:
                    if (i in country) == True:
                        change[i] = country[i]
                data = (change, data[1], data[2], data[3])
                return data
            else:
                print("invalid income category.")


def main():
    """
    This main function will output all of informations which users want to view with the working of dictories.
    Like output the total number of entities in the data file, the total number of countries in the data file, a summary
     of the different regions and the number of countries included in each region.
      Output a summary of the different income categories and the number of countries
    included in each category.
    """
    data = read_data("worldbank_life_expectancy")
    print("Total number of entities:",str(len(data[0])))
    num_countries = 0
    for i in data[1]:
       for n in  data[1][i]:
           num_countries += 1
    print("Number of countries/territories",str(num_countries),"\n")
    print("Regions and their country count:")
    for i in data[1]:
        count = 0
        for n in data[1][i]:
            count += 1
        print(i+": "+str(count))
    print("\nIncome categories and their country count:")
    for i in data[2]:
        count = 0
        for n in data[2][i]:
            count += 1
        print(i+": "+str(count))
    region = str(input("\nEnter region name: "))
    fdata = filter_region(data, region)
    if fdata is not None:
        print("Countries in the '"+region+"' region:")
        fcountries = fdata[0]
        for i in fcountries.values():
            print(i.name,"("+i.code+")")
    cate = str(input("\nEnter income category: "))
    fdata = filter_income(data, cate)
    if fdata is not None:
        print("Countries in the '"+cate+"' income category:")
        fcountries = fdata[0]
        for i in fcountries.values():
            print(i.name,"("+i.code+")")
    Countries = data[0]
    Codes = data[3]
    while True:
        name_or_code = str(input("\nEnter name of country or country code(Enter to quit): "))
        if name_or_code == "":
            break
        if (name_or_code in Countries) == True:
            print("Data for", name_or_code+":")
            list = Countries[name_or_code].expectancy
            n = 1960
            for i in list:
                if i != "":
                    print("Year:",str(n),"Life expectancy:",i)
                n += 1
        elif (name_or_code in Codes) == True:
            print("Data for", name_or_code+":")
            name_of_code = Codes[name_or_code]
            list = Countries[name_of_code].expectancy
            years= 1960
            for i in list:
                if i != "":
                    print("Year:",str(years),"Life expectancy:",i)
                years=years+1
        else:
            print("'"+name_or_code+"' is not a valid country name or code")
main()
