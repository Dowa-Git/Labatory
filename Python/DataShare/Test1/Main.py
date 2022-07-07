import SubModule
import SubModule2

print(f'All NameSpace : {dir()}')
print(f'SubModule NameSpace : {dir(SubModule)}')
print(f'SubModule2 NameSpace : {dir(SubModule2)}')

SubModule.ClassRef.PrintAll()
SubModule.ClassRef.SetA(100)
SubModule.ClassRef.PrintA()
SubModule.ClassRef.PrintAll()


SubModule2.PrintTestVar2()
SubModule2.Testvar2 = 'No longer Test2Var'
# SubModule2.
SubModule2.PrintTestVar2()