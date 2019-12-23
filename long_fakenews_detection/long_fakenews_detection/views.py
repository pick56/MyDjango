from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
import json
import pytz
from datetime import datetime

from django.views import generic

def index(request):
    # print("hello world")
    # 第一个参数是请求对象，第二个参数是模板名，第三个可选参数是字典。它返回使用给定上下文呈现的给定模板的HttpResponse对象。
    return render(request, 'long_fakenews_detection/index.html')

def detail(request, txt_id):
    print("show detail", txt_id)
    # 第一个参数是请求对象，第二个参数是模板名，第三个可选参数是字典。它返回使用给定上下文呈现的给定模板的HttpResponse对象。
    return render(request, 'long_fakenews_detection/detail.html')
    # video = VideoDetection.objects.get(video_id=video_id)
    # return render(request, 'videodetection/detail.html', {'video': video})

def check_txt(request):
    print("检测文本")
    rawcontent = request.POST.get('content')
    print(rawcontent)
    # print("real or not")
    # 将路径保存到数据库中。
    tz = pytz.timezone('Asia/Shanghai')
    t = datetime.now(tz)
    timestamp = t.strftime('%Y-%m-%d %H:%M:%S')
    txt_id = t.strftime('%Y%m%d%H%M%S')
    # video = VideoDetection(video_id=video_id)
    # video.rawvideopath = rawvideopath
    # video.newvideopath = newvideopath
    # video.rawvideocoverpath = frame_path1
    # video.newvideocoverpath = frame_path2
    # video.info = info
    # video.timeStamp = timestamp
    # video.save()

    result = []
    result.append(txt_id)
    # print(result)
    return JsonResponse(json.dumps(result), content_type='application/json', safe=False)


