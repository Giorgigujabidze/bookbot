
def sort_on(dict):
    return dict["count"]

def report(filename):
    chars_in_book = set()
    chars_and_counts = list()
    
    with open(filename, 'r') as f:
        book = f.read() 
    
    
    word_count = len(book.split())
    print(f"{word_count} words found in the documnet.")
    
    lowered_book = book.lower()
    
    for x in lowered_book:
        if x.isalpha():
            chars_in_book.add(x)
            
    for x in chars_in_book:
        chars_and_counts.append({"char": x, "count": lowered_book.count(x)})
        
    chars_and_counts.sort(reverse=True, key=sort_on)
    
    
    for x in chars_and_counts:
        print(f"The \'{x['char']}\' was found {x["count"]} times.")
    

def main():
    filename = "books/frankenstein.txt"
    print("--- Begin report of books/frankenstein.txt ---")
    report(filename)
    print("--- End report ---")
    
if __name__ == '__main__':
    main()