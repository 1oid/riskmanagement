from django.shortcuts import render
from django.views.generic import View
from stu.models import UserBroFile
from stu.views_.core import menu, pcinfo, size_format
from django.core.paginator import Paginator


class FileDownView(View):

    def get(self, request, page=1, did=None):

        if did is not None:
            objects = UserBroFile.objects.filter(Did=did)
        else:
            objects = UserBroFile.objects.all()

        # count = objects.count()
        p = Paginator(objects, 10)

        """
         <th>序号</th>
                        <th>文件名</th>
                          <th>文件大小</th>
                          <th>文件MD5</th>
                          <th>标签</th>
                        <th>执行程序</th>
                        <th>检测时间</th>
                        """
        obj = {
            "current_page": page,
            "pages": p.num_pages,
            "changePage": "",
            "pageurl": "filedownload",
            "nowIndex": 0,
            "topData": [
                {
                    "id": item.Did,
                    "odid": item.Did,
                    "title": item.FileName.strip().split("\\")[-1] if item.FileName != "" else "",
                    "fileSize": size_format(item.FileSize),
                    "md5": item.FileMd5,
                    "InsterTime": item.Other,
                    "tag": item.sTag,
                    "isdown": 0,
                    "download": item.FileMd5
                } for item in p.page(page)
            ],
            "toptotal": p.count,
            "current_name": "文件下载",
            "current_url": "filedownload",
            "PcInfo": pcinfo(),
            "fenri": [],
            "currentDate": "",
            "menu": menu()
        }
        return render(request, "pages/stFileDownload_Net.html", {"obj": obj})
