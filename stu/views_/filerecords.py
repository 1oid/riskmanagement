from django.db.models import Q
from django.shortcuts import render
from django.views.generic import View
from stu.models import UserFile, CacheFile
from stu.views_.core import menu, pcinfo
from django.core.paginator import Paginator


class FileRecordView(View):

    """
    通过identifier、md5进行文件关联
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

    def get(self, request, page=1, did=None, tag=None):
        if did is not None:
            if tag is None:
                objects = UserFile.objects.filter(Did=did)
            else:
                objects = UserFile.objects.filter(Did=did, FileTag=tag)
        else:
            objects = UserFile.objects.all()

        results = []
        name_set = []

        for item in objects:
            cache_list = []
            cache_all_count = 0

            if str(item.FileName) in name_set:
                continue

            name_set.append(str(item.FileName))

            try:
                cache_all = CacheFile.objects.filter(identifier=item.Did, MD5=item.FileMd5, IsImge=1).order_by("-IsImge")
                cache_one = cache_all.filter(CacheName=item.FileName).first()

                cache_set = []

                for cache_item in cache_all:

                    if "/image/{}/{}".format(cache_item.identifier, cache_item.MD5) in cache_set:
                        continue

                    cache_set.append("/image/{}/{}".format(cache_item.identifier, cache_item.MD5))

                    cache_all_count += 1
                    cache_list.append({
                        "id": cache_item.id,
                        "cache_name": cache_item.CacheName,
                        "save_name": "/image/{}/{}".format(cache_item.identifier, cache_item.MD5),
                        "is_img": cache_item.IsImge,
                        "filename": item.FileName,
                    })

            except CacheFile.DoesNotExist:
                continue

            results.append({
                "id": item.id,
                "odid": item.Did,
                "filename": item.FileName.split("\\")[-1],
                "filesize": self.size_format(item.FileSize),
                "remark": item.ContentRemark[:40],
                "keyword": item.KeyDesc,
                "md5": item.FileMd5,
                "filetype": item.FileType,
                "cache_one": {
                    "filename": item.FileName,
                    "cache": cache_one.CacheName if cache_one else "",
                    "path": cache_one.SaveName.split("\\")[-1] if cache_one else "",
                    "is_img": cache_one.IsImge if cache_one else ""
                } if cache_one else 0,
                "cache_all": cache_list,
                "cache_all_count": cache_all_count,
                "Other": item.Other
            })

        # count = objects.count()
        p = Paginator(results, 10)

        obj = {
            "current_page": page,
            "pages": p.num_pages,
            "changePage": "",
            "pageurl": "filerecords/detail/" + did if did else "filerecords",
            "nowIndex": 0,
            "topData": list(p.page(page)),
            "toptotal": p.count,
            "current_name": "文件风控",
            "current_url": "filerecords/detail/" + did if did else "filerecords",
            "PcInfo": pcinfo(),
            "fenri": [],
            "currentDate": "",
            "menu": menu()
        }
        return render(request, "pages/stu_filerecords.html", {"obj": obj})
