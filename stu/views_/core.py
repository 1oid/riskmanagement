import datetime
from django.http import FileResponse, Http404
import zipfile

from manage.settings import DOWNLOAD_ROOT, BASE_DIR
from manage.wsgi import *
from stu.models import *


def menu():
    return [
                {
                    "name": "智慧分析",
                    "total": str(IntelliAnalysis.objects.all().count()),
                    "current": "analysis",
                    "class": "bg-info",
                    "icon": "mdi-content-paste",
                    "show": 0
                },
                {
                    "name": "文件风控",
                    "total": str(UserFile.objects.all().count()),
                    "current": "filerecords",
                    "class": "bg-cyan",
                    "icon": "mdi-folder",
                    "show": 1,
                    "img": "risk"
                },
                {
                    "name": "文件下载",
                    "total": str(UserBroFile.objects.all().count()),
                    "current": "filedownload",
                    "class": "bg-success",
                    "icon": "mdi-folder-download",
                    "show": 1,
                    "img": "download"
                },
                {
                    "name": "移动存储",
                    "total": str(UserDevAccess.objects.all().count()),
                    "current": "usb_conn",
                    "class": "bg-yellow",
                    "icon": "mdi-usb",
                    "show": 1,
                    "img": "usb"
                },
                {
                    "name": "文件拷贝",
                    "total": str(UserFileCopy.objects.all().count()),
                    "current": "filecopy",
                    "class": "bg-purple",
                    "icon": "mdi-content-copy",
                    "show": 1,
                    "img": "copy"
                },
                {
                    "name": "USB历史",
                    "total": str(UserDevHistory.objects.all().count()),
                    "current": "usb_history",
                    "class": "bg-info",
                    "icon": "mdi-content-paste",
                    "show": 1,
                    "img": "history"
                },
                {
                    "name": "终端管理",
                    "total": str(UserDevHistory.objects.all().count()),
                    "current": "terminal",
                    "class": "bg-info",
                    "icon": "mdi-content-paste",
                    "show": 0
                }
            ]


def pcinfo():
    pc = UserDevice.objects.all().order_by("-id").first()

    if not pc:
        return {
            "id": "0",
            "PcName": "",
            "PcMac": "",
            "PcIp": "",
            "PcOs": "",
            "Location": "",
            "CacheFileTime": "3",
            "IsReportFull": "0",
            "ReportTime": "3",
            "date": "",
            "datetime": ""
        }
    return {
            "id": pc.DId,
            "PcName": pc.DName,
            "PcMac": pc.DMac,
            "PcIp": pc.DIp,
            "PcOs": pc.DSystem,
            "Location": pc.Remarks,
            "CacheFileTime": "3",
            "IsReportFull": "0",
            "ReportTime": "3",
            "date": pc.Other,
            "datetime": pc.Other
        }


def size_format(b):
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


def time_of_interval(start, end):
    print(start, end)

    def format_time(t):
        return datetime.datetime.strptime(str(t), "%Y-%m-%d %H:%M:%S")

    if start.strip() == "" or end.strip() == "":
        return ""

    s = format_time(start)
    e = format_time(end)
    return str(e - s)


def get_computer_name_by_id(did):
    try:
        _object = UserDevice.objects.get(DId=did)
        return _object.DName
    except UserDevice.DoesNotExist as e:
        _object = UserDevice.objects.filter(DId=did).last()

        if _object:
            return _object.DName
        return did


def download_file(_did, _fileid, tag):
    """
    文件下载
    tag:
        1 - 风控
        2 - 下载
        3 - 拷贝
    :param _fileid:
    :return:
    """
    f = CacheFile.objects.filter(identifier=_did, MD5=_fileid).last()

    if not f:
        raise Http404

    if tag == 1:
        name = UserFile.objects.filter(Did=_did, FileMd5=_fileid).last().FileName
    elif tag == 2:
        name = UserBroFile.objects.filter(Did=_did, FileMd5=_fileid).last().FileName
    elif tag == 3:
        name = UserFileCopy.objects.filter(Did=_did, FIleMD5=_fileid).last().FileName
    else:
        name = ""

    name = name.strip().split("\\")[-1]
    # name = UserFile.objects.filter(Did=_did, FileMd5=_fileid).last().FileName
    path = f.SaveName

    if '.zdat' in path:
        zf = zipfile.ZipFile(path)

        file = zf.open(zf.namelist()[0], mode='r', pwd='zdat'.encode('utf-8'))
        # extract_file = zf.namelist()[0]
        # zf.extract(extract_file, os.path.join(BASE_DIR, "downloads"), pwd="zdat".encode("utf-8"))
        # file = open(os.path.join(BASE_DIR, "downloads") + '/' + extract_file, 'rb')
    else:
        file = open(path, 'rb')

    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{}"'.format(name)
    return response


if __name__ == '__main__':
    time_of_interval("2021-03-31 20:19:40", "2021-03-31 20:19:26")
