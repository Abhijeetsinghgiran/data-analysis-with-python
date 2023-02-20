
 #  abhijeet singh

import csv
csv_filepath='C:\\Users\Abhi\Downloads\stack-overflow-developer-survey-2020\survey_results_public.csv'
lst=[]

with open(csv_filepath, 'r') as file:
    my_reader = csv.reader(file, delimiter=',')
    for row in my_reader:
        lst.append(list(row))
        
import collections
dct=collections.defaultdict(list)
a=''
for b in range(len(lst)):
    try:
        for c in range(len(lst)):
            if c==0:
                a=lst[c][b]
            else:
                dct[a].append(lst[c][b])
    except:
        break

count=0
for i in dct['Respondent']:
    count=count+1
print(f"Total number of people {count}")
    

arr=[]
for i in range(len(dct['NEWSOSites'])):
    if "Stack Overflow" in dct['NEWSOSites'][i]:
        arr.append(i)

brr=[]
for i in arr:
    if str(dct['Age'][i])!='NA':
        brr.append(dct['Age'][i])
    else:
        pass

young_age=[]
for i in brr:
    if len(young_age)==0:
        young_age.append(i)
    elif i<young_age[0]:
        young_age[0]=i
        
print(f"Youngest person' {young_age[0]}") 


set(dct['JobSat'])
crr=[]
very_satisfied=0
for i in dct['JobSat']:
    if "Very satisfied" in i:
        very_satisfied=very_satisfied+1
        crr.append(i)

drr=[]
Slightly_satisfied=0
for i in dct['JobSat']:
    if "Slightly satisfied" in i:
        Slightly_satisfied=Slightly_satisfied+1
        drr.append(i)
        
print(f"number of people are satisfied with job {very_satisfied+Slightly_satisfied}")


empty_list=[]
for i in dct['LanguageWorkedWith']:
    empty_list.append(i.split(";"))

empty_list1=[]
for i in range(len(empty_list)):
    for j in range(len(empty_list[i])):
        empty_list1.append(empty_list[i][j])

Set=list(set(empty_list1))
occurence={}
for i in Set:
    occurence[empty_list1.count(i)]=i

list_of_occurences=list(occurence.keys())
final_keys=[]
for i in range(0,5):
    Max=0
    for j in list_of_occurences:
        if j>Max:
            Max=j
    list_of_occurences.remove(Max)
    final_keys.append(Max)
    
print("Top 5 used languages:")
for i in final_keys:
    print(occurence[i])


empty_list2=[] 
for i in dct['DevType']:
    empty_list2.append(i.split(";"))
empty_list3=[]
for i in range(len(empty_list2)):
    for j in empty_list2[i]:
        if "Developer" in j:
            empty_list3.append(j)

final_list=[]
for i in range(len(empty_list2)):
    if set(empty_list2[i])<=set(empty_list3):
        final_list.append(empty_list2[i])
        
total_dev=0
for i in final_list:
    total_dev=total_dev+1
    
print(f"number of peoples work as a developer only is {total_dev}")


set_of_OS=list(set(dct['OpSys']))
list_of_OS=list(dct['OpSys'])
occurence2={}
for i in set_of_OS:
    occurence2[list_of_OS.count(i)]=i

Max2=0
for i in occurence2.keys():
    if i>Max2:
        Max2=i

print(f"Operating System is used by most of the people is {occurence2[Max2]}") 

set_of_YC=list(set(dct['YearsCode']))
num_of_YC=[]
str_of_YC=[]
for i in set_of_YC:
    if i.isdigit()==True:
        num_of_YC.append(i)
    else:
        str_of_YC.append(i)

for i in range(0, len(num_of_YC)):
    num_of_YC[i] = int(num_of_YC[i])

Max3=0
for i in range(len(num_of_YC)):
    if num_of_YC[i]>Max3:
        Max3=num_of_YC[i]

a="More than 50 years"
if a in str_of_YC:
    print(f"The maximum total years of code done by any person is {a.lower()}") 
else:
    print(f"The maximum total years of code done by any person is {Max3}")





















































































































