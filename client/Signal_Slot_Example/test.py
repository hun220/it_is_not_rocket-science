data = [['28544', '-0.09', '0.02', '1.01', '5.97'], ['28545', '-0.09', '0.02', '1.01', '6.22'], ['28546', '-0.09', '0.01', '1.01', '6.73'], ['28547', '-0.09', '0.02', '1.01', '6.47'], ['28548', '-0.09', '0.02', '1.01', '6.56']]
temp = []

def get_acceldata():
    for sor in data:
        sor[1] = float(sor[1])
        print(sor[1])
        temp.append(sor[1])      
    return str(max(temp))
