def computepay(h,r):
    if h > 40:

        extra = h-40
        extrapay = extra*(r*1.5)

        regularhrs = h-extra

        total = (regularhrs*r) + extrapay
        return total
    else:
        total = h*r
        return total
    
    

hrs = input("What is your hours worked? : ")
rate = input("What is your rate per hour? :")

h= float(hrs)
r= float(rate)  

p = computepay(h,r)

print("Pay ", p)
