# pyspark-dataframe-searcher
Taiwo's pyspark dataframe feature extraction problem.

**Problem description**

This problem can be found on [StackOverflow](https://stackoverflow.com/questions/55031126/search-the-rest-columns-of-pyspark-dataframe-for-values-in-column1). It involves a search vis-a-vis pattern matching in two dimensional array space; and, it can be regarded as a *two-dimensional pattern matching problem*(Ref. [[1](https://ieeexplore.ieee.org/document/6216622)]).

*For example:* 

Given a pyspark dataframe of the form:
 
    id  col1  col2 col3 col4
    ------------------------
    as1  4    10    4    6
    as2  6    3     6    1
    as3  6    0     2    1
    as4  8    8     6    1
    as5  9    6     6    9

The objective is to search the _*col 2-4*_ of the pyspark dataframe for values in _*col1*_ and to return the _*id row-name(s), column-name(s)*_. The feasible solutions are the following:

    In col1, 4 is found in (as1, col3)
    In col1, 6 is found in (as2,col3),(as1,col4),(as4, col3) (as5,col3)
    In col1, 8 is found in (as4,col2)
    In col1, 9 is found in (as5,col4)

*Hint:* Assume that col1 is a set: {4,6,8,9} i.e. distinct

**Solution**

An attempt is made to solve the above problem statement using pyspark.

  *Window users, run the following commands:*
     
    git clone https://github.com/taiwotman/pyspark-dataframe-searcher.git
    
    spark2-submit --py-files job_searchdataframe.zip main.py --search >> output_`date +\%m\%d\%y\%T`.txt
    
  *Unix user, run the bash script: [run.ksh](https://github.com/taiwotman/pyspark-dataframe-searcher/blob/master/run.ksh)*.
 
    chmod 777 run.ksh
    
    ./run.ksh
 
     
**Output**
 
   _Refer to the [output](https://github.com/taiwotman/pyspark-dataframe-searcher/blob/master/output_031219.txt) text file_
      
**Requirements**

   [pyspark>=2.4.0](https://pypi.org/project/pyspark/)
 
**Installation**
 
    pip install pyspark

**To do:**

1. Improve the runtime(i.e. End-time minus Start-time)
2. Improve the search to obtain the rows and columns(i.e. x,y coordinates) of feasible solutions.

**Reference**

1. J. Alwidian, H. Abu-Mansour and M. Ali, "Efficient algorithm for two dimensional pattern matching problem 
   (non-square pattern)," 2012 International Conference on Information Technology and e-Services, Sousse, 2012, pp. 1-8.
   doi: 10.1109/ICITeS.2012.6216622


**You want to be a contributor?** 
1. Fork repository

     and/or

2. Connect and chat me on [LinkedIn](https://www.linkedin.com/in/taiwo-o-adetiloye-ph-d-505a8023/).
