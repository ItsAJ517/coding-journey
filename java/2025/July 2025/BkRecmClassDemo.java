/* Book recommandations class
 * This program is an improvement on the 'BookRecommendations.java' program found in the folder labelled 'May 2025'.
 * I have used a BookClass object to encapsulate all the functionality of the previous program into different methods.
 * This approach is aesthetically pleasing and allows a programmer to upgrade the object's functionality without causing side effects in the main program.
 * How to run: this program does not have any additional requirements and can be run directly in the command line.
*/

class BookClass {
    void showMenu() {
        System.out.println("\nChoose a genre:");
        System.out.println("  1. Adventure");
        System.out.println("  2. Mystery");
        System.out.println("  3. Non-fiction");
        System.out.println("  4. Sci-fi/fantasy");
        System.out.println("  5. Romance");
        System.out.print("Choose one (q to quit): ");
    }

    boolean isValid(char ch) {
        if(ch < '1' | ch > '7' & ch != 'q') return false;
        else return true;
    }

    void helpOn(char what) {
        switch(what) {
            // 1. adventure
            case '1':
                System.out.println("Adventure recommendations:");
                System.out.println("  1. 'The Hobbit' by J.R.R. Tolkien");
                System.out.println("  2. 'Hatchet' by Gary Paulsen");
                System.out.println("  3. 'The Martian' by Andy Weir");
                break;
            
            // 2. mystert
            case '2':
                System.out.println("Mystery recommendations:");
                System.out.println("  1. 'The Westing Game' by Ellen Raskin");
                System.out.println("  2. 'And Then There Were None' by Agatha Christia (personal fav!)");
                System.out.println("  3. 'One of Us Is Lying' by Karen M. McManus");
                break;

            // 3. non-fiction
            case '3':
                System.out.println("Non-fiction recommendations:");
                System.out.println("  1. 'Sapiens: A Brief History of Humankind' by Yuval Noah Harari");
                System.out.println("  2. 'Educated' by Tara Westover");
                System.out.println("  3. 'The Body: A Guide for Occupants' by Bill Bryson");
                break;

            // 4. sci-fi/fantasy
            case '4':
                System.out.println("Sci-fi/fantasy recommendations:");
                System.out.println("  1. 'Dune' by Frank Herbert");
                System.out.println("  2. 'The Giver' by Lois Lowry");
                System.out.println("  3. 'Percy Jackson & the Olympians: The Lightning Thief' by Rick Riordan");
                break;
            
            // 5. romance
            case '5':
                System.out.println("Romance recommendations:");
                System.out.println("  1. 'Pride and Prejudice' by Jane Austen");
                System.out.println("  2. 'To All the Boys I've Loved Before' by Jenny Han");
                System.out.println("  3. 'The Fault in Our Stars' by John Green");
                break;
        }
    }
}


class BkRecmClassDemo {
    public static void main(String[] args) 
        throws java.io.IOException {
            
        char choice, ignore;
        BookClass bkobj = new BookClass();

        System.out.println("Book Recommendations");

        for(;;) {
            do {
                bkobj.showMenu();

                choice = (char) System.in.read();

                do {
                    ignore = (char) System.in.read();
                } while(ignore != '\n');

            } while( !bkobj.isValid(choice) );

            if(choice == 'q') break;

            System.out.println();

            bkobj.helpOn(choice);
            
        }

    }
}


