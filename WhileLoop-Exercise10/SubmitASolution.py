looking_book = str(input())

input_line = input()

is_book_found = False
book_count = 0
while input_line != 'No More Books':

    if input_line == looking_book:
        is_book_found = True
        break
    book_count += 1

    input_line = input()
if is_book_found:
    print(f'You checked {book_count} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {book_count} books.')