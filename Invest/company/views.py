from django.shortcuts import render
#from django.contrib.decorators import login_required



def CompanyView(request):
    return render(request, 'company/company.html')



#@login_required
def RecordView(request):
    if request.user.is_superuser():

        all_investment = Investment.objects.all()  #  total investement

        context = {

                'all_investment':all_investment,
                'all_investors' : all_investors

        }
        return render(request, 'company/record.html', context)



#@login_required
def TotalRecord(request):
    if request.user.is_superuser():
        all_investment = Investment.objects.all()
        args = {'all_investment':all_investment}
        return render(request, 'company/totalrecord.html', args)