
#goal
# 8,8,8,7, 9,9,8 => 3,8,1,7,2,9,1,8


def count(nums):
    print("input: "+str(nums))
    dict={}
    start=0

    prev = None

    result=[]


    while (start <= len(nums)-1):
        counter = 0

        #start with an index that changes
        key=nums[start]

        #start another loop to compare next values

        for idx in range(0, len(nums)-1):

            curr=start+counter #makes sure we are starting from the right index

            if curr>len(nums)-1:
                result.append(counter)
                result.append(key)
                #end of list exceeded
                return result

            elif key == nums[curr]:
                counter+=1
                continue
                #continue iteration

            else:
                result.append(counter)
                result.append(key)
                start=curr
                break
    return result


print("output: "+str(count([8,8,8,8,8,7,9,9,8,5,5,5,7,7,7])))
