class ExceptionHandling:
    def __init__(self):
        pass
    def check_exception_handling(self):
        print("Inside check_exception_handling")
        a=8
        b=0
        try:
            print(a/b)
        except ZeroDivisionError as ze:
            print("Exception caught",ze)
        except Exception as ex:
            print("Exception caught",ex)
        finally:
            print("Inside finally clause")

def main():
    obj=ExceptionHandling()
    obj.check_exception_handling()
main()