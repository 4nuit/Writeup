# flag chiffré
crypt_flag = "oz]{R]3l]]B#50es6O4tL23Etr3c10_F4TD2"

# attribut length de la classe java
length = 6

# fonction de tri
def takeSecond(elem):
    return elem[1]

# reverse de encrypt
def decrypt(array:list, mod:int):
    for i in range(0, length*2):
        array[i] = chr(ord(array[i]) ^ mod)
    tab1 = []
    tab2 = []
    for i in range(0,2*length,2):
        tab1.append(array[i])
        tab2.append(array[i+1])
    tab1.reverse()
    tab1.extend(tab2)
    
    return tab1

# reverse de getArray
def revGetArray(arr:list, n1:list, n2:list):
    arr1 = arr[0:length-1]
    arr2 = arr[length: 2*length-1]
    arr2.reverse()
    return [[arr1, n1], [arr2, n2]]

# reverse de Transform
def revTransform(mat:list):
    flag = ""
    for i in mat:
        flag += "".join(i)
    return flag

def revSolve():

    # division du flag chiffré en 3
    len_crypt = len(crypt_flag)//3
    part1 = [*crypt_flag[0:len_crypt]]
    part2 = [*crypt_flag[len_crypt: 2*len_crypt]]
    part3 = [*crypt_flag[2*len_crypt:3*len_crypt]]

    # reverse de encrypt + getArray
    pt1 = revGetArray(decrypt(part1, 2), 0, 5)
    pt2 = revGetArray(decrypt(part2, 1), 1, 4)
    pt3 = revGetArray(decrypt(part3, 0), 2, 3)

    # tri des lignes pour se retrouver la matrice originelle
    pt = [*pt1, *pt2, *pt3]
    pt.sort(key=takeSecond)
    pt = list(list(zip(*pt))[0])

    # rotation de la matrice -90° (reverse de solve)
    arr_flag = list(zip(*pt))[::-1]
    arr_flag = [list(elt) for elt in arr_flag]

    # afficher le flag
    print("SEKAI{" + revTransform(arr_flag) + "}")

revSolve() 
