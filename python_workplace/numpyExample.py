# =======================
# Array Manipulations (NumPy)
# =======================
# Importing NumPy for Array manipulations
import numpy as np
array_var = np.array([1, 2, 3, 4, 5])
print("\n=== Array Manipulations (NumPy) ===")
print(f"Original Array: {array_var}")

# Adding elements
array_var = np.append(array_var, [6])
print(f"After append([6]): {array_var}")

# Removing elements
array_var = np.delete(array_var, 2)
print(f"After delete(index 2): {array_var}")

# Updating elements
array_var[1] = 99
print(f"After updating index 1 to 99: {array_var}")

# Array operations
array_var = array_var * 2
print(f"After element-wise multiplication by 2: {array_var}")

# Sorting
sorted_array = np.sort(array_var)
print(f"After sort(): {sorted_array}")
