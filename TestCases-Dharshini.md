# Manual Test Cases — Contribution by Dharshini

## Feature: User Signup Form

### Test Case 1: Empty Fields
**Steps:**  
1. Open the signup page  
2. Click the "Sign Up" button without entering any data  
**Expected Result:**  
Validation messages should appear for all required fields (Name, Email, Password).

---

### Test Case 2: Invalid Email Format
**Steps:**  
1. Enter invalid text that is incorrect email ot text in email field  
2. Fill other fields correctly  
3. Click "Sign Up"  
**Expected Result:**  
Error message: "Please enter a valid email address".

---

### Test Case 3: Password Too Short
**Steps:**  
1. Enter a valid email  
2. Enter password "123"  
3. Click "Sign Up"  
**Expected Result:**  
Error message: "Password must be at least 6 characters".

---

### Test Case 4: Password and Confirm Password Mismatch
**Steps:**  
1. Enter valid email  
2. Enter your password for example "passwords@*123" 
3. Enter confirm password that does not match the password you entered for example "passwords@*1"  
4. Submit  
**Expected Result:**  
Error: "Passwords do not match".

---

### Test Case 5: Invalid Mobile Number
**Steps:**  
1. Enter 5-digit number in "Mobile No" field  
2. Submit  
**Expected Result:**  
Error: "Enter a valid 10-digit mobile number".

---

### Test Case 6: Email Already Exists (Server Validation)
**Steps:**  
1. Enter an email that is already registered  
2. Submit  
**Expected Result:**  
Error: "Email already in use".

---

### Test Case 7: Successful Signup
**Steps:**  
1. Enter valid name, email, password, confirm password, phone  
2. Click "Sign Up"  
**Expected Result:**  
Signup successful → Redirect to login page / Dashboard.

---

### Test Case 8: Password Strength Check
**Steps:**  
1. Enter weak password like "123"  
2. Check the strength indicator  
**Expected Result:**  
Strength indicator shows "Weak".

---

### Test Case 9: Special Characters in Name Field
**Steps:**  
1. Enter "@$%%" as name  
2. Submit  
**Expected Result:**  
Error message: "Name cannot contain special characters".

---


