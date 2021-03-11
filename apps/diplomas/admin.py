#from django.contrib import admin
from apps.core.admin import OPEN_DIPLOMAS_ADMIN_SITE
from apps.diplomas.models import Issuer
from apps.diplomas.admins.issuers import IssuerAdmin


OPEN_DIPLOMAS_ADMIN_SITE.register(Issuer, IssuerAdmin)