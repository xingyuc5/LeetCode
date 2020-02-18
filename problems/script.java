import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.FileWriter;
import java.io.PrintWriter;

public class Script {
    public static void main(String[] args) {
        // Concate template string
        String template = "";
        try (BufferedReader br = new BufferedReader(new FileReader("template.md"))) {
            // Skip first line
            br.readLine();
            String line;

            while ((line = br.readLine()) != null) {
                template += line;
                template += "\n";
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        // Extract file name and write file with template string
        try (BufferedReader br = new BufferedReader(new FileReader("question.txt"))) {
            int lineNumber = 0;
            String line, fileName = "";

            while ((line = br.readLine()) != null) {
                // Even line is question number
                if (lineNumber % 2 == 0) {
                    fileName = line;
                    fileName += ". ";
                } else {
                    fileName += line;
                    fileName += ".md";

                    try (PrintWriter pw = new PrintWriter(new FileWriter(fileName))) {
                        pw.println("# " + fileName);
                        pw.println(template);
                    }

                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}