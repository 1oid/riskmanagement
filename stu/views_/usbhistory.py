from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator
from stu.models import UserDevHistory
from stu.views_.core import menu, pcinfo


class UsbHistoryView(View):

    def get(self, request, page=1):
        objects = UserDevHistory.objects.all()
        # count = objects.count()
        p = Paginator(objects, 10)


        """
         <th>序号</th>
                        <th>设备名称</th>
                        <th>设备序列号</th>
                        <th>设备使用时间</th>
                        <th>设备类型</th>
                    """

        obj = {
            "current_page": page,
            "pages": p.num_pages,
            "changePage": "",
            "pageurl": "usb_history",
            "nowIndex": 0,
            "topData": [
                {
                    "id": item.id,
                    "dname": item.DName,
                    "snumber": item.SNumber,
                    "usetime": item.UseTime,
                    "dtype": item.DType,
                    "InsterTime": item.Other
                } for item in p.page(page)
            ],
            "toptotal": p.count,
            "current_name": "USB历史",
            "current_url": "usb_history",
            "PcInfo": pcinfo(),
            "fenri": [
                {
                    "InsterTime": "2021-02-12"
                }
            ],
            "currentDate": "",
            "menu": menu()
        }
        return render(request, "pages/stu_UsbHistory.html", {"obj": obj})
