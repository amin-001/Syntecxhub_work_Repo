import math

def clean_input(text):
    
    text = text.lower().strip()
    text = text.replace('^', '**')  
    text = text.replace('x', '*')   
    return text

def start_calculator():
    
    print(" Hey! Welcome to the Command-Line Calculator ")
    print(" You can type any expression (e.g., 5 * 6 - 4 + 3) ")
    print(" Type 'exit' or 'quit' whenever you're done. ")
    

    while True:
        raw_user_input = input("Calculate: ")
        
        
        if raw_user_input.strip().lower() in ['exit', 'quit', 'q']:
            print("Catch you later!")
            break
            
        
        if not raw_user_input.strip():
            continue
            
        
        equation = clean_input(raw_user_input)
        
        try:
            
            result = eval(equation, {"__builtins__": None})
            
            
            if isinstance(result, float) and result.is_integer():
                result = int(result)
                
            print(f"-> {result}\n")
            
        except ZeroDivisionError:
            print("-> Error: Can't divide by zero!\n")
        except Exception:
            print("-> Error: Hmm, that equation looks a bit messed up. Check your syntax.\n")


if __name__ == "__main__":
    start_calculator()
