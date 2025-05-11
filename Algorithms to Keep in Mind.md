# Algorithms

## Table of Contents
1. [Euclid's Algorithm](#euclids-algorithm)
2. [Other Algorithms](#other-algorithms)

---

## Euclid's Algorithm

**Description**: Euclid's Algorithm is used to find the Greatest Common Divisor (GCD) of two numbers. The GCD is the largest number that divides both numbers without leaving a remainder. (can be used on strings as well as long as str1 + str2 = str2 + str1)

**How It Works**:
1. **Take Two Numbers**: Start with two numbers, `a` and `b`.
2. **Find the Remainder**: Divide the larger number (`a`) by the smaller number (`b`) and find the remainder (`r`).
3. **Replace the Larger Number**: Replace `a` with `b` and `b` with the remainder (`r`).
4. **Repeat**: Repeat the process until the remainder is `0`. The non-zero number is the GCD.

**Example**:
Find the GCD of 48 and 18:
- Divide 48 by 18, remainder is 12. (48 % 18 = 12)
  - Replace: `a = 18`, `b = 12`
- Divide 18 by 12, remainder is 6. (18 % 12 = 6)
  - Replace: `a = 12`, `b = 6`
- Divide 12 by 6, remainder is 0. (12 % 6 = 0)
  - Replace: `a = 6`, `b = 0`

The GCD is `6`.

**JavaScript Code**:

```javascript
/**
 * Function to calculate the Greatest Common Divisor (GCD) using Euclid's Algorithm.
 * @param {number} a - The first number.
 * @param {number} b - The second number.
 * @return {number} - The GCD of the two numbers.
 */
const gcd = (a, b) => {
    if (b === 0) {
        return a;
    }
    return gcd(b, a % b);
};

// Example usage
console.log(gcd(48, 18)); // Output: 6

---

```

## Other Algorithms

### [Algorithm Name]

**Description**: 

**How It Works**:
1. 
2. 
3. 

**Example**:
- 

---

## Data Structures Notes

### What are Lists not good for?

**Lists are not good for**:
1. A large number of deletions of middle elements 
2. A large number of searching