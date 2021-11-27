# print("ModuleNotFoundError: ")
# import ali as a ModuleNotFoundError: No module named 'ali'

try:
    import ali as a
except ModuleNotFoundError as m:
    print(m)

# from package import thing  #ModuleNotFoundError: No module named 'package'
print("-------------------------------------------------")


def import_error():
    try:
        import MCS
    except ModuleNotFoundError as m:
        print(m)


import_error()
