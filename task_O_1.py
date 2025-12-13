def E_meh(**data):
    E=data['m']*9.8*data['h']+data['m']*data['v']**2/2
    print(E)
arg = {'m': 30, 'h': 45, 'v': 22}
E_meh(**arg)    
