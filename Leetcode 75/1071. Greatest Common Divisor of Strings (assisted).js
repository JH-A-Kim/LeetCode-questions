/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 * Using Euclids algorithm to find the greatest common divisor of the lengths of the strings (had to search for help with this one)
 */
var gcdOfStrings = function(str1, str2) {
    if (str1 + str2 !== str2 + str1) {
        return "";
    }

    const gcd = (a, b) => {
        if (b === 0) {
            return a;
        }
        return gcd(b, a % b);
    };

    const gcdLength = gcd(str1.length, str2.length);

    return str1.slice(0, gcdLength);
};