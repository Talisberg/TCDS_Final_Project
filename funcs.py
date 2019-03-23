import numpy as np

Weekdays = {0: '1', 1: '2', 2: '3', 3: '4', 4: '5', 5: '6', 6: '7'}
HGroups = {'16-23': list(range(16, 24)), '0-7': list(range(0, 8)), '8-15': list(range(8, 16))}


def get_int_quantiles(col, n=4):
    """the function recieves a pandas series and no. of cuttofs and returns the np array of cutoff values, default quantiles = 4"""

    quant = col.quantile(q=[x / n for x in range(n + 1)])

    quant = [int(x) for x in quant.values]

    quant_dict = {}
    for i in  range(len(quant)-1):
        quant_dict[range(quant[i],quant[i+1])] = '{0} - {1}'.format(quant[i],quant[i+1])
     
       
    return quant_dict
    
def quantile_grouping(val,quantiles):
    """the function groups values by quantile cutoffs"""

    if np.isnan(val):
        return "OTHER"
    
    for key in quantiles.keys():
        if val in key :
            return quantiles[key]
    
    return "OTHER"



def get_dec_quantiles(col, n=4):
    """the function recieves a pandas series and no. of cuttofs and returns the np array of cutoff values, default quantiles = 4"""

    quant = col.quantile(q=[x / n for x in range(n + 1)])
    quant = [x for x in quant.values]
    
    quant_dict = {}
    for i in range(len(quant)-1):
        quant_dict[range((10*quant[i]).astype(int), (10*quant[i+1]).astype(int))] = '{0}-{1}'.format(quant[i],quant[i+1])
      
    return quant_dict

def quantile_dec_grouping(val,quantiles):
    """the function groups values by quantile cutoffs"""

    if np.isnan(val):
        return "OTHER"
    
    for key in quantiles.keys():
        if 10*val in key :
            return quantiles[key]
    
    return "OTHER"


def hourgroup(a):
    """divides the day to 3 shifts of 8 hours"""
    for key, values in HGroups.items():
        if a in values:
            return key


def stategroup(val, better, worst):
    """recieves a State and classifies the variable according to the state performance """

    if val not in (better + worst):
        return np.nan
    else:
        return val
    

def osv_normalizer(x):
    """Reformat OSV across all ssps"""

    try:
        if np.isnan(x):
            return x
    except:
        pass

    if len(x) > 12 or len(x) < 1:
        return "OTHER"

    elif 1< len(x) < 3:
        return x

    norm = x
    Flag = True
    while Flag:
        if (norm[-1] == '0') and (not norm[-2].isnumeric()):
            norm = norm[:-2]
        else:
            Flag = False
    return norm



def device_screen_size(diag = -1, phone = -1):
    """Map diagonal to device class"""
    PhoneDict = { range(0,45):'0 - 4.5', range(45,55):'4.5 - 5.5', range(55,70):'5.5 - 7.0', range(70,100):'7+'}
    
    
    if diag != -1:
        for key,val in PhoneDict.items():
            if 10*diag in key:
                return val
        return np.nan


        
    
    
        
    
