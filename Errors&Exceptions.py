def exception1():
    while(True):
        try:
            n=float(input("Introduce un número: "))
            m=4
            print("{}/{}={}".format(n,m,n/m))
        except:
            print("Introduce bien el número")
        else:
            print("Todo correcto")
            break #Romper iteración si ok
        finally:
            print("Fin iteración")
def exception2():
    while (True):
        try:
            n = float(input("Introduce un número: "))
            m = 4
            m/n
        except ValueError:
            raise ValueError("No se puede dividir un número por una cadena")
        except ZeroDivisionError:
            print("El resultado es indeterminado")
        except Exception as e:
            print(type(e).__name__)
        else:
            print("Todo correcto")
            break  # Romper iteración si ok
        finally:
            print("Fin iteración")

exception2()