from django.http import HttpResponse, Http404
from django.views.generic import View

from stu.models import CacheFile
from stu.views_.core import image_gener


class ImageView(View):

    def get(self, request, did=None, md5=None):
        if not did or not md5:
            raise Http404()

        _objects = CacheFile.objects.filter(identifier=did, MD5=md5, IsImge=1).last()
        _image = image_gener(_objects.SaveName)
        return HttpResponse(_image, content_type='image/jpg')

