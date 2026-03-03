name=input("Enter name=")
roll_no=int(input("Roll no="))
atmost=int(input("max marks="))
maths=float(input("Enter marks of maths:"))
python=float(input("Enter marks of python:"))
ai=float(input("Enter marks of ai:"))
english=float(input("Enter marks of english:"))
physics=float(input("Enter marks of physics:"))
subject={"maths":maths,"python":python,"ai":ai,"english":english,"physics":physics}
total=python+ai+english+physics+maths
x=total*100/atmost/5
if x>=90:
    grade="A grade"
elif x>=75:
    grade="B grade"
elif x>=60:
    grade="C grade"
else:
    grade="D grade"
scorecard={"name":name,"roll no":roll_no,"marks":subject,"total":total,"percentage":x,"grade":grade}
print("=============================================================================================")
print("                                  STUDENT_REPORT_CARD                                        ")
print("=============================================================================================")
print("name",":",scorecard["name"])
print("roll_no",":",scorecard["roll no"])
for subject in scorecard["marks"]:
    print(subject,":",scorecard["marks"][subject])
print("total",":",scorecard["total"],"/",atmost*5)
print("percentage",":",round(scorecard["percentage"],2),"%")
print("grade",":",scorecard["grade"])
