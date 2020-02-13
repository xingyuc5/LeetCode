bool checkValidString(char* s) {
    int left = 0, right = 0, star = 0, i = 0;

    while (*s) {
        if (*s == '(') {
            left++;
        } else if (*s == ')') {
            right++;
        } else if (*s = '*') {
            star++;
        }
        if (left + star < right) {
            return false;
        }
        s++;
        i++;
    }
    left = 0, right = 0, star = 0, s--;
    while (i > 0) {
        if (*s == '(') {
            left++;
        } else if (*s == ')') {
            right++;
        } else if (*s = '*') {
            star++;
        }
        if (right + star < left) {
            return false;
        }
        s--;
        i--;
    }

    return true;
}

