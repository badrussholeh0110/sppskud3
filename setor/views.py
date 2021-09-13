from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.models import Group
from django.db.models import Sum, Q
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import pilihan_login, tolakhalaman_ini, ijinkan_pengguna
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.views.generic import ListView
from io import BytesIO
from django.template.loader import get_template
from django.views import View
from django.utils.timezone import datetime

def pdflap(request):
    cetak = Setoran.objects.values('namaunit__namaunit').annotate(jumlahsetoran_count=Sum('jumlahsetoran'))
    total = Setoran.objects.all().aggregate(Sum('jumlahsetoran'))
    template_path = 'data/pdf_template.html'
    context = {'laporan': cetak, 'total': total}
    # Buat objek tanggapan Django, dan tentukan content_type sebagai pdf
    response = HttpResponse(content_type='application/pdf')
    # jika langsung mau di download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # Jika pdf mau ditampilkan attachment dihapus
    response['Content-Disposition'] = 'filename="report.pdf"'
    # temukan template dan render.
    template = get_template(template_path)
    html = template.render(context)

    # buat pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # jika error tampil sebagai dibawah
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def pdflap1(request):
    petugas = request.user.petugas.namaunit
    cetak = Setoran.objects.filter(namaunit=petugas).values('namaunit__namaunit').annotate(jumlahsetoran_count=Sum('jumlahsetoran'))
    total = Setoran.objects.all().aggregate(Sum('jumlahsetoran'))
    template_path = 'data/pdf_template.html'
    context = {'laporan': cetak, 'total': total}
    # Buat objek tanggapan Django, dan tentukan content_type sebagai pdf
    response = HttpResponse(content_type='application/pdf')
    # jika langsung mau di download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # Jika pdf mau ditampilkan attachment dihapus
    response['Content-Disposition'] = 'filename="report.pdf"'
    # temukan template dan render.
    template = get_template(template_path)
    html = template.render(context)

    # buat pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # jika error tampil sebagai dibawah
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def pdflap2(request):
    peternak = request.user.peternak
    cetak = Setoran.objects.filter(nama=peternak).values('namaunit__namaunit', 'nama__nama', 'harga__harga', 'jumlahsetoran', 'tgl').annotate(jumlahsetoran_count=Sum('jumlahsetoran'))
    total = Setoran.objects.filter(nama=peternak).aggregate(Sum('jumlahsetoran'))
    harga1 = Harga.objects.filter(id='6').aggregate(Sum('harga'))
    # print(harga1)
    # print(total)
    # tam = harga1['Harga']
    # print(tam)
    tot = total['jumlahsetoran__sum'] * harga1['harga__sum']
    # print(tot)
    template_path = 'data/pdf_template2.html'
    context = {'laporan': cetak, 'total': total, 'peternak': peternak, 'tot': tot}
    # Buat objek tanggapan Django, dan tentukan content_type sebagai pdf
    response = HttpResponse(content_type='application/pdf')
    # jika langsung mau di download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # Jika pdf mau ditampilkan attachment dihapus
    response['Content-Disposition'] = 'filename="report.pdf"'
    # temukan template dan render.
    template = get_template(template_path)
    html = template.render(context)

    # buat pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # jika error tampil sebagai dibawah
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def pdfpeter(request, pk):
    peternak = Peternak.objects.get(id=pk)
    cetak = Setoran.objects.filter(nama=peternak).values('namaunit__namaunit', 'nama__nama', 'harga__harga', 'jumlahsetoran', 'tgl').annotate(jumlahsetoran_count=Sum('jumlahsetoran'))
    total = Setoran.objects.filter(nama=peternak).aggregate(Sum('jumlahsetoran'))
    harga1 = Harga.objects.filter(id='6').aggregate(Sum('harga'))
    # print(harga1)
    # print(total)
    # tam = harga1['Harga']
    # print(tam)
    tot = total['jumlahsetoran__sum'] * harga1['harga__sum']
    # print(tot)
    template_path = 'data/pdf_template2.html'
    context = {'laporan': cetak, 'total': total, 'peternak': peternak, 'tot': tot}
    # Buat objek tanggapan Django, dan tentukan content_type sebagai pdf
    response = HttpResponse(content_type='application/pdf')
    # jika langsung mau di download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # Jika pdf mau ditampilkan attachment dihapus
    response['Content-Disposition'] = 'filename="report.pdf"'
    # temukan template dan render.
    template = get_template(template_path)
    html = template.render(context)

    # buat pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # jika error tampil sebagai dibawah
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


