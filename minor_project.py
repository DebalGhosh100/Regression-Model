from datetime import timedelta
from tkinter.ttk import *
from tkinter import *
import datetime
import matplotlib.pyplot as plt
import threading

def cofac(m,t,p,q,n):
	i=0
	j=0
	for row in range(0,n):
		for column in range(0,n):
			if(row!=p and column!=q):
				t[i][j]=m[row][column]
				j+=1
				if(j==n-1):
					i+=1
					j=0
def det(m,n):
	t=[[float(0) for x in range(n)]for y in range(n)]
	d=float(0)
	if(n==1):
		return(m[0][0])
	sign=1
	for f in range(0,n):
		cofac(m,t,0,f,n)
		d+=sign*m[0][f]*det(t,n-1)
		sign*=(-1)
	return(d)
def solve(m,s,a,n):
	for i in range(0,n):
		c=[[float(0) for x in range(n)] for y in range(n)]
		for p in range(0,n):
			for q in range(0,n):
				c[p][q]=m[p][q]
		for j in range(0,n):
			c[j][i]=a[j]
		s[i]=det(c,n)/det(m,n)

car=int(0)
bike=int(1)
bus=int(2)
foot=int(3)
train=int(4)
weekday=int(0)
weekend=int(1)
a=[[float(0) for x in range(2)] for y in range(5)]
b=[[float(0) for x in range(2)] for y in range(5)]
c=[[float(0) for x in range(2)] for y in range(5)]


x=0
y=1
car_weekday=[[float(0) for x in range(10)] for y in range(2)]
car_weekend=[[float(0) for x in range(10)] for y in range(2)]
bike_weekday=[[float(0) for x in range(10)] for y in range(2)]
bike_weekend=[[float(0) for x in range(10)] for y in range(2)]
bus_weekday=[[float(0) for x in range(10)] for y in range(2)]
bus_weekend=[[float(0) for x in range(10)] for y in range(2)]
train_weekday=[[float(0) for x in range(10)] for y in range(2)]
train_weekend=[[float(0) for x in range(10)] for y in range(2)]
foot_weekday=[[float(0) for x in range(10)] for y in range(2)]
foot_weekend=[[float(0) for x in range(10)] for y in range(2)]


for j in range(0,10):
	car_weekend[x][j]=20+10*float(j)
	car_weekend[y][j]=car_weekend[x][j]/80
for j in range(0,10):
	car_weekday[x][j]=30+20*float(j)
	car_weekday[y][j]=car_weekday[x][j]/40
for j in range(0,10):
	bike_weekday[x][j]=10+5*float(j)
	bike_weekday[y][j]=bike_weekday[x][j]/15
for j in range(0,10):
	bike_weekend[x][j]=5+5*float(j)
	bike_weekend[y][j]=bike_weekend[x][j]/20
for j in range(0,10):
	bus_weekday[x][j]=100+20*float(j)
	bus_weekday[y][j]=bus_weekday[x][j]/40
for j in range(0,10):
	bus_weekend[x][j]=100+5*float(j)
	bus_weekend[y][j]=bus_weekend[x][j]/60

for j in range(0,10):
	train_weekday[x][j]=200+15*float(j)
	train_weekday[y][j]=train_weekday[x][j]/150
for j in range(0,10):
	train_weekend[x][j]=200+10*float(j)
	train_weekend[y][j]=train_weekend[x][j]/250
for j in range(0,10):
	foot_weekday[x][j]=2+1*float(j)
	foot_weekday[y][j]=foot_weekday[x][j]/3
for j in range(0,10):
	foot_weekend[x][j]=2+1*float(j)
	foot_weekend[y][j]=foot_weekend[x][j]/5


def trainData(item,vehicle,day):
	m=[[float(0) for x in range(3)] for y in range(3)]
	
	sum=float(0)
	for i in range(0,10):
		sum+=(item[x][i])*(item[x][i])
	m[0][0]=sum
	m[1][1]=sum
	m[2][2]=sum
	
	sum=float(0)
	for i in range(0,10):
		sum+=(item[x][i])*(item[x][i])*(item[x][i])
	m[1][0]=sum
	m[2][1]=sum
	
	sum=float(0)
	for i in range(0,10):
		sum+=(item[x][i])*(item[x][i])*(item[x][i])*(item[x][i])
	m[2][2]=sum
	
	sum=float(0)
	for i in range(0,10):
		sum+=(item[x][i])
	m[0][1]=sum
	m[1][2]=sum
	
	m[0][2]=10
	
	ans=[float(0) for x in range(3)]
	sum=float(0)
	for i in range(0,10):
		sum=sum+item[y][i]
	ans[0]=sum
	
	sum=float(0)
	for i in range(0,10):
		sum=sum+item[y][i]*item[x][i]
	ans[1]=sum
	
	sum=float(0)
	for i in range(0,10):
		sum=sum+item[y][i]*item[x][i]*item[x][i]
	ans[2]=sum
	
	s=[float(0) for x in range(3)]
	solve(m,s,ans,3)
	a[vehicle][day]=s[0]
	b[vehicle][day]=s[1]
	c[vehicle][day]=s[2]

