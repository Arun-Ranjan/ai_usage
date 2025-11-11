## Sample Task 1: Code Review

**Prompt:**  
Review this Python function for bugs and style issues.

```python
def calculate_discount(price, discount):
    if discount > 0 and discount < 100:
        discounted = price * (discount / 100)
        return price - discounted
    return price
```

**Outputs:**

- **GPT-4:**  
  1. The function looks correct overall. However, consider adding input validation for negative prices or discounts greater than 100.
  2. Use more descriptive variable names, e.g., "discount_amount" instead of "discounted".

- **Claude 2:**  
  1. Handles typical cases well, but does not check for zero or negative input.
  2. Consider logging a warning for invalid inputs.

- **CodeBERT (fine-tuned):**  
  - Suggests: Add input check for price and discount; rename variables for clarity.

---

## Sample Task 2: Code Summarization

**Prompt:**  
Summarize what this function does.

```python
def get_usernames(users):
    return [user.name for user in users if user.active]
```

**Outputs:**

- **GPT-4:**  
  Returns a list of usernames for users who are active.

- **Claude Instant:**  
  Generates: Extracts .name from each active user.

- **CodeT5 (fine-tuned):**  
  Summarizes: Returns names of active users from the users list.

---

## Sample Task 3: Bug Detection

**Prompt:**  
Detect any bug in the following function.

```python
def divide(x, y):
    return x / y
```

**Outputs:**

- **GPT-4:**  
  There's a potential bug if `y` is zero. Should handle ZeroDivisionError.

- **Claude 2:**  
  Warns: Function does not check for division by zero.

- **BugLab:**  
  Flags: Possible division by zero error; add validation.

---

## Sample Task 4: Code Q&A

**Prompt:**  
What is the purpose of this function?

```python
def count_positive(numbers):
    return len([n for n in numbers if n > 0])
```

**Outputs:**

- **GPT-4:**  
  This function counts how many numbers in the input list are positive.

- **Claude Instant:**  
  Purpose: Returns the count of positive numbers in a list.

- **CodeT5+ (fine-tuned):**  
  Counts number of positive values in numbers.

---

## Sample Task 5: Compare Model Costs (UI Table)

| Model      | Tokens | Cost ($) | Quality           |
|------------|--------|----------|-------------------|
| GPT-4      | 700    | 0.021    | SOTA              |
| Claude 2   | 700    | 0.0168   | Competitive       |
| CodeBERT   | 120    | 0.00036  | Very High         |
| CodeT5+    | 100    | 0.00010  | High              |

---

**How to Use in Your UI:**  
- Let users enter a code task or select a scenario, then show predicted or actual outputs from the models (just like above).
- Show the benchmarked costs/efficiency for each.

**You can expand these or allow users to interactively change the sample code for even more value!**