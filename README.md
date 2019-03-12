# pyspark-dataframe-searcher
Taiwo pyspark dataframe feature extraction problem

**Problem description**

This problem is taken from a question I posted on [StackOverflow](https://stackoverflow.com/questions/55031126/search-the-rest-columns-of-pyspark-dataframe-for-values-in-column1). It involves a search in two dimensional array space which is essentially a *two-dimensional pattern matching problem(Ref. [1])*.

For example: 

Suppose there is a pyspark dataframe of the form:
 
    id  col1  col2 col3 col4
    ------------------------
    as1  4    10    4    6
    as2  6    3     6    1
    as3  6    0     2    1
    as4  8    8     6    1
    as5  9    6     6    9

The objective is to search the ***col 2-4*** of the pyspark dataframe for values in ***col1*** and to return the ***(id row name, column name)***. The solution is described as follows:

    In col1, 4 is found in (as1, col3)
    In col1, 6 is found in (as2,col3),(as1,col4),(as4, col3) (as5,col3)
    In col1, 8 is found in (as4,col2)
    In col1, 9 is found in (as5,col4)

*Hint:* Assume that col1 will be a set {4,6,8,9} i.e. unique

**Solution**

An attempt is made to solve the above problem statement using pyspark.

**To run, use:**
   
     spark2-submit --py-files job_searchdataframe.zip main.py --search >> output_`date +\%m\%d\%y\%T`.txt
      
**Requirements**

 [pyspark2](https://pypi.org/project/pyspark/)
 
 **Installation**
 
    pip install pyspark
  
**Reference**

1. J. Alwidian, H. Abu-Mansour and M. Ali, "Efficient algorithm for two dimensional pattern matching problem 
   (non-square pattern)," 2012 International Conference on Information Technology and e-Services, Sousse, 2012, pp. 1-8.
   doi: 10.1109/ICITeS.2012.6216622


**You want to be a contributor?** 
1. Fork repository

     and/or

2. Connect and chat me on [LinkedIn](https://www.linkedin.com/in/taiwo-o-adetiloye-ph-d-505a8023/).
