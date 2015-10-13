#numnote.py
def numnote(list):
    msg=[]
    for num in list:
        if num <0: 
            s=str(num)+' is negative'
        elif 0<num<=9:
            s=str(num)+' is a digit'
        msg.append(s)
    return msg
