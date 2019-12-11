def rotate(arr):
    N = len(arr)
    for i in range(N):
        for j in range(i,N-i-1):
            temp = arr[i][j]
            i_temp = i
            j_temp = j
            for _ in range(4):
                temp1 = arr[j_temp][N-i_temp-1]
                arr[j_temp][N-i_temp-1] = temp
                temp = temp1
                local_var = N-i_temp-1
                i_temp = j_temp
                j_temp = local_var
    return arr

arr = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(arr))