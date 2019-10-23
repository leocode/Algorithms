import java.time.LocalDateTime;

public class ClockMain {
    public static void main(String[] args) {

        System.out.println(alarm(6, 10));
        System.out.println(alarm(21, 50));
        System.out.println(alarm(25, 10));
        System.out.println(alarm(22, 65));
    }

    public static String alarm(Integer hh, Integer mm) {
        Integer nowHH = LocalDateTime.now().getHour();
        Integer nowMM = LocalDateTime.now().getMinute();
        int ringHH = 0;
        int ringMM = 0;


        if (mm < nowMM && mm > 0 && mm <= 60 && hh >= 0 && hh <= 23) {
            ringMM = mm + 60 - nowMM;
            if (hh < nowHH) {
                ringHH = hh + 23 - nowHH;
            } else if (hh > nowHH) {
                ringHH = hh - nowHH;
            }
        } else if (mm > nowMM && mm > 0 && mm <= 60 && hh >= 0 && hh <= 23) {
            ringMM = mm - nowMM;
            ringHH = hh - nowHH;
        } else if (mm.equals(nowMM) && mm > 0 && mm <= 60 && hh >= 0 && hh <= 23) {

            ringHH = 0;
        } else {
            return "Please type a correct time.";
        }
        return "You will sleep " + ringHH + " hours and " + ringMM + " minutes.";
    }

}
