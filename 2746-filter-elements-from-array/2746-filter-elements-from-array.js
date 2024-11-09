/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let l = []
    for (i=0;i<arr.length;i++){
        console.log(arr[i]);
        if (fn(arr[i], i)){
            l.push(arr[i]);
        }
    };
    return l;
}