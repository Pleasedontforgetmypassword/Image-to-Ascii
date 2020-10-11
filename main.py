from sys import argv
from Ascii import valid, write, conversion

#checks if the command is valid
def check(args):
    
    #if the second argument does not specify 10 or 70 characters, then return false
    if args[1] not in ["10", "70"]:
        return False
    
    #if all those conditions are true, then return if the file can be opened
    return valid(' '.join(args[2:len(args)]))

#main function
def main():
    
    #if the command is incorrect
    if check(argv) == False:
        
        #tell the user how to use the program
        print("Usage: python main.py (70 or 10) (Image name)")
        return 1
    
    else:
        
        #print writing...
        print("Writing...")
        
        #write the image into ascii values
        write(int(argv[1]), conversion(' '.join(argv[2:len(argv)])), "Image.txt")
        
        #tell the user the program is done
        print("Done")
        return 0

if __name__ == '__main__':
    main()
