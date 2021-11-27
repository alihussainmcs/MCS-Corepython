# Assignment :

Text = """5
dave
laura
owen
vick
amr
dave
180 3
laura
owen
vick
owen
50 1
dave
amr
150 2
vick
owen
laura
360 2
amr
vick
vick
0 0"""

data = Text.strip().split('\n')
# print(data)

data_1 = ['5', 'dave', 'laura', 'owen', 'vick', 'amr', 'dave', '180 3', 'laura', 'owen', 'vick', 'owen', '50 1', 'dave',
          'amr', '150 2', 'vick', 'owen', 'laura', '360 2', 'amr', 'vick', 'vick', '0 0']

# Mathematics
"""        '5', 'dave', 'laura', 'owen', 'vick', 'amr'
dave = 180   ---> 'laura', 'owen', 'vick'
        laura = 60
        owen =  60
        vick =  60
owen = 50    --->  'dave'
        dave = 50
amr = 150    --->  'vick', 'owen'
        vick  = 75
        owen  = 75
laura = 360  --->  'amr', 'vick'
        amr = 180
        vick = 180
vick  = 0  --->  0
"""

"""
# with simple way

# dave  --->
d_v = 180  # 3 owen laura vick
o_v = 50  # 1 dave
a_v = 150  # 2 vick owen
la_v = 360  # 2 amr vick

dave = o_v
owen = d_v/3 + a_v/2
laura = d_v/3
vick = d_v/3 + a_v/2 + la_v/2
amr = la_v/2


print("dave", dave)
print("owen", owen)
print("laura", laura)
print("vick", vick)
print("amr", amr)
'''
output :
dave 50
owen 135.0
laura 60.0
vick 315.0
amr 180.0
'''
"""
print("---------------------------------------------------------------------------------------------")


def final_dist():
    d_v = 180//3  # 3 owen laura vick
    o_v = 50//1  # 1 dave
    a_v = 150//2  # 2 vick owen
    la_v = 360//2  # 2 amr vick
    data_v = ['dave', 'laura', 'owen', 'vick', 'amr']

    dave_d = ['laura', 'owen', 'vick']
    owen_d = ['dave']
    amr_d = ['vick', 'owen']
    laura_d = ['amr', 'vick']

    dave = 0
    owen = 0
    laura = 0
    vick = 0
    amr = 0
    count = 0
    for i in data_v:
        if i in dave_d:
            if count == 1:
                laura += d_v
                owen += d_v
                vick += d_v
                break
        if i in owen_d:
            if count == 1:
                dave += o_v
                break
        if i in amr_d:
            owen += a_v
            vick += a_v
        if i in laura_d:
            vick += la_v
            amr += la_v

    print(dave)
    print(owen)
    print(laura)
    print(vick)
    print(amr)


final_dist()
