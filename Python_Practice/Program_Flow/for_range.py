for i in range(1, 20):
    print(i)

print('*' * 100)

# If we don't provide start value in range, then it defaults to 0
for i in range(10):
    print(i)

print('*' * 100)

# If we want to provide 'step', 'start' value is required as well
for i in range(1, 10, 2):
    print(i)

print('*' * 100)

# if we don't provide 'start' when trying to use 'step'
# then what we consider 'end' will be considered as 'start' by Python..
# and what we consider 'step' will be considered as 'end' by python
for i in range(10, 2):
    print(i)

# Nothing will be printed for this, as end < start

print('*' * 100)

# Now we are going to use Negative step
# Though make sure that start > stop...
# In that case only negative step makes sense
for i in range(10, 1, -2):
    print(i)
