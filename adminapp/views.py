from django.shortcuts import render,redirect
from adminapp.models import AdminLoginModel,StateModel
# Create your views here.
def showindex(request):
    return render(request,"admin/login.html")
def admin_login_check(request):
    if request.method=="POST":
        try:
            admin = AdminLoginModel.objects.get(username=request.POST.get("admin_username"),
                                                password=request.POST.get("admin_password"))
            request.session["admin_status"] = True
            return redirect('welcome')
        except:
            return render(request, "admin/login.html", {"error": "Invalid User"})
    else:
        request.session["admin_status"]=False
        return render(request,"admin/login.html",{"error":"Admin Logout sucess"})
def welcome(request):
    return render(request,"admin/home.html")
def openState(request):
    data=StateModel.objects.all()
    return render(request,"admin/openstate.html",{"data":data})
def openCity(request):
    return render(request,"admin/opencity.html")
def openCuisine(request):
    return render(request,"admin.cuisine.html")
def openVendor(request):
    return render(request,"admin/openvendor.html")
def openReports(request):
    return render(request,"admin/report.html")
def state_submit(request):
    sname=request.POST.get("sname")
    sfile=request.FILES["sphoto"]
    data=StateModel.objects.create(state_name=sname,state_photo=sfile)
    print(data)
    return redirect('state')
def state_update(request):
    sid=request.GET.get("sid")
    print(sid)
    data=StateModel.objects.all()
    res=StateModel.objects.get(state_id=sid)
    return render(request,"admin/openstate.html",{"res":res})
def state_update_process(request):
    sid=request.POST.get("sid")
    sname=request.POST.get("suname")
    sphoto=request.FILES["suphoto"]
    StateModel.objects.filter(state_id=sid).update(state_name=sname,state_photo=sphoto)
    return redirect('state')
def delete_state(request):
    sid=request.GET.get("stateid")
    print(sid)
    StateModel.objects.get(state_id=sid).delete()
    return redirect('state')
