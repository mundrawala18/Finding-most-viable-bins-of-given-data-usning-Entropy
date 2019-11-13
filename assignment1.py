import pandas as pd
from math import log,log2,ceil
dataFile='data.csv'
max_value=0
overall_entropy=0 
total=0

#defining methods==================================
def loadData(dataFile):
	"""Loading data from dataset and calculating totalsales (qty*price)"""
	global max_value
	data=pd.read_csv(dataFile,encoding = "ISO-8859-1",low_memory=False)
	frame={'Country':data['Country'],'Quantity':data['Quantity'],'UnitPrice':data['UnitPrice']}
	result = pd.DataFrame(frame)
	result["TotalSales"]=result['Quantity']*result['UnitPrice']
	max_value = ceil(result['TotalSales'].max()*10)
	return result


def binning(data,size):
	"""Creating bin as per user given size"""
	global max_value
	bins=range(0,max_value,size)
	data['TotalSales'] = pd.cut(data['TotalSales'], bins) 
	del bins
	binList=data['TotalSales'].unique()
	return data,binList

def fetchCountry(data):
	"""Extracting countries and its frequency"""
	cntry=data['Country'].unique()
	country={}
	for i in cntry:
		cdata=data[data.Country==i]
		country[i]=cdata['TotalSales'].count()
	return country

def binCount(data,Country=None):
	"""Finding bins Frequency"""
	binCnt={}
	if(Country!=None):
		data=data[data.Country==Country]
	binCnt['count']=data['TotalSales'].count()
	bins=data['TotalSales'].unique()
	for i in bins:
		tData=data[data.TotalSales==i]
		binCnt[str(i)]=tData['TotalSales'].count()
	return binCnt

def getEntropy(data):
	"""
	Finding Entropy using this formula
		Entropy=-∑p(xi) log P(xi)
			where xi = m/total
	"""
	entropy=0
	y=[]
	count=data['count']
	del data['count']
	for k in data:
		x=(data[k]/count)
		entropy += -(x * log2(x if x>0 else 1))
	return count,entropy

def getCountryWiseEntropy(data,CountryList):
	"""
	Finding Countries Entropy 
	"""
	CountryEntropy={}
	for i in CountryList:
		CountryEntropy[i] = getEntropy(binCount(data,i))
	return CountryEntropy


def getNetEntropy(c_entropy):
	"""
	Finding info=D1/D.entropy(D1)+...+Dn/n.entropy(Dn)
	"""
	global total
	n_Entropy=0
	for key,value in c_entropy.items():
		n_Entropy+=(value[0]/total)*(value[1])
	return n_Entropy

def getGain(o_entropy,n_entropy):
	"""
	Finding Gain=Entropy(D)-Info(D)
	"""
	return o_entropy-n_entropy

#=================================
output=[]
Lable=['Case','Bin Size','Overall Entropy','Info','Gain']
case=0
op="y"
while 1:
	case+=1
	binSize=int(input("Enter bin size:-"))
	#calling methods
	raw_data=loadData(dataFile)
	Country=fetchCountry(raw_data)
	processed_data,binlist=binning(raw_data,binSize)
	bins_count=binCount(processed_data)
	total,overall_entropy = getEntropy(bins_count)
	CountryEntropy = getCountryWiseEntropy(raw_data,Country)
	netEntropy=getNetEntropy(CountryEntropy)
	gain=getGain(overall_entropy,netEntropy)

	#printing result 
	print("Overall Entropy - ",overall_entropy)
	print("Net Entropy (info)- ",netEntropy)
	print("Gain - ",gain)
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	output.append((case,binSize,overall_entropy,netEntropy,gain))
	op=input("To finish press 'N'-")
	if(op=='N' or op=='n'):
		df = pd.DataFrame.from_records(output,columns=Lable)
		print("printing all the Cases and saveing as csv file")
		print("\n",df)
		df.to_csv("output.csv",sep="|")
		break


