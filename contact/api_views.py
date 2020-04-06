from django.utils.decorators import method_decorator
from rest_framework import generics
from .serializers import ContactSerializer
from django.views.decorators.csrf import csrf_exempt

from .models import Contact

class ContactAPIView(generics.ListCreateAPIView):
    '''
        Contact 리스트를 보여주거나 생성하는 API

        ---
        # 내용
            - name : 이름
            - email : 이메일
            - phone_no : 전화번호
            - service : 문의유형
            - url : 홈페이지 주소
            - content : 내용
    '''
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ContactAPIView, self).dispatch(request, *args, **kwargs)