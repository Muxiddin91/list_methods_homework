def main(fruits):
    """
    A list called "fruits" is given and is five in length and contains at least one "apple". Remove the apples from the list and return the list.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    n=0
    ans = []
    while n<len(fruits):
        if fruits[n]!='apple':
            ans.append(fruits[n])
        n+=1
    return ans
print(main(['apple', 'meva1', 'meva2', 'apple', 'meva3', 'apple']))