def is_called():
    def is_returned():
        print("Hello")
    
    # Part of is_called
    # Returns is_returned function     
    return is_returned


new = is_called()

# Outputs "Hello"
new()