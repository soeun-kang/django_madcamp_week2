from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.shortcuts import redirect

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        # 이메일 주소가 제공되지 않는 소셜 계정은 무시
        if not sociallogin.account.user.email:
            return

        # 소셜 계정에 매핑된 사용자가 없을 경우
        if not sociallogin.is_existing:
            # 회원가입 페이지로 리디렉션
            return redirect('account_signup')
