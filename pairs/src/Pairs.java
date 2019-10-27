class Pairs {
    public static void main(String[] args) {
        int[] partyPeople1 = {25, 19, 21, 25, 21};
        int[] partyPeople2 = {25, 19, 21, 25, 21, 19};
        aloneAtParty(partyPeople1);
        aloneAtParty(partyPeople2);
    }

    //finds an integer in an array that does not have a 'partner' of the same value

    private static void aloneAtParty(int[] attendees) {
        int unpaired = -1;

        for (int index = 0; index < attendees.length; index++) {
            int count = 0;
            for (int check = 0; check < attendees.length; check++) {
                if (attendees[index] == attendees[check]) {
                    count++;
                }
            }
            if (count == 1) {
                unpaired = attendees[index];
            }
        }
        if (unpaired > -1) {
            System.out.println("The person alone is " + unpaired + " years old.");
        }
        else {
            System.out.println("Everybody's got a pair.");
        }
    }
}