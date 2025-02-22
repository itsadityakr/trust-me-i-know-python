
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

# Augmented Assignment Operators

Augmented assignment operators **combine an arithmetic operation with assignment** in a shorter and more efficient way.  

Instead of writing:  
`num = num + 10`  
You can simply write:  
`num += 10`  

This applies to all arithmetic operations like addition, subtraction, multiplication, division, exponentiation, and modulus.  

---

## **Using Augmented Assignment Operators**  

```python
# Initial value
num = 20
```

1. **Addition Assignment (`+=`)**  
   ```python
   # num = num + 10
   num += 10  
   print(num)  # Output: 30
   ```
   - Adds `10` to `num`.  

2. **Subtraction Assignment (`-=`)**  
   ```python
   # num = num - 15
   num -= 15  
   print(num)  # Output: 15
   ```
   - Subtracts `15` from `num`.  

3. **Multiplication Assignment (`*=`)**  
   ```python
   # num = num * 10
   num *= 10  
   print(num)  # Output: 150
   ```
   - Multiplies `num` by `10`.  

4. **Division Assignment (`/=`)**  
   ```python
   # num = num / 10
   num /= 10  # [1] 
   print(num)  # Output: 15.0
   ```
   - Divides `num` by `10` and **converts it to a float**.  

5. **Exponentiation Assignment (`**=`)**  
   ```python
   # num = num ** 2
   num **= 2  
   print(num)  # Output: 225.0
   ```
   - Raises `num` to the power of `2` (`15.0 ** 2 = 225.0`).  

6. **Modulus Assignment (`%=`)**  
   ```python
   # num = num % 10
   num %= 10  
   print(num)  # Output: 5.0
   ```
   - Finds the remainder when `num` is divided by `10`.  

---

## **Summary Table**  

| Operator  | Example | Equivalent To | Description |
|-----------|---------|--------------|-------------|
| `+=` | `num += 10` | `num = num + 10` | Adds and assigns |
| `-=` | `num -= 5` | `num = num - 5` | Subtracts and assigns |
| `*=` | `num *= 3` | `num = num * 3` | Multiplies and assigns |
| `/=` | `num /= 2` | `num = num / 2` | Divides and assigns (converts to float) |
| `**=` | `num **= 2` | `num = num ** 2` | Exponentiation and assigns |
| `%=` | `num %= 4` | `num = num % 4` | Modulus and assigns |

**Key Notes:**  
- These operators make the code **shorter and more readable**.  
- Division (`/=`) **always converts the result to a float**, even if the original number was an integer.

![Static Badge](https://img.shields.io/badge/Aditya%20Kumar-black?style=for-the-badge&logo=atlasos&logoColor=%23ffffff)