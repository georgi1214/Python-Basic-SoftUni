pens = int(input())
markers = int(input())
clean = int(input())
dis = int(input())

pricePens = pens * 5.8
priceMarkers = markers * 7.2
priceClean = clean * 1.2

totalPrice = pricePens + priceMarkers + priceClean

finalPrice = totalPrice - (dis * (totalPrice / 100))

print(finalPrice)


