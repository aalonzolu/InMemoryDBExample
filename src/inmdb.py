from typing import Union, Optional
from collections import Counter
from functools import reduce

from src.constants import VALID_TYPES, VALID_TYPES_UNION, NoTransaction


class InMDB:
    def __init__(self):
        self._db = {}
        self._transactions = []

    def _transaction_open(self):
        return len(self._transactions)

    def _current_transaction(self):
        if self._transaction_open():
            return self._transactions[-1]
        else:
            return self.db

    def _set(self, name: str, value: VALID_TYPES_UNION):
        if self._transaction_open():
            self._transactions[-1][name] = value
        else:
            self._db[name] = value

    def set(self, name: str, value: VALID_TYPES_UNION) -> None:
        self._set(name, value)

    def _get(self, name: str) -> Optional[VALID_TYPES_UNION]:
        if self._transaction_open():
            transaction_values = reduce(lambda a, b: {**a, **b}, self._transactions)  # merge all transactionss
            values = {**self._db, **transaction_values}  # search values stored in db and all open transaction
        else:
            values = self._db
        try:
            return values[name]
        except KeyError:
            return None

    def get(self, name: str) -> VALID_TYPES_UNION:
        return self._get(name)

    def _unset(self, name: str):
        if self._transaction_open():
            self._transactions[-1][name] = None
        else:
            del self._db[name]

    def unset(self, name: str) -> None:
        return self._unset(name)

    def numequalto(self, value: VALID_TYPES_UNION):
        if self._transaction_open():
            transaction_values = reduce(lambda a, b: {**a, **b}, self._transactions)  # merge all transactionss
            values = {**self._db, **transaction_values}  # search values stored in db and all open transaction
        else:
            values = self._db
        try:
            return list(values.values()).count(value)
        except KeyError:
            return 0

    def commit(self):
        if self._transaction_open() and self._transaction_open() > 1:
            self._transactions[-2] = {**self._transactions[-2], **self._transactions[-1]}
        elif self._transaction_open():
            self._db = {**self._db, **self._transactions[-1]}

    def rollback(self):
        if self._transaction_open():
            self._transactions.pop()
        else:
            raise NoTransaction

    def begin(self):
        self._transactions.append({})
