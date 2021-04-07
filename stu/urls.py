from django.urls import path

from stu.views_.download import DownloadView
from stu.views_.filecopy import FileCopyView
from stu.views_.filedownload import FileDownView
from stu.views_.filerecords import FileRecordView
from stu.views_.imageView import ImageView
from stu.views_.index import IndexView
# from stu.views_.fileinfo import SensitiveView, TrojanView
# from stu.views_.installapp import InstalledAppView
# from stu.views_.ipvisit import IPVisitView
# from stu.views_.recents import RecentsView
from stu.views_.intellianalysis import AnalysisView
from stu.views_.terminal import TerminalView
from stu.views_.usbconn import UsbConnView
# from stu.views_.usbexchange import UsbExchangeView
from stu.views_.usbhistory import UsbHistoryView
# from stu.views_.winuser import WinUserView

urlpatterns = [
    path('', IndexView.as_view()),
    path('index', IndexView.as_view()),

    # path('fileinfo', SensitiveView.as_view(), name="sensitive"),
    # path('fileinfo/<int:page>', SensitiveView.as_view(), name="sensitive"),
    #
    # path('fileinfo_2', TrojanView.as_view(), name="trojan"),
    # path('fileinfo_2/<int:page>', TrojanView.as_view(), name="trojan"),
    #
    # path("usb_exchange", UsbExchangeView.as_view()),
    # path("usb_exchange/<int:page>", UsbExchangeView.as_view()),
    #
    path("filedownload", FileDownView.as_view()),
    path("filedownload/<int:page>", FileDownView.as_view()),
    path("filedownload/detail/<str:did>", FileDownView.as_view()),
    path("filedownload/detail/<str:did>/<int:page>", FileDownView.as_view()),

    path("filerecords", FileRecordView.as_view()),
    path("filerecords/<int:page>", FileRecordView.as_view()),
    path("filerecords/detail/<str:did>", FileRecordView.as_view()),
    path("filerecords/detail/<str:did>/<int:page>", FileRecordView.as_view()),
    path("filerecords/detail_tag/<str:did>/<int:tag>", FileRecordView.as_view()),
    path("filerecords/detail_tag/<str:did>/<int:tag>/<int:page>", FileRecordView.as_view()),

    path("analysis", AnalysisView.as_view()),
    path("analysis/<int:page>", AnalysisView.as_view()),
    # path("analysis/detail/<str:did>", AnalysisView.as_view()),
    # path("analysis/detail/<str:did>/<int:page>", AnalysisView.as_view()),

    path("terminal", TerminalView.as_view()),
    path("terminal/<int:page>", TerminalView.as_view()),

    #
    # path("ipvisit", IPVisitView.as_view()),
    # path("ipvisit/<int:page>", IPVisitView.as_view()),
    #
    path("usb_conn", UsbConnView.as_view()),
    path("usb_conn/<int:page>", UsbConnView.as_view()),

    path("filecopy", FileCopyView.as_view()),
    path("filecopy/<int:page>", FileCopyView.as_view()),
    path("filecopy/detail/<str:did>", FileCopyView.as_view()),
    path("filecopy/detail/<str:did>/<int:page>", FileCopyView.as_view()),
    #
    # path("installedapp", InstalledAppView.as_view()),
    # path("installedapp/<int:page>", InstalledAppView.as_view()),
    #
    path("usb_history", UsbHistoryView.as_view(), name="usb_history"),
    path("usb_history/<int:page>", UsbHistoryView.as_view()),
    #
    # # path("winuser", WinUserView.as_view()),
    # # path("winuser/<int:page>", WinUserView.as_view()),
    #
    # path("recents", RecentsView.as_view()),
    # path("recents/<int:page>", RecentsView.as_view())

    path("download/<int:tag>/<str:did>/<str:fid>", DownloadView.as_view()),

    path("image/<int:did>/<str:md5>", ImageView.as_view())
]