# Create your views here.
@login_required(login_url='login')
@pilihan_login
def home(request):    
    grafik = Setoran.objects.values('namaunit__namaunit').annotate(jumlahsetoran_count=Sum('jumlahsetoran'))
    grafik1 = Setoran.objects.values('namaunit__namaunit').annotate(jumlahsetoran_count=Sum('jumlahsetoran', filter=Q(tgl=datetime.today())))
    peternak = Peternak.objects.all().count()
    setoran = Setoran.objects.all().aggregate(Sum('jumlahsetoran'))
    unit = Unit.objects.all().count()
    petugas = Petugas.objects.all().count()
    print (grafik1)
    print (grafik)
    context = {
        'judul': 'Halaman Utama',
        'peternak': peternak,
        'petugas': petugas,
        'unit': unit,
        'setoran': setoran,
        'grafik': grafik,
        'grafik1': grafik1
    }
    return render(request, 'data/home2.html', context) 

def uuser(request, pk):
    user = User.objects.get(id=pk)
    ubah = UuserForm(instance=user)
    if request.method == 'POST':
        formubah = UuserForm(request.POST, instance=user)
        if formubah.is_valid:
            formubah.save()
            return redirect('/petugas/')
    context = {
        'judul': 'Ubah Peternak',
        'form': ubah,
    }
    return render(request, 'data/input_form.html', context)

def uuuser(request):
    user = request.user
    ubah = UuserForm(instance=user)
    if request.method == 'POST':
        formubah = UuserForm(request.POST, instance=user)
        if formubah.is_valid:
            formubah.save()
            return redirect('/petugas/')
    context = {
        'judul': 'Ubah Petugas',
        'form': ubah,
    }
    return render(request, 'data/input_form.html', context)

def uuseradmin(request):
    user = request.user
    ubah = UuserForm(instance=user)
    if request.method == 'POST':
        formubah = UuserForm(request.POST, instance=user)
        if formubah.is_valid:
            formubah.save()
            return redirect('/petugas/')
    context = {
        'judul': 'Ubah Petugas',
        'form': ubah,
    }
    return render(request, 'data/input_form1.html', context)

def uuseradmin1(request):
    user = request.user
    ubah = UuserForm1(instance=user)
    if request.method == 'POST':
        formubah = UuserForm1(request.POST, instance=user)
        if formubah.is_valid:
            formubah.save()
            return redirect('/home/')
    context = {
        'judul': 'Ubah Admin',
        'form': ubah,
    }
    return render(request, 'data/input_form1.html', context)

def uuserpeternak(request):
    user = request.user
    ubah = UuserForm(instance=user)
    if request.method == 'POST':
        formubah = UuserForm(request.POST, instance=user)
        if formubah.is_valid:
            formubah.save()
            return redirect('/petugas/')
    context = {
        'judul': 'Ubah peternak',
        'form': ubah,
    }
    return render(request, 'data/input_form2.html', context)


@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan='admin')
def petugas(request):
    petugas1 = Petugas.objects.all()
    petugas = Petugas.objects.values('id', 'namapetugas', 'namaunit__namaunit', 'user__id', 'user__username', 'user__email')
    print (petugas)
    context = {
        'judul': 'Halaman Petugas',
        'Petugas': petugas,
    }
    return render(request, 'data/petugas2.html', context)

def Tpetugas(request):
    formpetugas = UserForm()
    if request.method == 'POST':
        formsimpan = UserForm(request.POST)
        if formsimpan.is_valid:
            petugas = formsimpan.save()
            grup = Group.objects.get(name='petugas')
            petugas.groups.add(grup)
            Petugas.objects.create(
                namapetugas=petugas.first_name,
                level=petugas.last_name,
                user=petugas),
            return redirect('/petugas/')
    context = {
        'judul': 'form tambah petugas',
        'form': formpetugas,
        }
    return render(request, 'data/input_form.html', context)
        
