class LetterCombinations:
    def solution(self, digits):
        self._keypad = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        if len(digits) == 0:
            return []
        
        self._digits = digits
        self._comb = []
        self._BT(index=0, current_string=[])
        return self._comb

    def _BT(self, index, current_string):
        if index == len(self._digits):
            comb = ''.join(current_string)
            self._comb.append(comb)
            return
            
        num = int(self._digits[index])
        chars = self._keypad[num]
        for char in chars:
            current_string.append(char)
            self._BT(index+1, current_string)      
            current_string.pop()

letter_combo = LetterCombinations()
print(letter_combo.solution('259'))