from django.views.generic import View
from django.http import Http404
from stu.views_.core import download_file


class DownloadView(View):

    def get(self, request, fid=None, did=None, tag=None):
        if fid is None or not did or not tag:
            raise Http404("Not Found")

        return download_file(_fileid=fid, _did=did, tag=tag)
