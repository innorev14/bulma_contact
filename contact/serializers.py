from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = Contact
        fields = '__all__'