trainData(bus_weekday,bus,weekday)
trainData(bus_weekend,bus,weekend)
trainData(car_weekday,car,weekday)
trainData(car_weekend,car,weekend)
trainData(bike_weekday,bike,weekday)
trainData(bike_weekend,bike,weekend)
trainData(foot_weekday,foot,weekday)
trainData(foot_weekend,foot,weekend)
trainData(train_weekday,train,weekday)
trainData(train_weekend,train,weekend)


def distanceCovered(vehicle,d,day):
	sum=float(0)
	sum=a[vehicle][day]*d*d+b[vehicle][day]*d+c[vehicle][day]
	return(sum)



graphWindow=Tk()
totalDist=float(0)

large_font = ('Verdana',15)
small_font = ('Verdana',10)

var1=var = StringVar(value='')

timeLabel=Frame(graphWindow)
timeLabel1=Label(timeLabel,text="  ")
timeLabel1.config(font=large_font)
timeLabel2=Label(timeLabel,text="  ")
timeLabel2.config(font=large_font)
timeLabel1.pack(side="top")
timeLabel2.pack(side="top")

menubar=Menu(graphWindow)
edit=Menu(menubar,tearoff=0)

menubar.add_cascade(label ='Edit', menu = edit) 
remaining=float(100)

m=Menu(graphWindow)
ed=Menu(m,tearoff=0)
m.add_cascade(label ='Options', menu = ed) 

def goBack():
	global f1
	global f15
	global f2
	global f3
	global lBottom1
	global lBottom2
	global lBottom3
	global lBottom4
	global menubar
	global cal
	global ver
	global but
	global butFrame
	global newBut
	global timeEntry
	global list
	global totalPercentage
	global timeLabel
	global timeLabel1
	global timeLabel2
	global dEntry1
	
	dEntry1.insert(0,"0")
	timeLabel1.config(text="  ")
	timeLabel2.config(text="  ")
	totalPercentage=100
	f1.pack_forget()
	f15.pack_forget()
	f2.pack_forget()
	f3.pack_forget()
	lBottom1.pack_forget()
	lBottom2.pack_forget()
	lBottom3.pack_forget()
	lBottom4.pack_forget()
	but.grid_forget()
	newBut.grid_forget()
	but.pack(side="top")
	
	but.config(text="Verify")
	graphWindow.config(menu=menubar)
	cal.pack(side="top")
	timeEntry.pack(side="top")
	ver.pack(side="top")
	butFrame.pack(side="top")
	list.pack(side="bottom")
	timeLabel.pack(side="bottom")
	
	
	


ed.add_command(label ='Back', command = goBack) 

ed.add_command(label ='View Dataset', command = None) 




def go():
	global f1
	global f15
	global f2
	global f3
	global graphWindow
	global cal
	global ver
	global but
	global label1
	global list
	global button
	global dist
	global superLabel
	global final
	global timeEntry
	global timeLabel
	global m
	global lBottom1
	global lBottom2
	global lBottom3
	global lBottom4
	
	
	timeLabel.pack_forget()
	timeEntry.pack_forget()
	superLabel.pack_forget()
	final.pack_forget()
	button.pack_forget()
	dist.pack_forget()
	list.pack_forget()
	label1.pack_forget()
	but.pack_forget()
	cal.pack_forget()
	ver.pack_forget()
	
	f1.pack(side="top")
	f15.pack(side="top")
	f2.pack(side="top")
	f3.pack(side="top")
	lBottom4.pack(side="bottom")
	lBottom3.pack(side="bottom")
	lBottom2.pack(side="bottom")
	lBottom1.pack(side="bottom")
	graphWindow.config(menu=m)
	
final=Frame(graphWindow)
final2=Frame(final)
p=Entry(final2,width=3,font=large_font)
textP=Label(final2,text="% of the journey covered by")
textP.config(font=large_font)
final1=Frame(final)

