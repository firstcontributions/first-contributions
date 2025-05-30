function isPalindrome(str) {
    
    const cleanStr = str.toLowerCase().replace(/[^a-z0-9]/g, '');
    
    const reversedStr = cleanStr.split('').reverse().join('');
    
   
    return cleanStr === reversedStr;
}

// Example usage
console.log(isPalindrome("A man, a plan, a canal: Panama")); 
console.log(isPalindrome("race a car")); 
console.log(isPalindrome("Was it a car or a cat I saw?")); 
console.log(isPalindrome("hello")); 