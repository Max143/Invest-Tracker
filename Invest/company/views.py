from django.shortcuts import render
from investors.models import Investor, Investment



def PaymentView(request):
    return render(request, 'company/transfer.html')



# Home View
def CompanyView(request):
    all_investor = Investor.objects.all()
    context = {

        'all_investor':all_investor
     }
    return render(request, 'company/company.html', context)



# Each investor Record view
def RecordView(request,id):
    print ("id :",id)
    all_investor = Investor.objects.all()
    # total_investment = Investment.objects.all()
    total_investment=Investment.objects.filter(investor=id)
    print("all_investor :",all_investor)
    print("total_investment :",total_investment)
    investor_id = Investor.objects.get(id=id)
    print("investor_id :",investor_id)
    investor_name = investor_id.name
    print("investor_name :",investor_name)

    try:
        investor_id = request.GET.get('investor_id')
        investor_id = int(investor_id)
        investment = Investment.objects.filter(pk=investor_id)
    except:
        pass

    context = {

        'all_investor':all_investor,
        'total_investment':total_investment,
        'investor_name':investor_name
    }

    return render(request, 'company/record.html', context)


# Total Investments Record  View
def TotalRecordView(request):
    total_investment = Investment.objects.all()
    all_investors = Investor.objects.all()
    context = {
        'total_investment':total_investment,
        'all_investors': all_investors
    }
    return render(request, 'company/total.html', context)