totalPercentage=float(100)
def computeCar():
	global p
	global index
	global totalDist
	global list
	global current
	global totalPercentage
	global label1
	global car
	global weekday
	global weekend
	xDay=int(current.strftime("%w"))
	dayOfJourney=int(0)
	if(xDay==0 or xDay==6):
		dayOfJourney=weekend
	else:
		dayOfJourney=weekday

		
	d=float(p.get())
	if(totalPercentage==100):
		mystr=current.strftime("%X")+": Journey Started"
		list.insert((index),mystr)
		index+=1
	totalPercentage=totalPercentage-d
	string=(str(totalPercentage)+"% journey remaining")
	if(totalPercentage>=0 and totalPercentage<=100):
		label1.config(text=string,fg="green")
	d=(d*totalDist)/100
	d=distanceCovered(car,d,dayOfJourney)
	if(totalPercentage>=0):
		current=current+timedelta(hours=d)
	myString=current.strftime("%c")+" : by Car"

	myString1="Time of arrival is "+current.strftime("%X")
	myString2="("+str(100-totalPercentage)+"% of the journey covered.)"
	if(totalPercentage>=0):
		list.insert(index,myString)
		index+=1
	global timeLabel1
	global timeLabel2
	if(totalPercentage>=0):
		timeLabel1.config(text=myString1,fg="green")
		timeLabel2.config(text=myString2,fg="green")
	if(totalPercentage==0):
		mystr=current.strftime("%X")+": Journey Finished"
		list.insert((index),mystr)
		index+=1
	
def computeBus():
	global p
	global index
	global totalDist
	global list
	global current
	global totalPercentage
	global label1
	global bus
	global weekday
	global weekend
	xDay=int(current.strftime("%w"))
	dayOfJourney=int(0)
	if(xDay==0 or xDay==6):
		dayOfJourney=weekend
	else:
		dayOfJourney=weekday

		
	d=float(p.get())
	
	if(totalPercentage==100):
		mystr=current.strftime("%X")+": Journey Started"
		list.insert((index),mystr)
		index+=1
	totalPercentage=totalPercentage-d
	string=(str(totalPercentage)+"% journey remaining")
	if(totalPercentage>=0 and totalPercentage<=100):
		label1.config(text=string,fg="green")
	d=(d*totalDist)/100
	d=distanceCovered(bus,d,dayOfJourney)
	if(totalPercentage>=0):
		current=current+timedelta(hours=d)
	myString=current.strftime("%c")+" : by Bus"

	myString1="Time of arrival is "+current.strftime("%X")
	myString2="("+str(100-totalPercentage)+"% of the journey covered.)"
	if(totalPercentage>=0):
		list.insert(index,myString)
		index+=1
	global timeLabel1
	global timeLabel2
	if(totalPercentage>=0):
		timeLabel1.config(text=myString1,fg="green")
		timeLabel2.config(text=myString2,fg="green")
	if(totalPercentage==0):
		mystr=current.strftime("%X")+": Journey Finished"
		list.insert((index),mystr)
		index+=1
	

def computeFoot():
	global p
	global index
	global totalDist
	global list
	global current
	global totalPercentage
	global label1
	global foot
	global weekday
	global weekend
	xDay=int(current.strftime("%w"))
	dayOfJourney=int(0)
	if(xDay==0 or xDay==6):
		dayOfJourney=weekend
	else:
		dayOfJourney=weekday

		
	d=float(p.get())
	
	if(totalPercentage==100):
		mystr=current.strftime("%X")+": Journey Started"
		list.insert((index),mystr)
		index+=1
	totalPercentage=totalPercentage-d
	string=(str(totalPercentage)+"% journey remaining")
	if(totalPercentage>=0 and totalPercentage<=100):
		label1.config(text=string,fg="green")
	d=(d*totalDist)/100
	d=distanceCovered(foot,d,dayOfJourney)
	if(totalPercentage>=0):
		current=current+timedelta(hours=d)
	myString=current.strftime("%c")+" : by Foot"

	myString1="Time of arrival is "+current.strftime("%X")
	myString2="("+str(100-totalPercentage)+"% of the journey covered.)"
	if(totalPercentage>=0):
		list.insert(index,myString)
		index+=1
	global timeLabel1
	global timeLabel2
	if(totalPercentage>=0):
		timeLabel1.config(text=myString1,fg="green")
		timeLabel2.config(text=myString2,fg="green")
	if(totalPercentage==0):
		mystr=current.strftime("%X")+": Journey Finished"
		list.insert((index),mystr)
		index+=1


