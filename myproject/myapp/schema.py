import graphene
from graphene_django.types import DjangoObjectType
from myapp.models import Account

class AccountType(DjangoObjectType):
    class Meta:
        model = Account

class Query:
    account= graphene.Field(AccountType, id=graphene.Int())
    all_accounts = graphene.List(AccountType)
   
    def resolve_account(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Account.objects.get(pk=id)
        return None
    
    def resolve_all_accounts(self, info, **kwargs):
        return Account.objects.all()
