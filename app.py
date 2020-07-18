# FR: The procedure used below to import a module in Python is similar to 'using namespace' in C#
from ecommerce.shopping import salesModule

sale = salesModule.Sale()

# To see information related to salesModule
#print(dir(salesModule))

# full name of module
print(salesModule.__name__)

# name of package containing the module
print(salesModule.__package__)

# address of the module file
print(salesModule.__file__)