def computeTrain():
	global p
	global index
	global totalDist
	global list
	global current
	global totalPercentage
	global label1
	global train
	global weekday
	global weekend
	xDay=int(current.strftime("%w"))
	dayOfJourney=int(0)
	if(xDay==0 or xDay==6):
		dayOfJourney=weekend
	else:
		dayOfJourney=weekday

		
	d=float(p.get())
	if(totalPercentage==100):
		mystr=current.strftime("%X")+": Journey Started"
		list.insert((index),mystr)
		index+=1
	
	totalPercentage=totalPercentage-d
	string=(str(totalPercentage)+"% journey remaining")
	if(totalPercentage>=0 and totalPercentage<=100):
		label1.config(text=string,fg="green")
	d=(d*totalDist)/100
	d=distanceCovered(train,d,dayOfJourney)
	if(totalPercentage>=0):
		current=current+timedelta(hours=d)
	myString=current.strftime("%c")+" : by Train"

	myString1="Time of arrival is "+current.strftime("%X")
	myString2="("+str(100-totalPercentage)+"% of the journey covered.)"
	if(totalPercentage>=0):
		list.insert(index,myString)
		index+=1
	global timeLabel1
	global timeLabel2
	if(totalPercentage>=0):
		timeLabel1.config(text=myString1,fg="green")
		timeLabel2.config(text=myString2,fg="green")
	if(totalPercentage==0):
		mystr=current.strftime("%X")+": Journey Finished"
		list.insert((index),mystr)
		index+=1
	

def computeBike():
	global p
	global index
	global totalDist
	global list
	global current
	global totalPercentage
	global label1
	global bike
	global weekday
	global weekend
	xDay=int(current.strftime("%w"))
	dayOfJourney=int(0)
	if(xDay==0 or xDay==6):
		dayOfJourney=weekend
	else:
		dayOfJourney=weekday

		
	d=float(p.get())
	if(totalPercentage==100):
		mystr=current.strftime("%X")+": Journey Started"
		list.insert((index),mystr)
		index+=1
	
	totalPercentage=totalPercentage-d
	string=(str(totalPercentage)+"% journey remaining")
	if(totalPercentage>=0 and totalPercentage<=100):
		label1.config(text=string,fg="green")
	d=(d*totalDist)/100
	d=distanceCovered(bike,d,dayOfJourney)
	if(totalPercentage>=0):
		current=current+timedelta(hours=d)
	myString=current.strftime("%c")+" : by Bike"

	myString1="Time of arrival is "+current.strftime("%X")
	myString2="("+str(100-totalPercentage)+"% of the journey covered.)"
	
	if(totalPercentage>=0):
		list.insert(index,myString)
		index+=1
	global timeLabel1
	global timeLabel2
	if(totalPercentage>=0):
		timeLabel1.config(text=myString1,fg="green")
		timeLabel2.config(text=myString2,fg="green")
	if(totalPercentage==0):
		mystr=current.strftime("%X")+": Journey Finished"
		list.insert((index),mystr)
		index+=1
	



	
b1=Button(final1,text="Car",command=computeCar)
b2=Button(final1,text="Bus",command=computeBus)
b3=Button(final1,text="Foot",command=computeFoot)
b4=Button(final1,text="Train",command=computeTrain)
b5=Button(final1,text="Bike",command=computeBike)

b1.config(font=large_font)
b2.config(font=large_font)
b3.config(font=large_font)
b4.config(font=large_font)
b5.config(font=large_font)


b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)
b4.grid(row=0,column=3)
b5.grid(row=0,column=4)
p.grid(row=0,column=0)
textP.grid(row=0,column=1)
final2.pack(side="top")
final1.pack(side="top")
font2=('Verdana', 25)
superLabel=Label(graphWindow,text=" ",font=font2)
font3=('Verdana',18)
list=Listbox(graphWindow,height=10,width=30,font=font3)
list.pack(side="bottom")
timeLabel.pack(side="bottom")

edit.add_command(label ='Train Dataset', command = go) 

edit.add_command(label ='View Dataset', command = None) 

graphWindow.config(menu=menubar)


dist=Frame(graphWindow)
dLabel=Label(dist,text="Distance to be covered")
dLabel1=Label(dist,text="Km")
dLabel.config(font=large_font)
dLabel1.config(font=large_font)

dEntry1=Entry(dist,width=5,textvariable=var1,font=large_font)
dLabel.grid(row=0,column=0)
dEntry1.grid(row=0,column=1)
dLabel1.grid(row=0,column=2)

