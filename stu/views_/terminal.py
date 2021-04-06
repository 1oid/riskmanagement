from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator
from stu.models import IntelliAnalysis, UserDevice, UserFileCopy, UserFile
from stu.views_.core import menu, pcinfo
from django.db.models import Q


class TerminalView(View):
    """
    一条记录一个机器信息，机器名，IP，MAC，备注，
    文件风控（计数）
    文件拷贝（计数）...
    点这个计数就可以看到这个机器的对应的记录数
    """
    def get(self, request, page=1):
        objects = UserDevice.objects.all()
        results = []

        for item in objects:
            if item.DId.strip() == "":
                continue

            relationDidsWithUserFileCopy = UserFileCopy.objects.filter(Did=item.DId).count()
            relationDidsWithUserFile = UserFile.objects.filter(Did=item.DId).count()

            results.append({
                "info": {
                    "did": item.DId,
                    "name": item.DName,
                    "ip": item.DIp,
                    "mac": item.DMac,
                    "remark": item.Remarks
                },
                "count": {
                    "risk": relationDidsWithUserFile,
                    "copy": relationDidsWithUserFileCopy
                }
            })

        p = Paginator(objects, 10)

        """
        <tr>
                        <th>序号</th>
                        <th>设备卷名</th>
                        <th>设备大小</th>
                        <th>设备序列号</th>
                        <th>插拔状态</th>
                        <th>插入时间</th>
                        <th>拔出时间</th>
                          <th>类别</th>
                      </tr>
                    """
        obj = {
            "current_page": page,
            "pages": p.num_pages,
            "changePage": "",
            "pageurl": "analysis",
            "nowIndex": 0,
            "topData": results,
            "toptotal": p.count,
            "current_name": "终端管理",
            "current_url": "terminal",
            "PcInfo": pcinfo(),
            "fenri": [],
            "currentDate": "",
            "menu": menu()
        }
        return render(request, "pages/stu_terminal.html", {"obj": obj})
