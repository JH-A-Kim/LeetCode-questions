/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    function toBe(test) {
        if (val!==test) throw new Error('Not Equal');
        else return true;
    }
    function notToBe(test){
        if (val===test) throw new Error('Equal');
        else return true;
    }
    return {toBe, notToBe}
};
