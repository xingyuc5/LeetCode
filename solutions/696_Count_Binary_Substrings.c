int countBinarySubstrings(char *s) {
    int counts = 0, lastConsecutiveCount = 0, currentConsecutiveCount = 0;
    char currentStreak = *s;
    // Interate through string until nullbyte is reached
    while (*s) {
        if (*s != currentStreak) {
            counts += (lastConsecutiveCount > currentConsecutiveCount)
                          ? currentConsecutiveCount
                          : lastConsecutiveCount;

            currentStreak = *s;
            lastConsecutiveCount = currentConsecutiveCount;
            currentConsecutiveCount = 1;
        } else {
            currentConsecutiveCount++;
        }

        s++;
    }

    return counts + (lastConsecutiveCount > currentConsecutiveCount)
               ? currentConsecutiveCount
               : lastConsecutiveCount;
}