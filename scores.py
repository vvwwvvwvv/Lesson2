

students =[{'school_class': '4A', 'scores': [3,4,4,5,5]},
           {'school_class': '4Б', 'scores': [3,4,3,4,5]},
           {'school_class': '4В', 'scores': [5,3,3,5,4]},
           {'school_class': '4Г', 'scores': [4,3,5,5,4]}]
value = []



for i in students:
    result = (sum(i['scores'])/len(i['scores']))
    value.append(result)
    print(f'Средний балл по классу равен:',result)

print()

mean_value = sum(value) / len(students)
print('Средний балл по школе равен: {:.2}'.format(mean_value))