def compute():
	global dist
	global button
	global totalDist
	global final
	global index
	global list
	global dEntry1
	totalDist=float(dEntry1.get())
	st=str(totalDist)+"Km"
	dist.pack_forget()
	button.pack_forget()
	superLabel.config(text=st)
	superLabel.pack(side="top")
	final.pack(side="top")
	s=str(remaining)+"%"+" of the journey remaining"
	list.insert(index,s)
	index+=1


button=Button(graphWindow,text="Compute")
button.config(font=large_font)


cal=Frame(graphWindow)
label1=Label(cal,text="Date in DD/MM/YYYY format: ")
label2=Label(cal,text="/")
label3=Label(cal,text="/")

label1.config(font=large_font)
label2.config(font=large_font)
label3.config(font=large_font)

day=Entry(cal,width=2,font=large_font)
month=Entry(cal,width=2,font=large_font)
year=Entry(cal,width=4,font=large_font)
label1.grid(row=0,column=0)
day.grid(row=0,column=1)
label2.grid(row=0,column=2)
month.grid(row=0,column=3)
label3.grid(row=0,column=4)
year.grid(row=0,column=5)
timeEntry=Frame(graphWindow)

iLabel=Label(timeEntry,text="Time in HH:MM:SS format: ")
iLabel.config(font=large_font)

hourEntry=Entry(timeEntry,width=2,font=large_font)
hourLabel=Label(timeEntry,text=":")
hourLabel.config(font=large_font)
minEntry=Entry(timeEntry,width=2,font=large_font)
minLabel=Label(timeEntry,text=":")
minLabel.config(font=large_font)
secEntry=Entry(timeEntry,width=2,font=large_font)
iLabel.grid(row=0,column=0)
hourEntry.grid(row=0,column=1)
hourLabel.grid(row=0,column=2)
minEntry.grid(row=0,column=3)
minLabel.grid(row=0,column=4)
secEntry.grid(row=0,column=5)


cal.pack(side="top")
timeEntry.pack(side="top")

current=datetime.datetime.now()

day.insert(0,current.strftime("%d"))
month.insert(0,current.strftime("%m"))
year.insert(0,current.strftime("%Y"))
hourEntry.insert(0,current.strftime("%H"))
minEntry.insert(0,current.strftime("%M"))
secEntry.insert(0,current.strftime("%S"))

ver=Frame(graphWindow)
lab1=Label(ver,text="")
lab2=Label(ver,text="Date: Unverified", fg="red")
lab3=Label(ver,text="Time: Unverified",fg="red")
lab4=Label(ver,text="")

lab1.config(font=large_font)
lab2.config(font=large_font)
lab3.config(font=large_font)
lab4.config(font=large_font)

lab1.pack(side="top")
lab2.pack(side="top")
lab3.pack(side="top")
lab4.pack(side="top")
ver.pack(side="top")
dCal=int(0)
mCal=int(0)
yCal=int(0)
hourCal=int(0)
minCal=int(0)
secCal=int(0)
label1=Label(graphWindow,text="")
label1.config(font=large_font)

index=int(0)

def sub():
	global cal
	global ver
	global butFrame
	global timeEntry
	timeEntry.pack_forget()
	cal.pack_forget()
	ver.pack_forget()
	butFrame.pack_forget()
	global dCal
	global mCal
	global yCal
	global label1
	global current
	global dist
	global button
	global list
	global index
	s="Journey starts at "+current.strftime("%H")+":"+current.strftime("%M")+":"+current.strftime("%S")
	label1.config(text=s)
	label1.pack(side="top")
	dist.pack(side="top")
	button.config(command=compute)
	button.pack(side="top")

	
	
	
	
	

def verifyDate():
	global day
	global month
	global year
	global lab1
	global lab3
	global lab2
	global lab4
	global dCal
	global mCal
	global yCal
	global butFrame
	global current
	global hourCal
	global minCal
	global secCal
	global hourEntry
	global minEntry
	global secEntry
	global but
	global newBut
	dCal=int(day.get())
	mCal=int(month.get())
	yCal=int(year.get())
	hourCal=int(hourEntry.get())
	minCal=int(minEntry.get())
	secCal=int(secEntry.get())
	current=datetime.datetime(year=yCal,month=mCal,day=dCal,hour=hourCal,minute=minCal,second=secCal)
	str1="Day of the month:"+current.strftime("%A")
	str2="Month: "+current.strftime("%B")
	str3="Year: "+current.strftime("%Y")
	
	but.pack_forget()
	but.grid(row=0,column=1)
	newBut.grid(row=0,column=2)
	but.config(text="Update",command=verifyDate)
	str4=current.strftime("%H")+":"+current.strftime("%M")+":"+current.strftime("%S")
		
		
	
	lab1.config(text=str1,fg="green")
	lab2.config(text=str2,fg="green")
	lab3.config(text=str3,fg="green")
	lab4.config(text=str4,fg="green")
