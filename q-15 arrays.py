def smallest(number):
    if number<10:
        return 10+number
    else:
        arr = [9,8,7,6,5,4,3,2]
        multiple = []
        i=0
        while(number>1 and i<len(arr)):
            # print("outer loop")
            while(number%arr[i]==0):
                multiple.append(arr[i])
                number = number/arr[i]
            i+=1
        # print(multiple)
        string = ''
        if len(multiple)==0:
            return "Not Possible"
        for i in range(len(multiple)-1,-1,-1):
            # print(multiple[i])
            string = string+str(multiple[i])
        return string


number = 361
print(smallest(number))