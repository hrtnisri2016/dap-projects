import numpy as np

def calculate(dlist):
  # check length of the list
  if len(dlist) != 9:
    # raise the ValueError
    raise ValueError("List must contain nine numbers.")
  else:
    # convert the list into 3 x 3 Numpy array
    arr = np.array(dlist).reshape(3, 3)
    # calculate mean
    mean_axis1 = list(np.mean(arr, axis=0))
    mean_axis2 = list(np.mean(arr, axis=1))
    mean_flattened = np.mean(arr).tolist()
    mean = [mean_axis1, mean_axis2, mean_flattened]
    # calculate variance
    variance_axis1 = list(np.var(arr, axis=0))
    variance_axis2 = list(np.var(arr, axis=1))
    variance_flattened = np.var(arr).tolist()
    variance = [variance_axis1, variance_axis2, variance_flattened]
    # calculate standard deviation
    std_axis1 = list(np.std(arr, axis=0))
    std_axis2 = list(np.std(arr, axis=1))
    std_flattened = np.std(arr).tolist()
    standard_deviation = [std_axis1, std_axis2, std_flattened]
    # calculate the maximum value
    max_axis1 = list(np.amax(arr, axis=0))
    max_axis2 = list(np.amax(arr, axis=1))
    max_flattened = np.amax(arr).tolist()
    max = [max_axis1, max_axis2, max_flattened]
    # calculate the minimum value
    min_axis1 = list(np.amin(arr, axis=0))
    min_axis2 = list(np.amin(arr, axis=1))
    min_flattened = np.amin(arr).tolist()
    min = [min_axis1, min_axis2, min_flattened]
    # calculate sum
    sum_axis1 = list(np.sum(arr, axis=0))
    sum_axis2 = list(np.sum(arr, axis=1))
    sum_flattened = np.sum(arr).tolist()
    sum = [sum_axis1, sum_axis2, sum_flattened]
    # the output
    calculations = {
      'mean': mean,
      'variance': variance,
      'standard deviation': standard_deviation,
      'max': max, 
      'min': min,
      'sum': sum
    }

    return calculations
