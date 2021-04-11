import json
import psutil
from django.shortcuts import render
from django.views.generic import View
from stu.views_.core import menu, pcinfo
from stu.models import UserFile, UserFileCopy, UserBroFile, UserNetWork, UserDevHistory, UserDevAccess, IntelliAnalysis
from django.db.models import Sum, Count


class IndexView(View):

    def __statistics(self):
        """
        统计
        打印文件(总数)
        风险文件(总数)
        文件拷贝(总数)
        文件下载(总数)
        外发文件(总数)

        文件占比 所有文件之和
        :return:
        """
        files_print = UserFile.objects.filter(FileTag=4).count()
        files_risk = UserFile.objects.filter(FileType=1).count()
        files_copy = UserFileCopy.objects.all().count()
        files_download = UserBroFile.objects.all().count()
        files_network = UserNetWork.objects.all().count()

        total = files_print + files_risk + files_download + files_network + files_copy

        return {
            "type": 'pie',
            "data": {
                "labels": ["打印文件", "风险文件", "文件拷贝", "文件下载", "外发文件"],
                "datasets": [{
                    "data": [files_print, files_risk, files_copy, files_download, files_network],
                    "backgroundColor": ['#ff6384', '#57c7d4', '#15c378', '#fcc525', '#926dde', '#48b0f7']
                }]
            },
            "options": {
                "responsive": 0
            }
        }

    def __risk_statistics(self):
        """
        文件风控统计
        :return:
         风险、木马、重复、打印、伪装
        """
        warning = UserFile.objects.filter(FileTag=1).count()
        troj = UserFile.objects.filter(FileTag=2).count()
        repeat = UserFile.objects.filter(FileTag=3).count()
        _print = UserFile.objects.filter(FileTag=4).count()
        fake = UserFile.objects.filter(FileTag=6).count()

        total = warning + troj + repeat + _print + fake
        if total == 0:
            return [
                {"number": 0, "total": 0, "string": "风险文件", "percent": 0, "class": "yellow"},
                {"number": 0, "total": 0, "string": "木马", "percent": 0, "class": "red"},
                {"number": 0, "total": 0, "string": "重复", "percent": 0, "class": "blue"},
                {"number": 0, "total": 0, "string": "打印", "percent": 0, "class": "gray"},
                {"number": 0, "total": 0, "string": "伪装", "percent": 0, "class": "purple"},
            ]

        return [
            {"number": warning, "total": total, "string": "风险文件", "percent": round(warning / total * 100, 2),
             "class": "yellow"},
            {"number": troj, "total": total, "string": "木马", "percent": round(troj / total * 100, 2), "class": "red"},
            {"number": repeat, "total": total, "string": "重复", "percent": round(repeat / total * 100, 2),
             "class": "blue"},
            {"number": _print, "total": total, "string": "打印", "percent": round(_print / total * 100, 2),
             "class": "gray"},
            {"number": fake, "total": total, "string": "伪装", "percent": round(fake / total * 100, 2),
             "class": "purple"},
        ]

    def __usb_statistics(self):
        """
        usb插拔
        根据时间做统计
        :return:
        """
        objects = UserDevAccess.objects.all().order_by("-Ctime")
        results = {}
        _ = []

        for item in objects:
            if item.Ctime.strip() == "":
                continue

            _time = item.Ctime[:10]
            if item.Ctime not in _:
                results[_time] = 0
                _.append(_time)

            results[_time] += 1

        return {
            "dateDataset": list(results.keys())[:5],
            "valueDataset": list(results.values())[:5]
        }

    def __usb_history(self):
        """
        USB历史
        :return:
        """
        objects = UserDevHistory.objects.all().order_by("-UseTime")[:5]
        return [
            {"name": item.DName, "time": item.UseTime} for item in objects
        ]

    def __system_statistics(self):
        """
        系统性能统计
        :return:
        """
        phymem = psutil.virtual_memory()

        _cpu = psutil.cpu_percent(0)
        _mem_used = phymem.percent
        return {
            "cpu": _cpu,
            "mem": _mem_used
        }

    def analysis_statistics(self):
        """
        智慧分析统计
        :return:
        """
        objects = IntelliAnalysis.objects.values("action").annotate(counts=Count("action"))
        results_for_name = []
        results_for_count = []

        for result in objects:
            results_for_name.append(IntelliAnalysis.action_choice[result['action']][1])
            results_for_count.append(result['counts'])
        return {
            "name": results_for_name,
            "count": results_for_count
        }

    def get(self, request):
        self.analysis_statistics()
        obj = {
            "foo": "报告概况",
            "current": "报告概况",
            "width": 100,
            "height": 100,
            "menu": menu(),
            "PcInfo": pcinfo(),
            "riskFiles": [],
            "risk_statistics": self.__risk_statistics(),
            "usb_history": self.__usb_history(),

        }
        return render(request, "index.html", {
            "obj": obj,
            "statistics": self.__statistics(),
            "system_statistics": self.__system_statistics(),
            "usb_statistics": self.__usb_statistics(),
            "analysis_statistics": self.analysis_statistics()
        })
