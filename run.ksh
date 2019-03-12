git clone https://github.com/taiwotman/pyspark-dataframe-searcher.git
spark2-submit --py-files job_searchdataframe.zip main.py --search >> output_`date +\%m\%d\%y\%T`.txt
