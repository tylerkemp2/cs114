"""Convert a number in base-10 into a written out number in English."""

def git_tens(tens):
    if tens == 9:
        tens_word = 'ninety'
    elif tens == 8:
        tens_word = 'eighty'
    elif tens == 7:
        tens_word = 'seventy'
    elif tens == 6:
        tens_word = 'sixty'
    elif tens == 5:
        tens_word = 'fifty'
    elif tens == 4:
        tens_word = 'fourty'
    elif tens == 3:
        tens_word = 'thirty'
    elif tens == 2:
        tens_word = 'twenty'
    return tens_word

def git_ones(ones):
    if ones == 9:
        ones_word = 'nine'
    elif ones == 8:
        ones_word = 'eight'
    elif ones == 7:
        ones_word = 'seven'
    elif ones == 6:
        ones_word = 'six'
    elif ones == 5:
        ones_word = 'five'
    elif ones == 4:
        ones_word = 'four'
    elif ones == 3:
        ones_word = 'three'
    elif ones == 2:
        ones_word = 'two'
    elif ones == 1:
        ones_word = 'one'
    return ones_word

def git_teens(tens, ones):
    if tens == 0:
        teens_word = git_ones(ones)
    elif tens == 1:
        if ones == 1:
            teens_word = 'eleven'
        elif ones == 2:
            teens_word = 'twelve'
        elif ones == 3:
            teens_word = 'thirteen'
        else:
            teens_word = git_ones(ones) + 'teen'
        return teens_word


def main():
     num = int(input('Pick a number between 1 and 99: '))

     tens = num // 10
     ones = num % 10

    #  tens_word = git_tens(tens)
     ones_word = git_ones(ones)
     teens_word = git_teens(tens, ones)

     if tens == 0:
         output = ones_word
     elif tens == 1:
         output = teens_word
     else:
         tens_word = git_tens(tens)
         ones_word = git_ones(ones)
         teens_word = ones_word + 'teen'
    #  return output
    # tens_word = git_tens(tens)
    # ones_word = git_ones(ones)
    # output = git_teens(tens, ones)
         output = tens_word + '-' + ones_word
     print(output)
main()
