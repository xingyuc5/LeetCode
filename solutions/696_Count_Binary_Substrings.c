int countBinarySubstrings(char *s)
{
    int counts = 0, lastConsecutiveCount = 0, currentCosecutiveCount = 0;
    char currentStreak = *s;
    // Interate through string until nullbyte is reached
    while (*s)
    {
        if (*s != currentStreak)
        {
            counts++;
            currentStreak = *s;
            lastConsecutiveCount = currentCosecutiveCount;
            currentCosecutiveCount = 1;
        }
        else
        {
            currentCosecutiveCount++;
            if (lastConsecutiveCount != 0 && currentCosecutiveCount <= lastConsecutiveCount)
            {
                counts++;
            }
        }

        s++;
    }

    return counts;
}