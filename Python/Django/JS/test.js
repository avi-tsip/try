function solution(X, Y, A) {
    var N = A.length;
    var result = -1;
    var nX = 0;
    var nY = 0;
    for (var i = 0; i < N; i++) {
        if (A[i] == X) 
            nX += 1;
        else if (A[i] == Y) 
            nY += 1;
        if (nX == nY)
            result = i;
    }
    return result;
}

console.log(solution(1, 2, [9, 0, 1, 2, 1, 2, 1, 4, 1, 2,2, 0, 1]));

