from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator
from stu.models import UserDevAccess
from stu.views_.core import menu, pcinfo, size_format, time_of_interval, get_computer_name_by_id


class UsbConnView(View):

    def get(self, request, page=1):
        objects = UserDevAccess.objects.all()
        # count = objects.count()
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
            "pageurl": "usb_conn",
            "nowIndex": 0,
            "topData": [
                {
                    "id": get_computer_name_by_id(item.Did),
                    "vname": item.VName,
                    "dname": item.DName,
                    "snumber": item.SNumber,
                    "dsize": size_format(item.DSize),
                    "daction": item.DAction,
                    "ctime": item.Ctime,
                    "dtime": item.Dtime,
                    "dtype": item.DType,
                    "InsterTime": item.Other,
                    "interval": time_of_interval(item.Ctime, item.Dtime)
                } for item in p.page(page)
            ],
            "toptotal": p.count,
            "current_name": "移动存储",
            "current_url": "usb_conn",
            "PcInfo": pcinfo(),
            "fenri": [],
            "currentDate": "",
            "menu": menu()
        }
        return render(request, "pages/stu_usb_conn.html", {"obj": obj})