butFrame=Frame(graphWindow)
but=Button(butFrame,text="verify",command=verifyDate)
but.config(font=large_font)
newBut=Button(butFrame,text="Submit",command=sub)
newBut.config(font=large_font)
but.pack(side="top")
butFrame.pack(side="top")







daySelected=0
vehicleSelected=0
transport=int(0)
travelDay=int(0)
trans="nothing"

lBottom4=Label(graphWindow,text="    ",fg="red")
lBottom3=Label(graphWindow,text="  ")
lBottom2=Label(graphWindow,text="   ",fg="red")
lBottom1=Label(graphWindow,text="  ")

lBottom4.config(font=large_font)
lBottom3.config(font=large_font)
lBottom2.config(font=large_font)
lBottom1.config(font=large_font)

lBottom4.pack(side="bottom")
lBottom3.pack(side="bottom")
lBottom2.pack(side="bottom")
lBottom1.pack(side="bottom")





def enterCar():
	global car
	global travelDay
	global vehicleSelected
	global transport
	global daySelected
	global lBottom1
	global lBottom2
	global lBottom3
	global lBottom4
	global trans
	trans="car"
	vehicleSelected=1
	transport=car
	if(daySelected==0):
		str="Medium of transport: Car"
		str1="Please specify whether the journey commences"
		str2="on week day or week end."
		lBottom2.config(text=str)
		lBottom3.config(text=str1)
		lBottom4.config(text=str2)
	else:
		populate(car,travelDay)
		str1="Data analytics for"
		str2="Mode of transportation: Car"
		str3=" on a "
		str4=None
		if(travelDay==0):
			str4="Weekday"
		else:
			str4="Weekend"
		lBottom1.config(text=str1)
		lBottom2.config(text=str2)
		lBottom3.config(text=str3)
		lBottom4.config(text=str4)
		
		
		
def enterBike():
	global bike
	global travelDay
	global vehicleSelected
	global transport
	global daySelected
	global lBottom1
	global lBottom2
	global lBottom3
	global lBottom4
	global trans
	trans="bike"
	vehicleSelected=1
	transport=bike
	if(daySelected==0):
		str="Medium of transport: Bike"
		str1="Please specify whether the journey commences"
		str2="on week day or week end."
		lBottom2.config(text=str)
		lBottom3.config(text=str1)
		lBottom4.config(text=str2)
	else:
		populate(bike,travelDay)
		str1="Data analytics for"
		str2="Mode of transportation: Bike"
		str3=" on a "
		str4=None
		if(travelDay==0):
			str4="Weekday"
		else:
			str4="Weekend"
		lBottom1.config(text=str1)
		lBottom2.config(text=str2)
		lBottom3.config(text=str3)
		lBottom4.config(text=str4)		


def enterBus():
	global bus
	global travelDay
	global vehicleSelected
	global transport
	global daySelected
	global lBottom1
	global lBottom2
	global lBottom3
	global lBottom4
	global trans
	trans="bus"
	vehicleSelected=1
	transport=bus
	if(daySelected==0):
		str="Medium of transport: Bus"
		str1="Please specify whether the journey commences"
		str2="on week day or week end."
		lBottom2.config(text=str)
		lBottom3.config(text=str1)
		lBottom4.config(text=str2)
	else:
		populate(bus,travelDay)
		str1="Data analytics for"
		str2="Mode of transportation: Bus"
		str3=" on a "
		str4=None
		if(travelDay==0):
			str4="Weekday"
		else:
			str4="Weekend"
		lBottom1.config(text=str1)
		lBottom2.config(text=str2)
		lBottom3.config(text=str3)
		lBottom4.config(text=str4)


def enterTrain():
	global train
	global travelDay
	global vehicleSelected
	global transport
	global daySelected
	global lBottom1
	global lBottom2
	global lBottom3
	global lBottom4
	global trans
	trans="train"
	vehicleSelected=1
	transport=train
	if(daySelected==0):
		str="Medium of transport: Train"
		str1="Please specify whether the journey commences"
		str2="on week day or week end."
		lBottom2.config(text=str)
		lBottom3.config(text=str1)
		lBottom4.config(text=str2)
	else:
		populate(train,travelDay)
		str1="Data analytics for"
		str2="Mode of transportation: Train"
		str3=" on a "
		str4=None
		if(travelDay==0):
			str4="Weekday"
		else:
			str4="Weekend"
		lBottom1.config(text=str1)
		lBottom2.config(text=str2)
		lBottom3.config(text=str3)
		lBottom4.config(text=str4)
	
	