def Upetugas(request, pk):
    petugas = Petugas.objects.get(id=pk)
    ubah = PetugasForm(instance=petugas)
    if request.method == 'POST':
        formubah = PetugasForm(request.POST, instance=petugas)
        if formubah.is_valid:
            formubah.save()
            return redirect('/petugas/')
    context = {
        'judul': 'Ubah Petugas',
        'form': ubah,
    }
    return render(request, 'data/input_form.html', context)

def Hpetugas(request, pk):
    petugas = Petugas.objects.get(id=pk)
    petugas.delete()

    return redirect('petugas')


def unit(request):
    unit = Unit.objects.all()
    context = {
        'judul': 'Halaman unit',
        'unit': unit,
    }
    return render(request, 'data/unit2.html', context)
    
def Tunit(request):
    formunit = UnitForm()
    if request.method == 'POST':
        formsimpan = UnitForm(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/unit/')
    context = {
        'judul': 'form tambah unit',
        'form': formunit,
        }
    return render(request, 'data/input_form.html', context)


def Uunit(request, pk):
    unit = Unit.objects.get(id=pk)
    ubah = UnitForm(instance=unit)
    if request.method == 'POST':
        formubah = UnitForm(request.POST, instance=unit)
        if formubah.is_valid:
            formubah.save()
            return redirect('/unit/')
    context = {
        'judul': 'Ubah Unit',
        'form': ubah,
    }
    return render(request, 'data/input_form.html', context)

def Hunit(request, pk):
    unit = Unit.objects.get(id=pk)
    unit.delete()

    return redirect('unit')

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan='admin')
def peternak(request):
    peternak1 = Peternak.objects.all()
    peternak = Peternak.objects.values('id', 'nama', 'alamat', 'namaunit__namaunit', 'user__id', 'user__username', 'user__email')
    context = {
        'judul': 'Halaman Peternak',
        'Peternak': peternak,
    }
    return render(request, 'data/peternak2.html', context)

# def Tpeternak(request):
#     formpeternak = PeternakForm()
#     if request.method == 'POST':
#         formsimpan = PeternakForm(request.POST)
#         if formsimpan.is_valid:
#             formsimpan.save()
#             return redirect('/peternak/')
#     context = {
#         'judul': 'form tambah peternak',
#         'form': formpeternak,
#         }
#     return render(request, 'data/input_form.html', context)

def Tpeternak(request):
    formpeternak = UserpeternakForm()
    if request.method == 'POST':
        formsimpan = UserpeternakForm(request.POST)
        if formsimpan.is_valid:
            peternak = formsimpan.save()
            grup = Group.objects.get(name='peternak')
            peternak.groups.add(grup)
            Peternak.objects.create(
                nama=peternak.first_name,
                level=peternak.last_name,
                user=peternak),
            return redirect('/peternak/')
    context = {
        'judul': 'form tambah peternak',
        'form': formpeternak,
        }
    return render(request, 'data/input_form.html', context)

def Upeternak(request, pk):
    peternak = Peternak.objects.get(id=pk)
    ubah = PeternakForm(instance=peternak)
    if request.method == 'POST':
        formubah = PeternakForm(request.POST, instance=peternak)
        if formubah.is_valid:
            formubah.save()
            return redirect('/peternak/')
    context = {
        'judul': 'Ubah peternak',
        'form': ubah,
    }
    return render(request, 'data/input_form.html', context)

def Hpeternak(request, pk):
    peternak = Peternak.objects.get(id=pk)
    peternak.delete()

    return redirect('peternak')

def harga(request):
    harga = Harga.objects.all()
    context = {
        'judul': 'Halaman harga',
        'harga': harga,
    }
    return render(request, 'data/harga2.html', context)

