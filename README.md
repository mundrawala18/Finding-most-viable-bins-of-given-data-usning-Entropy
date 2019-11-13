# Finding-most-viable-bins-of-given-data-usning-Entropy
This is a data mining assignment. Program is written in python 3 language. Program find entropy, info, and gain based on user-defined bin size

  Required libraries 
  -
    Pandas
        -to install refer this link https://pandas.pydata.org/pandas-docs/stable/install.html
    math
      -built-in library
      
  Required data
  -
    E-Commerce dataset from kaggle.com
    link- https://www.kaggle.com/carrie1/ecommerce-data
   
  Code discription
  -
    the main motto of this code is to find entropy, info, and gain. In this code, we load data set using the pandas library. Create a bin on 'TotalSales' (Quantity * UnitPrice) column which is added at loading time. After that Overall entropy is calculated using this formula:-
            Entropy(D)=-∑p(xi) log P(xi)
     like this Country-wise entropy is calculated. After that net entropy (Info) is calculated using this formula:- Info(D)=|D1|/|D|Entropy(D1)+...+|Dn|/|D|Entropy(Dn)
    then gain is calculated using this formula:- gain(D new)=(E init) - (E new)
