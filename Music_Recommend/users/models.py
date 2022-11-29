from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):

        if not email:
            raise ValueError('이메일 작성해주세요.')

        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password=None):

        user = self.create_user(
            email,
            password=password,
            nickname=nickname,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        error_messages={'unique': "이미 존재하는 이메일 주소입니다."}   
    )
    nickname = models.CharField(max_length=15, unique=True, error_messages={'unique': "이미 존재하는 닉네임입니다."})
    profile_image = models.ImageField(default="default_profile_pic.jpg",upload_to="profile_pics" )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
