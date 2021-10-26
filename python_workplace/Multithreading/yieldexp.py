# A simple yield 
def new_gen():
    n = 1
    print('First execution...')
    # Generator function contains yield statements
    yield n

    n += 1
    print('Second execution...')
    yield n

    n += 1
    print('Third execution...')
    yield n

# main method
if __name__=='__main__':
  
  # new_gen function will not execute, but return a generator
  x = new_gen()
  # calling next on variable x
  print(next(x))
  # calling next on variable x
  print(next(x))
  # calling next on variable x
  print(next(x))