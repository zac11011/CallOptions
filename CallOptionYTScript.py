import numpy as np
# first entry is the market price
strikePrice = np.array([0,65,70,75,80,85,90,95,100,105,110])
premium = np.array([89.37,24.53,20.65,16.1,12.36,8.8,6,3.8,2.27,1.31,0.76])
marketPrice = 89.37
breakEven = strikePrice+premium
breakEvenMovePct = (breakEven-marketPrice)*100/marketPrice
breakEvenMovePct = np.round(breakEvenMovePct,2)
elems = 1000
futurePrice = np.linspace(60,125,elems)
priceChange = (futurePrice-marketPrice)/marketPrice

ind = np.array(np.zeros(elems),dtype=int)
retrunsPctArr = np.zeros((elems,strikePrice.size))
firstEntry = np.array(np.zeros(strikePrice.size),dtype=float)
returnFactor = np.round(marketPrice/premium,2)

for i in range(futurePrice.size):
    returns = np.maximum(futurePrice[i]-strikePrice,0)-premium
    retrunsPct = returns/premium
    retrunsPctArr[i,:] = (returns/premium)*100
    ind[i] = np.floor(np.argmax(retrunsPct))
    if firstEntry[ind[i]] == 0:
        firstEntry[ind[i]] = futurePrice[i]

firstEntry = np.round((firstEntry-marketPrice)*100/marketPrice,2)

print(firstEntry)
print(breakEvenMovePct)
print(returnFactor)