import enum

class TransactionType(str, enum.Enum):
    IN = "IN"
    OUT = "OUT"