def Tharga(request):
    harga = HargaForm()
    if request.method == 'POST':
        formsimpan = HargaForm(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/harga/')
    context = {
        'judul': 'form tambah harga',
        'form': harga,
        }
    return render(request, 'data/input_form.html', context)

def Uharga(request, pk):
    harga = Harga.objects.get(id=pk)
    ubah = HargaForm(instance=harga)
    if request.method == 'POST':
        formubah = HargaForm(request.POST, instance=harga)
        if formubah.is_valid:
            formubah.save()
            return redirect('/harga/')
    context = {
        'judul': 'Ubah harga',
        'form': ubah,
    }
    return render(request, 'data/input_form.html', context)

def Hharga(request, pk):
    harga = Harga.objects.get(id=pk)
    harga.delete()

    return redirect('harga')

@login_required(login_url='login')
def setoran(request):
    # petugas = request.user.petugas
    setoran = Setoran.objects.all()
    context = {
        'judul': 'Halaman Setoran',
        'setoran': setoran,
        # 'petugas': petugas,
    }
    return render(request, 'data/setorann.html', context)

@login_required(login_url='login')
def setoran1(request):
    petugas = request.user.petugas.namaunit
    setoran = Setoran.objects.filter(namaunit=petugas)
    context = {
        'judul': 'Halaman Setoran',
        'setoran': setoran,
        # 'petugas': petugas,
    }
    return render(request, 'data/setorann1.html', context)
@login_required(login_url='login')
def setoran2(request):
    peternak = request.user.peternak
    setoran = Setoran.objects.filter(nama=peternak)
    context = {
        'judul': 'Halaman Setoran',
        'setoran': setoran,
        # 'petugas': petugas,
    }
    return render(request, 'data/setorann2.html', context)

def Tsetoran(request):
    petugas = request
    # petugas = request.user.petugas.namaunit
    setoran = SetoranForm()
    if request.method == 'POST':
        formsimpan = SetoranForm(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/setoran/')
    context = {
        'judul': 'form tambah setoran',
        'form': setoran,
        }
    return render(request, 'data/input_form.html', context)

def Usetoran(request, pk):
    setoran = Setoran.objects.get(id=pk)
    ubah = SetoranForm(instance=setoran)
    if request.method == 'POST':
        formubah = SetoranForm(request.POST, instance=setoran)
        if formubah.is_valid:
            formubah.save()
            return redirect('/setoran/')
    context = {
        'judul': 'Ubah setoran',
        'form': ubah,
    }
    return render(request, 'data/input_form.html', context)

def Hsetoran(request, pk):
    setoran = Setoran.objects.get(id=pk)
    setoran.delete()

    return redirect('setoran')


def Tsetoran1(request):
    petugas = request.user.petugas
    # petugas = request.user.petugas.namaunit
    setoran = SetoranForm(instance=petugas)
    if request.method == 'POST':
        formsimpan = SetoranForm(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/setoran1/')
    context = {
        'judul': 'form tambah setoran',
        'form': setoran,
        }
    return render(request, 'data/input_form1.html', context)

def Usetoran1(request, pk):
    setoran = Setoran.objects.get(id=pk)
    ubah = SetoranForm(instance=setoran)
    if request.method == 'POST':
        formubah = SetoranForm(request.POST, instance=setoran)
        if formubah.is_valid:
            formubah.save()
            return redirect('/setoran1/')
    context = {
        'judul': 'Ubah setoran',
        'form': ubah,
    }
    return render(request, 'data/input_form1.html', context)

def Hsetoran1(request, pk):
    setoran = Setoran.objects.get(id=pk)
    setoran.delete()

    return redirect('setoran1')


def loginPage (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        cocokan = authenticate(request, username=username, password=password)
        # print (cocokan)
        if cocokan is not None:
            login(request, cocokan)
            return redirect('home')

    context = {
        'judul': 'Halaman Login',
        'menu': 'login'
    }
    return render(request, 'data/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')

def lihathasil(request, pk):
    peternak = Peternak.objects.get(id=pk)
    setoran = Setoran.objects.filter(nama=peternak)
    context = {
        'judul': 'Halaman Hasil Setoran',
        'setoran': setoran,
    }
    return render(request, 'data/setorann3.html', context)

def peternakunit(request, pk):
    unit = Unit.objects.get(id=pk)
    peternak = Peternak.objects.filter(namaunit=unit)
    context = {
        'judul': 'Halaman Peternak',
        'Peternak': peternak,
    }
    return render(request, 'data/peternakunit1.html', context)