# Create your views here.
'''

 
Create a database per country to store the farmer's data. during onboarding take the country and automatically create a database, not manually
explanation - User1 from country_a should not be kept on the database for country-b. 

Model the following data per country.
-> Farmer data > Phone number, Name, Language 
-> Farm data > Area, Village, Crop grown, Sowing date 
-> Schedule data > Days after sowing, Fertiliser, Quantity, Quantity unit(ton, kg, g for solids and L, mL for liquids)

Views needed.
-> Find all schedules due for today/tomorrow 
-> Find all farmers who are growing a crop 
-> Given prices of fertilizers, calculate the bill of materials for a single farmer

Note: 
There is a 'sowing date' parameter in the farm which defines when sowing was done. 

A farm will have multiple schedules and they have a parameter called 'days from sowing' which define how many days the schedule is followed after sowing. 
We want to know when a schedule is due, given by 'sowing date' + 'days from sowing'

'''
#from django.shortcuts import render
from tkinter import *
from tkinter import ttk
from .models import ModelSchema,FieldSchema
from datetime import date

def schedule_view():
    if (Modelschema.sowing_date + ModelSchema.date_after_sowing)==date.today() or (Modelschema.sowing_date + ModelSchema.date_after_sowing)==date.today+1:
        return Modelschema.sowing_date + ModelSchema.date_after_sowing
    
def Crop_view():
    if (Modelschema.sowing_date + ModelSchema.date_after_sowing)!=date.today():
        return Model.Name


def Fertilizers_view(fert):
    return fertilizers*46

def farmer_details_view():
    master = Tk()
    master.geometry('250x150') 
    
    Label(master, text='Name').grid(row=0,column=2)
    Label(master,text='Country').grid(row=1,column=2)
    Label(master,text='Phone Number').grid(row=2,column=2)
    Label(master,text='Language').grid(row=3,column=2)
    Label(master,text='Area').grid(row=4,column=2)
    Label(master,text='Village').grid(row=5,column=2)
    Label(master,text='Crop grown').grid(row=6,column=2)
    Label(master,text='Sowing Date').grid(row=7,column=2)
    Label(master,text='Days after sowing').grid(row=8,column=2)
    Label(master,text='Fertiliser').grid(row=9,column=2)
    Label(master, text='Quantity').grid(row=10,column=2)
    variable = StringVar(master)
    variable.set("ton")
    
    
    
    
    e1 = Entry(master).grid(row=0, column=3)  
    e2 = Entry(master).grid(row=1, column=3) 
    e3 = Entry(master).grid(row=2, column=3)  
    e4 = Entry(master).grid(row=3, column=3) 
    e5 = Entry(master).grid(row=4, column=3)  
    e6 = Entry(master).grid(row=5, column=3) 
    e7 = Entry(master).grid(row=6, column=3)  
    e8 = Entry(master).grid(row=7, column=3) 
    e9 = Entry(master).grid(row=8, column=3) 
    e10 = Entry(master).grid(row=9, column=3) 
    
    
    w = ttk.Combobox(master,textvariable=variable,values=['kg','g','mL'])
    w.grid(row=10,column=3)
    master.mainloop()
    return e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,w

def createdb(self):
    data = farmer_details_view()
    country_schema = ModelSchema.objects.create(name=self.e1.get())
    Country = country_schema.as_model()
    assert issubclass(Country, models.Model)
    
    # The dynamic model can now be used to create Car instances
    instance = Country.objects.create()
    assert instance.pk is not None
    country_field_schema = ( FieldSchema.objects.create(name='Name', data_type='character',value=data[0].get()),
                            FieldSchema.objects.create(name='Phone_number', data_type='integer',value=data[1].get()),
                           FieldSchema.objects.create(name='Language', data_type='character',value=data[2].get()),
                           FieldSchema.objects.create(name='Area', data_type='character',value=data[3].get()),
                           FieldSchema.objects.create(name='Village', data_type='character',value=data[4].get()),
                           FieldSchema.objects.create(name='crop_grown', data_type='character',value=data[5].get()),
                           FieldSchema.objects.create(name='sowing_date', data_type='date',value=data[6].get()),
                           FieldSchema.objects.create(name='date_after_sowing', data_type='date',value=data[7].get()),
                           FieldSchema.objects.create(name='Fertilizer', data_type='character',value=data[8].get()),
                           FieldSchema.objects.create(name='Quantity', data_type='integer',value=data[9].get()))
    country = Country.add_field(country_field_schema)
    
