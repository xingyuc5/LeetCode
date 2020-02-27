class Solution {
    public String countAndSay(int n) {
        String result = "1";
        if (n == 1) {
            return result;
        }
        // While greater than 1
        while (n > 1) {
            // Apply transition function
            result = transition(result);
            n--;
        }
        return result;
    }

    // Transition function to get next term in sequence from previous
    public String transition(String input) {

        StringBuffer output = new StringBuffer();

        char group = input.charAt(0);
        int counter = 1;
        for (int i = 1; i < input.length(); i++) {
            if (input.charAt(i) == group) {
                // current chracter same as group
                counter++;
            } else {
                // different from group
                output.append(counter).append(group);

                group = input.charAt(i);
                counter = 1;
            }
        }
        output.append(counter).append(group);
        return output.toString();
    }
}