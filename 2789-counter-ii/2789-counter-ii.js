/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let localInit = init

    function increment(){
        return ++localInit;
    }
    function  decrement(){
        return --localInit;
    }
    function reset(){
        localInit = init
        return localInit;
    }
    return {
        increment:increment,
        decrement:decrement,
        reset:reset
    };
};


const counter = createCounter(5)
counter.increment(); // 6
counter.reset(); // 5
counter.decrement(); // 4