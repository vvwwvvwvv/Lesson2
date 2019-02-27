import ephem

mars = ephem.Mars('1970')
print(ephem.constellation(mars))

print(ephem.next_full_moon('2016/09/23'))
