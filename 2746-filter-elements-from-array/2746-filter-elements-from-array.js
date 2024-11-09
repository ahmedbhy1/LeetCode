/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let l = []
    for (i in arr){
        console.log(arr[i]);
        if (fn(arr[i], Number(i))){
            l.push(arr[i]);
        }
    };
    return l;
}