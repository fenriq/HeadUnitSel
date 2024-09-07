from django.shortcuts import render, redirect
from .forms import Params
from .models import Headunit

# Create your views here.


def index(request):
    params = Params
    count = Headunit.object_hu.count()
    hudata = Headunit.object_hu.order_by('gu_diag_int')

    if request.method == "POST":
        params = Params(request.POST)
        if params.is_valid():
            width = request.POST.get("width")
            height = request.POST.get("height")
            diag = request.POST.get("diag")
            amin = int(width) - 30
            amax = int(width) + 30
            hmin = int(height) - 30
            hmax = int(height) + 30
            dmin = int(diag) - 1
            dmax = int(diag) + 1
            if width == "0" and height == "0" and diag == "0":
                # если все условия не заданы, выводим все записи БД
                output = "Вы не ввели никаких данных. \
                Посмотрите все имеющиеся варианты: "
                context = {
                    "params": params,
                    "output": output,
                    "hudata": hudata,
                }
                return render(request, 'result_negative.html', context)

            elif width == "0" and height != "0" and diag != "0":
                # если известны две величины - считаем
                # диагональ в миллиметры
                cmm = int(diag) * 25.4
                # квадрат ширины
                a2 = cmm ** 2 - int(height) ** 2
                # корень из квадрата ширины, обрезаем лишнее после запятой
                amm = str(a2 ** 0.5)[0:5]
                dmin = int(diag) - 1
                dmax = int(diag) + 1
                hmin = int(height) - 30
                output = (f"Результаты рассчёта: диагональ {diag} дюйм при высоте {height} мм будет иметь ширину"
                          f" {amm} мм \
                          Похожие результаты: ")
                hudata = Headunit.object_hu.filter(
                    gu_diag_int__gte=dmin,
                    gu_diag_int__lte=dmax,
                    height__gte=hmin,
                )
                context = {
                    "params": params,
                    "output": output,
                    "hudata": hudata,
                }
                return render(request, 'result.html', context)
            elif width != "0" and height == "0" and diag != "0":
                # Известны ширина и диагональ
                cmm = int(diag) * 25.4
                b2 = cmm ** 2 - int(width) ** 2
                bmm = str(b2 ** 0.5)[0:5]
                amin = int(width) - 30
                output = (f"Результаты рассчёта: диагональ {diag} дюйм при ширине {width} мм будет иметь высоту"
                          f" {bmm} мм")
                hudata = Headunit.object_hu.filter(
                    gu_diag_int__gte=dmin,
                    gu_diag_int__lte=dmax,
                    width__gte=amin,
                )
                context = {
                    "params": params,
                    "output": output,
                    "hudata": hudata,
                }
                return render(request, 'result.html', context)
            elif width != "0" and height != "0" and diag == "0":
                # диагональ в квадрате равно теорема Пифагора
                cmm2 = int(width)**2 + int(height)**2
                # извлекаем корень
                cmm = cmm2**0.5
                # и обрезаем, затем переводим в дюймы
                cm_s = str(cmm)[0:5]
                cdd = str(cmm / 25.4)[0:5]
                amin = int(width) - 30
                amax = int(width) + 30
                hmin = int(height) - 30
                hmax = int(height) + 30
                diag = cdd
                dmin = round(float(diag)) - 1
                dmax = round(float(diag)) + 1
                output = (f"Результаты рассчёта: При размерах {width} мм в ширину и {height} "
                          f"мм в высоту магнитола будет иметь диагональ {cdd} дюймов ({cm_s} мм) \
                Следующие магнитолы подходят под это описание: ")
                hudata = Headunit.object_hu.filter(
                    width__gte=amin,
                    height__gte=hmin,
                    gu_diag_int__gte=dmin,
                    gu_diag_int__lte=dmax,
                )
                context = {
                    "params": params,
                    "output": output,
                    "hudata": hudata,
                }
                return render(request, 'result.html', context)
            elif width == "0" and height == "0" and diag != "0":
                # Известна только диагональ
                dmin = int(diag) - 1
                dmax = int(diag) + 1
                output = (f"Известна только диагональ - {diag} дюймов."
                          f"Следующие результаты подходят под это описание: ")
                hudata = Headunit.object_hu.filter(
                    gu_diag_int__gte=dmin,
                    gu_diag_int__lte=dmax,
                )
                context = {
                    "params": params,
                    "output": output,
                    "hudata": hudata,
                }
                return render(request, 'result.html', context)
            elif width == "0" and height != "0" and diag == "0" or width != "0" and height == "0" and diag == "0":
                # Задан только один параметр
                output = f"Известен только один параметр. " \
                          f"Посмотрите весь каталог, чтобы подобрать нужный результат: "
                hudata = Headunit.object_hu.all
                context = {
                    "params": params,
                    "output": output,
                    "hudata": hudata,
                }
                return render(request, 'result_negative.html', context)
            else:
                # Всякий случай
                output = "Введены данные: Ширина {0}, Высота {1}, Диагональ {2}".format(width, height, diag)

            context = {
                "params": params,
                "output": output,
                "hudata": hudata,
            }
            return render(request, 'result.html', context)

    context = {
        "params": params,
        "count": count,
        "hudata": hudata,
    }
    return render(request, 'index.html', context)


def result(request):
    params = Params
    count = Headunit.object_hu.count()
    hudata = Headunit.object_hu.all()
    if request.method == "POST":
        params = Params(request.POST)
        if params.is_valid():
            width = request.POST.get("width")
            height = request.POST.get("height")
            diag = request.POST.get("diag")
            output = "Ширина: {0}, Высота: {1}, Диагональ: {2}".format(width, height, diag)
            context = {
                "params": params,
                "output": output,
                "hudata": hudata,
            }
            return render(request, 'result.html', context)

    context = {
        "params": params,
        "count": count,
        "hudata": hudata,
    }
    return render(request, "result.html", context)


def result_negative(request):
    return render(request, "result_negative.html")
