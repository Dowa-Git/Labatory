import Sub1
import Sub2

print(hex(id(Sub1.SingletonManager.TestModule1.TestModule)))
print(hex(id(Sub2.SingletonManager.TestModule1.TestModule)))
print(hex(id(Sub1.SingletonManager.TestModule2.TestModule)))
print(hex(id(Sub2.SingletonManager.TestModule2.TestModule)))

print(Sub1.SingletonManager.TestModule1.TestModule.TestVar1)
Sub1.SingletonManager.TestModule1.TestModule.TestVar1 = 100
print(Sub2.SingletonManager.TestModule1.TestModule.TestVar1)

SubTestModule = Sub1.SingletonManager.TestModule1.TestModule
SubTestModule.TestVar1 = 9

print(hex(id(SubTestModule)))

print(Sub2.SingletonManager.TestModule1.TestModule.TestVar1)

SubTestModuleVar = Sub1.SingletonManager.TestModule1.TestModule.TestVar1
print(hex(id(SubTestModuleVar)))
print(hex(id(Sub1.SingletonManager.TestModule1.TestModule.TestVar1)))
# setattr(SubTestModuleVar, 99)
print(Sub2.SingletonManager.TestModule1.TestModule.__dict__.keys())
print(dir(Sub2.SingletonManager.TestModule1.TestModule))

print(type(SubTestModuleVar))

SubTestModuleVar_Test = id(Sub1.SingletonManager.TestModule1.TestModule.TestVar1)
print(type(SubTestModuleVar_Test))  


import TestPackage.TestModule