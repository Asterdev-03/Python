#Data_types

#Numbers
num = 20
print(id(num))                      #are immutable data type
complex_no = 10+5j
print(type(complex_no))             #data type


#Strings
text = "python programming"
print(text)
print(len(text))
print(text.capitalize())
print(text.upper())
print(text.replace("python","java"))
print(text.count("p"))


#Lists
teachers = ['John','Anu','Nandhana','Hari']
print(teachers[1])
print(teachers[-1])                 #prints last value in the list
print(teachers[0:3])                #prints form [0] to [2]
teachers[2]= 'Priya'
print(teachers)

#print(teachers.count(5))
teachers.append('Vinu')
teachers.insert(1,'Maya')
teachers.remove('Hari')
teachers.pop(0)
teachers.sort()
print(teachers)
#print(teachers.extend())


#Tuple
emp_details = ('John','E041',2019)
#emp_details[0] = 'Maya'            ...Error since tuple is immutable
print(emp_details)


#Dictionary
staff_details = {'name':'Hari','emp_no':'E045','year':2018}
print(staff_details['name'])
print(staff_details.get('emp_no'))
staff_details['emp_no'] = 'E049'
staff_details['last_company'] = 'Infosys'
del staff_details['year']
print(staff_details)



