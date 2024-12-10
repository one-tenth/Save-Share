from django import forms
from django.core.validators import RegexValidator

class PhoneForm(forms.Form):
    username = forms.CharField(
        max_length=150,  # 通常用戶名可以更長
        required=True,
        label="用戶名",
        error_messages={
            'required': '寶寶你沒打名字喔~'
        }
    )
    email = forms.EmailField(
        max_length=254,  # 電子郵件的標準長度限制
        required=True,
        label="電子郵件"
    )
    password = forms.CharField(
        max_length=128,  # Django 默認的密碼最大長度
        widget=forms.PasswordInput,  # 使用密碼輸入類型
        required=True,
        label="密碼"
    )
    confirm_password = forms.CharField(
        max_length=128,
        widget=forms.PasswordInput,
        required=False,
        label="確認密碼"
    )
    phone = forms.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^09\d{8}$',
                message="親親您輸入錯了，請輸入有效的台灣電話號碼 (09開頭的10位數字)"
            )
        ],
        required=True,
        label="電話號碼"
    )
#這裡我不太懂哈哈哈
    def clean(self):
        """
        自定義驗證方法，用於檢查密碼是否一致。
        """
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("密碼和確認密碼不一致，請重新輸入。")
        return cleaned_data
