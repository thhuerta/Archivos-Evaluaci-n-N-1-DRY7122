acl = int(input("ingrese el numero de su ACL? "))
if acl >= 1 and acl <= 99:
    print(" ")
    print("Este numero corresponde a una ACL IPv4 estándar.")
elif acl >=100 and acl <= 199:
    print(" ")
    print("Este numero corresponde a una ACL IPv4 extendida")
else:
    print("no corresponde a una ACL IPv4 extendida o estandar")
