/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    let cachedValues = {};

    return function(...args) {
        const key = JSON.stringify(args); //Will create a key that is sorted so [5,4] would become [4,5]

        if (key in cachedValues){ //Checks if the key such as [4,5] exists in the cachedValues string
            return cachedValues[key]; //if so it will return the cached value at the key location as we can use it as
            //an index location for the result of that operation
        }

        const result = fn(...args); //This will do the operation if it has never been performed before
        cachedValues[key] = result; //this will add the result of the operation to the location of the key created
        //so it can then be used as an index for finding that result if the same operation is performed.

        return result; //And this will simply return the result
    }
}


/**
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1
 */