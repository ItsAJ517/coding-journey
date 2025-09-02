/* Book recommendations
This program provides the user with recommendations for different genres of books.
/*

class BookRecommendations {
    public static void main(String[] args)
        throws java.io.IOException {
            
        char choice, ignore;

        System.out.println("Book Recommendations");

        for(;;) {
            do {
                System.out.println("\nChoose a genre:");
                System.out.println("  1. Adventure");
                System.out.println("  2. Mystery");
                System.out.println("  3. Non-fiction");
                System.out.println("  4. Sci-fi/fantasy");
                System.out.println("  5. Romance");
                System.out.print("Choose one (q to quit): ");

                choice = (char) System.in.read();

                do {
                    ignore = (char) System.in.read();
                } while(ignore != '\n');

            } while(choice < '1' | choice > '7' & choice != 'q');

            if(choice == 'q') break;

            System.out.println();

            switch(choice) {
                // 1. adventure
                case '1':
                    System.out.println("Adventure recommendations:");
                    System.out.println("  1. 'The Lord Of The Rings' (trilogy) by J.R.R. Tolkien");
                    System.out.println("  2. 'Hatchet' by Gary Paulsen");
                    System.out.println("  3. 'The Martian' by Andy Weir");
                    break;
                
                // 2. mystery
                case '2':
                    System.out.println("Mystery recommendations:");
                    System.out.println("  1. 'The Westing Game' by Ellen Raskin");
                    System.out.println("  2. 'And Then There Were None' by Agatha Christie (personal fav!)");
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
}



