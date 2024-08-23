print("NAV++")
q = input("")
def code():
    if q == "write:":
        w = input("write:")
        print(w)
    elif q == "createvar:":
        var = input("enter the value of variable:")
        m_var = var
        e = input("variable created.print it ? :")
        if e == "y":
            print(m_var)
        else:
            return code()
    elif q == "about:" or q == "about":
        print("nav++ made by navinderjeet singh.maded using python.")
    else:
        print("code not found")
code()
input("exit ?:")
