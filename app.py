# FR: The procedure used below to import a module in Python is similar to 'using namespace' in C#
from ecommerce.shopping import salesModule
import sys

sale = salesModule.Sale()

print(sale.madeBy)
