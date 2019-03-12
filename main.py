'''
Created on 3/12/2019
Author: Taiwo Adetiloye   
Email: taiwo.adetiloye@gmail.com
Website: taiwotman.github.io
'''

from job_searchdataframe.search import SearchCol1ValuesInRestCols

import argparse



def main():
    parser = argparse.ArgumentParser(description='Search the rest columns of pyspark dataframe for values in column1')

    parser.add_argument("-s", "--search", action='store_true',
                        help="search the rest columns of pyspark dataframe for values in column1")

    args = parser.parse_args()

    if args.search:
        b = SearchCol1ValuesInRestCols()
        b.template_method()

    else:
        print("Specify parameter --search or -s to perform search respectively")


if __name__ == "__main__":
    main()

