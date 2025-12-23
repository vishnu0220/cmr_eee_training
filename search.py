def searchElement(l, tar):
    for i in l:
        if i == tar:
            return True
    return False

l = [10, 20, 30, 40, 50]
tar = 50 # You can enter whatever you want as a target element

found = searchElement(l , tar)
if(found):
    print("Target element found in the list")
else:
    print("Target element not found in the list")