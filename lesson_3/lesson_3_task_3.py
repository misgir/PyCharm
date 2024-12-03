from Address import Address
from Mailing import Mailing


to_address = Address(101111, "Moscow", "Arbat", 3, 1)
from_address = Address(101111, "Moscow", "Arbat", 8, 2)

mailing = Mailing(to_address, from_address, 100, "372838jhg")

print(mailing)
