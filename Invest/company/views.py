from django.shortcuts import render



def CompanyView(request):
    return render(request, 'company/company.html')