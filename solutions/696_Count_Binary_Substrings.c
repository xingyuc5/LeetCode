int countBinarySubstrings(char *s) {
    int counts = 0, lastStrLen = 0, currStrLen = 0;
    char currSign = *s;

    while (*s) {
        if (*s != currSign) {
            counts += ((lastStrLen > currStrLen) ? currStrLen : lastStrLen);

            currSign = *s;
            lastStrLen = currStrLen;
            currStrLen = 1;
        } else {
            currStrLen++;
        }
        s++;
    }

    return counts + ((lastStrLen > currStrLen) ? currStrLen : lastStrLen);
}
