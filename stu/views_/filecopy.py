from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator
from stu.models import UserFileCopy
from stu.views_.core import menu, pcinfo, size_format, get_computer_name_by_id


class FileCopyView(View):

    def get(self, request, page=1, did=None):
        if did is not None:
            objects = UserFileCopy.objects.filter(Did=did)
        else:
            objects = UserFileCopy.objects.all()
        # count = objects.count()
        p = Paginator(objects, 10)

        """
        <tr>
                        <th>序号</th>
                        <th>设备卷名</th>
                        <th>设备名称</th>
                        <th>拷入/拷出</th>
                          <th>文件名</th>
                          <th>大小</th>
                          <th>MD5</th>
                          <th>文件属性</th>
                        <th>操作时间</th>
                      </tr>
                      """
        obj = {
            "current_page": page,
            "pages": p.num_pages,
            "changePage": "",
            "pageurl": "filecopy",
            "nowIndex": 0,
            "topData": [
                {
                    "id": get_computer_name_by_id(item.Did),
                    "odid": item.Did,
                    "vname": item.VName,
                    "dname": item.DName,
                    "action": item.Action,
                    "filename": item.FileName,
                    "atime": item.ATime,
                    "filesize": size_format(item.FileSize),
                    "md5": item.FIleMD5,
                    "attribute": item.FileAttribute
                } for item in p.page(page)
            ],
            "toptotal": p.count,
            "current_name": "文件拷贝",
            "current_url": "filecopy",
            "PcInfo": pcinfo(),
            "fenri": [],
            "currentDate": "",
            "menu": menu()
        }
        return render(request, "pages/stu_filecopy.html", {"obj": obj})
