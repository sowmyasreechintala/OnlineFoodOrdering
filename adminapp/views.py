from django.shortcuts import render,redirect
from adminapp.models import AdminLoginModel,StateModel,CityModel,CuisineModel
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



def openVendor(request):
    return render(request,"admin/openvendor.html")
def openReports(request):
    return render(request,"admin/report.html")

def openState(request):
    data=StateModel.objects.all()
    return render(request,"admin/openstate.html",{"data":data})
def state_submit(request):
    sname=request.POST.get("sname")
    # # sfile=request.FILES["sphoto"]
    # data=StateModel.objects.create(state_name=sname,state_photo=sfile)
    # print(data)
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
    photo=request.FILES["suphoto"]
    StateModel.objects.filter(state_id=sid).update(state_name=sname,state_photo=photo)
    return redirect('state')
def delete_state(request):
    sid=request.GET.get("stateid")
    print(sid)
    StateModel.objects.get(state_id=sid).delete()
    return redirect('state')




def openCity(request):
    data=CityModel.objects.all()
    state_data=StateModel.objects.all()
    return render(request,"admin/opencity.html",{"data":data,"state_data":state_data})
def city_submit(request):
    sname=request.POST.get("sname")
    res=StateModel.objects.get(state_name=sname)
    cname=request.POST.get("cname")
    cfile=request.FILES["cphoto"]
    data=CityModel.objects.create(city_name=cname,city_photo=cfile,city_state_id=res.state_id)
    print(data)
    return redirect('city')
def city_update(request):
    cid=request.GET.get("cid")
    print(cid)
    res=CityModel.objects.get(city_id=cid)
    return render(request,"admin/opencity.html",{"res":res})
def city_update_process(request):
    cid=request.POST.get("cid")
    cname=request.POST.get("cuname")
    cphoto=request.FILES["cuphoto"]
    CityModel.objects.filter(city_id=cid).update(city_name=cname,city_photo=cphoto)
    return redirect('city')
def delete_city(request):
    cid=request.GET.get("cityid")
    print(cid)
    CityModel.objects.get(city_id=cid).delete()
    return redirect('city')





def openCuisine(request):
    data=CuisineModel.objects.all()
    return render(request,"admin/opencuisine.html",{"data":data})
def cuisine_submit(request):
    pname=request.POST.get("pname")
    pfile=request.FILES["pphoto"]
    data=CuisineModel.objects.create(cuisine_name=pname,cuisine_photo=pfile)
    print(data)
    return redirect('cuisine')
def cuisine_update(request):
    pid=request.GET.get("pid")
    print(pid)
    res=CuisineModel.objects.get(cuisine_id=pid)
    return render(request,"admin/opencuisine.html",{"res":res})
def cuisine_update_process(request):
    pid=request.POST.get("pid")
    pname=request.POST.get("puname")
    pphoto=request.FILES["puphoto"]
    CuisineModel.objects.filter(cuisine_id=pid).update(cuisine_name=pname,cuisine_photo=pphoto)
    return redirect('cuisine')
def delete_cuisine(request):
    pid=request.GET.get("pid")
    print(pid)
    CuisineModel.objects.get(cuisine_id=pid).delete()
    return redirect('cuisine')











