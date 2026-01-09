let s = "121";
let rev = s.split("").reverse().join("");

if (s === rev) {
    console.log("Palindrome");
} else {
    console.log("Not Palindrome");
}
