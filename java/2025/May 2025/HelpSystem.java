/* Java Help System
This file displays the general form of several selection and iteration statements.
This file could perhaps serve as a reminder of how to use the statements in the future.
How to run: this file does not have any additional requirements and can be run directly in the command line.*/

class HelpSystem {
    public static void main(String[] args) 
        throws java.io.IOException {
        char choice, ignore;

        for(;;) {
            do {
                // user enters option
                System.out.println("Help on:");
                System.out.println("  1. if");
                System.out.println("  2. switch");
                System.out.println("  3. for");
                System.out.println("  4. while");
                System.out.println("  5. do-while");
                System.out.println("  6. break");
                System.out.println("  7. continue\n");
                System.out.print("Choose one (q to quit): ");

                choice = (char) System.in.read();

                // this loop prevents multiple lines being printed
                do {
                    ignore = (char) System.in.read();
                } while(ignore != '\n');
            
            } while(choice < '1' | choice > '7' & choice != 'q');

            if(choice == 'q') break;

            System.out.println();

            switch(choice) {
                // [1] if
                case '1':
                    System.out.println("The if:\n");
                    System.out.println("if(condition) statement;");
                    System.out.println("else statement;");
                    break;

                // [2] switch
                case '2':
                    System.out.println("The traditional switch:\n");
                    System.out.println("switch(expression) {");
                    System.out.println("  case constant:");
                    System.out.println("    statement sequence");
                    System.out.println("    break;");
                    System.out.println("  // ...");
                    System.out.println("}");
                    break;

                // [3] for
                case '3':
                    System.out.println("The for:\n");
                    System.out.print("for(init; condition; iteration)");
                    System.out.println(" statement;");
                    break;

                // [4] while
                case '4':
                    System.out.println("The while:\n");
                    System.out.println("while(condition) statement;");
                    break;

                // [5] do-while
                case '5':
                    System.out.println("The do-while:\n");
                    System.out.println("do {");
                    System.out.println("  statement;");
                    System.out.println("} while(condition);");
                    break;

                // [6] break
                case '6':
                    System.out.println("The break:\n");
                    System.out.println("break; or break label;");
                    break;

                // [7] continue
                case '7':
                    System.out.println("The continue:\n");
                    System.out.println("continue; or continue label;");
                    break;
            }
            System.out.println();
        }
    }
}