def enterFoot():
	global foot
	global travelDay
	global vehicleSelected
	global transport
	global daySelected
	global lBottom1
	global lBottom2
	global lBottom3
	global lBottom4
	global trans
	trans="foot"
	vehicleSelected=1
	transport=foot
	if(daySelected==0):
		str="Medium of transport: Foot"
		str1="Please specify whether the journey commences"
		str2="on week day or week end."
		lBottom2.config(text=str)
		lBottom3.config(text=str1)
		lBottom4.config(text=str2)
	else:
		populate(foot,travelDay)
		str1="Data analytics for"
		str2="Mode of transportation: Foot"
		str3=" on a "
		str4=None
		if(travelDay==0):
			str4="Weekday"
		else:
			str4="Weekend"
		lBottom1.config(text=str1)
		lBottom2.config(text=str2)
		lBottom3.config(text=str3)
		lBottom4.config(text=str4)


f1=Frame(graphWindow)
tCar=Button(f1,text="Car",command=enterCar)
tBike=Button(f1,text="Bike",command=enterBike)
tTrain=Button(f1,text="Train",command=enterTrain)
tFoot=Button(f1,text="Foot",command=enterFoot)
tBus=Button(f1,text="Bus",command=enterBus)

tCar.config(font=large_font)
tBike.config(font=large_font)
tTrain.config(font=large_font)
tFoot.config(font=large_font)
tBus.config(font=large_font)

tCar.grid(row=0,column=0)
tBike.grid(row=0,column=1)
tTrain.grid(row=0,column=2)
tFoot.grid(row=0,column=3)
tBus.grid(row=0,column=4)

f1.pack(side="top")

def setWeekday():
	global travelDay
	global daySelected
	global vehicleSelected
	global lBottom1
	global lBottom2
	global lBottom3
	global lBottom4
	global trans
	global transport
	global weekday
	global weekend
	travelDay=weekday
	daySelected=1
	if(vehicleSelected==0):
		str1="Travelling on a WeekDay"
		str2="Specify mode of transport"
		lBottom3.config(text=str1)
		lBottom4.config(text=str2)
	else:
		populate(transport,travelDay)
		str1="Data analytics for"
		str2="Mode of transportation: "+trans
		str3=" on a "
		str4=None
		if(travelDay==weekday):
			str4="Weekday"
		else:
			str4="Weekend"
		lBottom1.config(text=str1)
		lBottom2.config(text=str2)
		lBottom3.config(text=str3)
		lBottom4.config(text=str4)
		
	
def setWeekend():
	global travelDay
	global daySelected
	global vehicleSelected
	global lBottom1
	global lBottom2
	global lBottom3
	global lBottom4
	global trans
	global transport
	global weekend
	global weekday
	travelDay=weekend
	daySelected=1
	if(vehicleSelected==0):
		str1="Travelling on a WeekEnd"
		str2="Specify mode of transport"
		lBottom3.config(text=str1)
		lBottom4.config(text=str2)
	else:
		populate(transport,travelDay)
		str1="Data analytics for"
		str2="Mode of transportation: "+trans
		str3=" on a "
		str4=None
		if(travelDay==weekday):
			str4="Weekday"
		else:
			str4="Weekend"
		lBottom1.config(text=str1)
		lBottom2.config(text=str2)
		lBottom3.config(text=str3)
		lBottom4.config(text=str4)

f15=Frame(graphWindow)
tWeekday=Button(f15,text="Week Day",command=setWeekday)
tWeekend=Button(f15,text="Week End",command=setWeekend)
tWeekday.config(font=small_font)
tWeekend.config(font=small_font)

tWeekday.pack(side="top")
tWeekend.pack(side="top")
f15.pack(side="top")


f2=Frame(graphWindow)
l1=Label(f2,text="x")
l1.config(font=small_font)
l2=Label(f2,text="y")
l2.config(font=small_font)
l1.grid(row=0,column=0)
l2.grid(row=0,column=1)
font1=('Verdana',12)

E=[[None for x in range(2)] for y in range(10)]
for i in range(0,10):
        for j in range(0,2):
                var = StringVar(value='')
                E[i][j]=Entry(f2,width=23,textvariable=var,font=font1)
                E[i][j].grid(row=i+1,column=j)
		


