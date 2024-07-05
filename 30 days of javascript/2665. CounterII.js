/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    const ogValue = init;
    let workingValue = ogValue;

    function increment() {
        return workingValue=workingValue+1;
    }
    function decrement() {
        return workingValue=workingValue-1;
    }
    function reset() {
        return workingValue=ogValue;
    }
    return {increment, decrement, reset}
};