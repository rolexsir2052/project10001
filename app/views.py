from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def Normal_sheet(request):
    import openpyxl
    x=openpyxl.load_workbook("C:\\Users\\pavan\\OneDrive\\Documents\\Django\\rolex\\Scripts\\project10001\\app\\normal_excel_sheet.xlsx")
    y=x["Sheet1"]
    for i in y.iter_rows(min_row=2,values_only=True):
        N=Normal.objects.get_or_create(name=i[0],age=i[1],marks=i[2],mobile=i[3],place=i[4])[0]
        N.save()
    return HttpResponse('inserted data') 
def Google_sheet(request):
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    scope=["https://www.googleapis.com/auth/drive"]
    C=ServiceAccountCredentials.from_json_keyfile_name("C:\\Users\\pavan\\OneDrive\\Documents\\Django\\rolex\\Scripts\\project10001\\app\\key.json",scope)
    X=gspread.authorize(C)
    S=X.open("google_sheet_1").sheet1
    data=S.get_all_values()
    for n in data[1::]:
        G=Google.objects.get_or_create(name=n[0],age=n[1],marks=n[2],mobile=n[3],place=n[4])[0]
        G.save()
    return HttpResponse('inserted google sheet data')

def display_data(request):
    N=Normal.objects.all()
    G=Google.objects.all()
    obj=[]
    for i in N:
        if G.filter(place=i.place).exists():
            obj.append(i)
    d={'obj':obj}
    return render(request,'data.html',d)