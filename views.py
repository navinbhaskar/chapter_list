from django.http import HttpResponse
from rest_framework.views import APIView
from classcast.classcast_search_fetch.models import chapter


class chapterlist(APIView):
    def get(self, request, standard, subject):
        if not chapter(standard =standard):
                return Response('Standard not found', status= status.HTTP_400_BAD_REQUEST)
        if not chapter(subject =subject):
                return Response('Subject not found', status= status.HTTP_400_BAD_REQUEST)
        if standard=="all":
                chapterlist1 = chapter.objects.filter(subject=subject)
                serializer=chapterlistSerializer(chapterlist1, many=True)
                return Response(serializer.data)
        chapterlist = chapter.objects.filter(standard=standard, subject=subject)
        serializer=chapterlistSerializer(chapterlist, many=True)
        return Response(serializer.data)

    