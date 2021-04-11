from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator
from stu.models import IntelliAnalysis, UserBroFile, UserFile, UserNetWork, UserFileCopy, CacheFile
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

    def get(self, request, page=1, did=None):
        objects = IntelliAnalysis.objects.all()
        results = []

        # 过滤重复名字
        item_sets = {}
        reply_objects = []
        not_reply_objects = []          # 用来保存不重复的元素

        for item in objects:
            _filename = item.filename.strip().split("\\")[-1].strip()

            if item_sets.get(_filename, None):
                item_sets.get(_filename).append(item)
                continue

            item_sets[_filename] = [item]

        for _, values in item_sets.items():
            cache_list = []
            first_item = {}
            cache_count = 0
            cache_set = []
            
            for index, value in enumerate(values):

                _cache = CacheFile.objects.filter(identifier=value.did, MD5=value.md5, IsImge=1).last()

                if index == 0:
                    first_item = {
                        "id": value.id,
                        "odid": get_computer_name_by_id(value.did),
                        "did": value.did,
                        "filename": value.filename.split("\\")[-1],
                        "filesize": self.size_format(value.filesize),
                        "remark": value.description[:40],
                        "md5": value.md5,
                        "cache_one": 0,
                        "cache_all": [],
                        "action": value.get_action_string(),
                        "cache_all_count": 0,
                        "other": value.Other.strftime("%Y-%m-%d %H:%M:%S")
                    }

                if _cache:
                    
                    if str(value.filename) + str(value.md5) in cache_set:
                        pass
                    else:
                        first_item['cache_all_count'] = first_item['cache_all_count'] + 1
                    
                        cache_set.append(str(value.filename) + str(value.md5))
                        print(cache_set)
                        
                        cache_list.append({
                                "id": _cache.id,
                                "cache_name": _cache.CacheName,
                                "save_name": "/image/{}/{}".format(_cache.identifier, _cache.MD5),
                                "is_img": _cache.IsImge,
                                "filename": value.filename,
                                "other": value.Other.strftime("%Y-%m-%d %H:%M:%S")
                            })

                # print(len(values), index + 1)
                if len(values) == index + 1 or len(values) == 1:
                    first_item['cache_all'] = cache_list
                    results.append(first_item)

        # count = objects.count()
        # results = []
        # result_set = []
        #
        # for item in objects:
        #     # 拒绝重复
        #     _ = "{}_{}".format(item.md5, item.action)
        #
        #     if _ in result_set:
        #         continue
        #
        #     result_set.append(_)
        #     _cache = CacheFile.objects.filter(identifier=item.did, MD5=item.md5, IsImge=1).last()
        #
        #     print(_cache)
        #     results.append({
        #             "id": item.id,
        #             "did": get_computer_name_by_id(item.did),
        #             "odid": item.did,
        #             "filename": item.filename.split("\\")[-1],
        #             "filepath": item.filename,
        #             "filesize": self.size_format(item.filesize),
        #             "md5": item.md5,
        #             "description": item.description,
        #             "duplicate": 1 if item.duplicate else 0,
        #             "action": item.get_action_string(),
        #             "other": item.Other.strftime("%Y-%m-%d %H:%I:%S"),
        #             "is_img": _cache.IsImge if _cache else 0,
        #             "save_name": "/image/{}/{}".format(_cache.identifier, _cache.MD5) if _cache else ""
        #         })

        p = Paginator(results, 10)
        obj = {
            "current_page": page,
            "pages": p.num_pages,
            "changePage": "",
            "pageurl": "analysis",
            "nowIndex": 0,
            "topData": results,
            "toptotal": p.count,
            "current_name": "智慧分析",
            "current_url": "analysis",
            "PcInfo": pcinfo(),
            "fenri": [],
            "currentDate": "",
            "menu": menu()
        }
        return render(request, "pages/stu_filereanalysis.html", {"obj": obj})
