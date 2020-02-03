# from util.setup import Setup
from selenium import webdriver
import pytest
from selenium.webdriver.support.select import Select

from actions.helper import Helper



@pytest.fixture(scope="session")
def open_browser():
    """
     Validate that site opens or not.
    :return: driver
    """
    driver = webdriver.Chrome("/Users/deepanshu.ahuja/Documents/chromedriver")
    driver.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
    return driver





def test_ranking(open_browser,request):
    """
    Validate that top 250 movies are correctly sorted with their ranks
    
    Description :- Preparing the golden data
    
    parameters: 
        open_browser = driver
        request = For caching the golden_data
        
    """
    elements = open_browser.find_element_by_xpath("//tbody[@class='lister-list']")

    superlist = elements.text.split("\n")
    flag=0
    for i in range(len(superlist)):
        tmp=int(superlist[i].split(".")[0])
        if (tmp != i + 1):
            flag=1
            break
    dict1=Helper().super_data(superlist)
    request.config.cache.set("golden_data", dict1)
    Helper().write_into_file("target/ranking.txt",superlist)
    assert (flag==0),"The list is not sorted with the ranking type"




def test_year(open_browser,request):
    
    
    """
    Validate that top 250 movies are correctly sorted with the release date.
    
    Description: In this we are validating that movies are sorted with the descending order and
                 also comparing with the golden data that movie name and imdb rating would be correct.
    
    parameters:- 
    
    open_browser = driver
    request = For caching the golden_data
    
    """
    dict1 = request.config.cache.get("golden_data", None)
    dropdown = Select(open_browser.find_element_by_id("lister-sort-by-options"))

    dropdown.select_by_index(2)
    elements = open_browser.find_element_by_xpath("//tbody[@class='lister-list']")

    superlist = elements.text.split("\n")
    flag = 0
    for i in range(len(superlist)):

        if (i != len(superlist) - 1):
            if (int(superlist[i].split("(")[1].split(")")[0]) >= int(superlist[i + 1].split("(")[1].split(")")[0])):
                if (dict1[str(superlist[i].split(".")[0])][0] == superlist[i].split(".")[1].split(" (")[0].strip() and
                        dict1[str(superlist[i].split(".")[0])][2] == float(superlist[i].split("(")[1].split(")")[1])):
                    continue
            else:
                flag = 1
                break
        else:
            if (int(superlist[i - 1].split("(")[1].split(")")[0]) >= int(superlist[i].split("(")[1].split(")")[0])):
                if (dict1[str(superlist[i].split(".")[0])][0] == superlist[i].split(".")[1].split(" (")[0].strip() and
                        dict1[str(superlist[0].split(".")[0])][2] == float(superlist[i].split("(")[1].split(")")[1])):
                    continue
            else:
                flag = 1
                break
    Helper().write_into_file("target/year.txt",superlist)
    assert (flag==0),"Top 250 movies are not correctly sorted with the release date"


def test_imdb_rating(open_browser,request):
    
    """
    Validate that top 250 movies are correctly sorted with the imdb ratings.
    
    Description: In this we are validating that movies are sorted with the descending order and
                 also comparing with the golden data that movie name and release date would be correct.
    
    parameters:- 
    
    open_browser = driver
    request = For caching the golden_data
    """
    
    
    dict1 = request.config.cache.get("golden_data", None)
    dropdown = Select(open_browser.find_element_by_id("lister-sort-by-options"))

    dropdown.select_by_index(1)

    elements = open_browser.find_element_by_xpath("//tbody[@class='lister-list']")

    superlist = elements.text.split("\n")

    flag = 0
    for i in range(len(superlist)):

        if (i != len(superlist) - 1):
            if (float(superlist[i].split("(")[1].split(")")[1]) >= float(superlist[i + 1].split("(")[1].split(")")[1])):
                if (dict1[str(superlist[0].split(".")[0])][0] == superlist[i].split(".")[1].split(" (")[0].strip() and
                        dict1[str(superlist[0].split(".")[0])][1] == int(superlist[i].split("(")[1].split(")")[0])):
                    continue
            else:
                flag = 1
                break
        else:
            if (float(superlist[i - 1].split("(")[1].split(")")[1]) >= float(superlist[i].split("(")[1].split(")")[1])):
                if (dict1[str(superlist[0].split(".")[0])][0] == superlist[i].split(".")[1].split(" (")[0].strip() and
                        dict1[str(superlist[0].split(".")[0])][1] == int(superlist[i].split("(")[1].split(")")[0])):
                    continue
            else:
                flag = 1
                break
    Helper().write_into_file("target/imdbratings.txt",superlist)
    assert (flag==0),"Top 250 movies are not correctly sorted with the imdb ratings"