def populate(veh,day):
	global E
	global car
	global bike
	global bus
	global foot
	global train
	global weekend
	global weekday
	global transport
	transport=veh
	if(veh==car and day==weekday):
		for i in range(0,2):
			for j in range(0,10):
				E[j][i].delete(0,END)
				E[j][i].insert(0,car_weekday[i][j])
	if(veh==car and day==weekend):
		for i in range(0,2):
			for j in range(0,10):
				E[j][i].delete(0,END)
				E[j][i].insert(0,car_weekend[i][j])
	if(veh==bike and day==weekday):
		for i in range(0,2):
			for j in range(0,10):
				E[j][i].delete(0,END)
				E[j][i].insert(0,bike_weekday[i][j])
	if(veh==bike and day==weekend):
		for i in range(0,2):
			for j in range(0,10):
				E[j][i].delete(0,END)
				E[j][i].insert(0,bike_weekend[i][j])	
				
	if(veh==bus and day==weekday):
		for i in range(0,2):
			for j in range(0,10):
				E[j][i].delete(0,END)
				E[j][i].insert(0,bus_weekday[i][j])
	if(veh==bus and day==weekend):
		for i in range(0,2):
			for j in range(0,10):
				E[j][i].delete(0,END)
				E[j][i].insert(0,bus_weekend[i][j])
	if(veh==train and day==weekday):
		for i in range(0,2):
			for j in range(0,10):
				E[j][i].delete(0,END)
				E[j][i].insert(0,train_weekday[i][j])
	if(veh==train and day==weekend):
		for i in range(0,2):
			for j in range(0,10):
				E[j][i].delete(0,END)
				E[j][i].insert(0,train_weekend[i][j])
	if(veh==foot and day==weekday):
		for i in range(0,2):
			for j in range(0,10):
				E[j][i].delete(0,END)
				E[j][i].insert(0,foot_weekday[i][j])
	if(veh==foot and day==weekend):
		for i in range(0,2):
			for j in range(0,10):
				E[j][i].delete(0,END)
				E[j][i].insert(0,foot_weekend[i][j])
	


	


	

				


dataItem=[[float(0) for x in range(10)] for y in range(2)]



f2.pack(side="top")
def submit():
	global graphWindow
	global dataItem
	global E
	global car
	global bike
	global bus
	global train
	global foot
	global weekday
	global weekend
	global transport
	global car_weekday
	global car_weekend
	global bike_weekday
	global bike_weekend
	global train_weekday
	global train_weekend
	global bus_weekday
	global bus_weekend
	global foot_weekday
	global foot_weekend
	
	global travelDay
	for i in range(0,2):
		for j in range(0,10):
			yx=E[j][i].get()
			dataItem[i][j]=float(yx)
			if(transport==car and travelDay==weekday):
				car_weekday[i][j]=yx
			if(transport==car and travelDay==weekend):
				car_weekend[i][j]=yx
			if(transport==bike and travelDay==weekday):
				bike_weekday[i][j]=yx
			if(transport==bike and travelDay==weekend):
				bike_weekend[i][j]=yx
			if(transport==bus and travelDay==weekday):
				bus_weekday[i][j]=yx
			if(transport==bus and travelDay==weekend):
				bus_weekend[i][j]=yx
			if(transport==foot and travelDay==weekday):
				foot_weekday[i][j]=yx
			if(transport==foot and travelDay==weekend):
				foot_weekend[i][j]=yx
			if(transport==train and travelDay==weekday):
				train_weekday[i][j]=yx
			if(transport==train and travelDay==weekend):
				train_weekend[i][j]=yx
	trainData(dataItem,transport,travelDay)
	
	xi=[0 for c in range(500)]
	yi=[0 for c in range(500)]
	for c in range(0,500):
		xi[c]=c
		yi[c]=distanceCovered(transport,xi[c],weekday)
	string="car"
	if(transport==car):
		string="Car"
	if(transport==bike):
		string="Bike"
	if(transport==train):
		string="Train"
	if(transport==bus):
		string="Bus"
	if(transport==foot):
		string="Foot"
	plt.scatter(yi,xi,marker=".",label=string+" on Weekday",color="green")
	
	for c in range(0,500):
		xi[c]=c
		yi[c]=distanceCovered(transport,xi[c],weekend)
	plt.scatter(yi,xi,marker=".",label=string+" on Weekend",color="blue")
	plt.legend()
	
	plt.show()
	
	


f3=Frame(graphWindow)
trainDat=Button(f3,text="Train Data",command=submit)
trainDat.config(font=small_font)
trainDat.pack(side="top")
f3.pack(side="top")


f1.pack_forget()
f15.pack_forget()
f2.pack_forget()
f3.pack_forget()
graphWindow.mainloop()

