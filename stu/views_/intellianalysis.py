from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator
from stu.models import IntelliAnalysis, UserBroFile, UserFile, UserNetWork, UserFileCopy
from stu.views_.core import menu, pcinfo, get_computer_name_by_id


class AnalysisView(View):

    """
    通过 UserFile 的fileTag找到对象的MD5
    之后与

    先从 UserBroFile 获取文件，通过md5再从UserFile中找，确认是否此下载文件是否有标记
    """

    def size_format(self, b):
        if b < 1000:
            return '%i' % b + 'B'
        elif 1000 <= b < 1000000:
            return '%.1f' % float(b / 1000) + 'KB'
        elif 1000000 <= b < 1000000000:
            return '%.1f' % float(b / 1000000) + 'MB'
        elif 1000000000 <= b < 1000000000000:
            return '%.1f' % float(b / 1000000000) + 'GB'
        elif 1000000000000 <= b:
            return '%.1f' % float(b / 1000000000000) + 'TB'

    def __get_print(self):
        """
        获取对应打印记录
        :return:
        """
        pass

    def __get_download(self):
        """
        获取下载
        :return:
        """
        pass

    def __get_network(selfa):
        """
        获取外发
        :return:
        """
        pass

    def get(self, request, page=1):
        objects = IntelliAnalysis.objects.all()

        # count = objects.count()
        p = Paginator(objects, 10)

        obj = {
            "current_page": page,
            "pages": p.num_pages,
            "changePage": "",
            "pageurl": "analysis",
            "nowIndex": 0,
            "topData": [
                {
                    "id": item.id,
                    "did": get_computer_name_by_id(item.did),
                    "odid": item.did,
                    "filename": item.filename.split("\\")[-1],
                    "filepath": item.filename,
                    "filesize": self.size_format(item.filesize),
                    "md5": item.md5,
                    "description": item.description,
                    "duplicate": 1 if item.duplicate else 0,
                    "action": item.get_action_string(),
                    "other": item.Other.strftime("%Y-%m-%d %H:%I:%S")
                } for item in objects
            ],
            "toptotal": p.count,
            "current_name": "智慧分析",
            "current_url": "analysis",
            "PcInfo": pcinfo(),
            "fenri": [],
            "currentDate": "",
            "menu": menu()
        }
        return render(request, "pages/stu_filereanalysis.html", {"obj": obj})
