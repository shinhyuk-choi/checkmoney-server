from rest_framework.exceptions import NotFound

from cashbook.models import CashBook


class CashBookService:
    def create(self, user, validated_data):
        cashbook = CashBook.objects.create(user=user, **validated_data)
        return cashbook

    def list(self, user):
        cashbooks = CashBook.objects.filter(user=user)
        return cashbooks

    def update(self, user, cashbook_id, validated_data):
        try:
            cashbook = CashBook.objects.get(user=user, id=cashbook_id)
        except CashBook.DoesNotExist:
            raise NotFound(detail=f"User does not have Cashbook: (id:{cashbook_id})")
        name = validated_data.get('name')
        cashbook.name = name
        cashbook.save()
        return cashbook

    def delete(self, user, cashbook_id):
        try:
            cashbook = CashBook.objects.get(user=user, id=cashbook_id)
        except CashBook.DoesNotExist:
            raise NotFound(detail=f"User does not have Cashbook: (id:{cashbook_id})")
        cashbook.delete()
        return cashbook
