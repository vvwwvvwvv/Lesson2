

students =[{'school_class': '4A', 'scores': [3,4,4,5,2]},
           {'school_class': '4Б', 'scores': [2,4,3,4,5]},
           {'school_class': '4В', 'scores': [5,3,3,5,2]},
           {'school_class': '4Г', 'scores': [3,3,5,5,2]}]
value = []



for i in students:
    result = (sum(i['scores'])/len(i['scores']))
    value.append(result)
    print(f'Средний балл по классу равен: ',sum(value)/len(i))


mean_value = sum(value) / len(students)
print('Средний балл по школе равен: {:.2}'.format(mean_value))
