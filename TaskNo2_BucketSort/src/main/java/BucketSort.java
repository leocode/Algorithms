import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class BucketSort {

    public static void main(String[] args) {

        int[] array = {1, 4, 6, 8, 13, 2, 3};
        bucketSort(array, 2, 13);
        System.out.println(java.util.Arrays.toString(array));

        array = new int[]{1235, 12, 25, 65, 2};
        bucketSort(array, 10, 10);
        System.out.println(java.util.Arrays.toString(array));

    }

    public static void bucketSort(int[] tab, int minVal, int maxVal) {

        if (tab == null || tab.length == 0 || minVal == maxVal) return;

        final int N = tab.length, M = maxVal - minVal, NUM_BUCKETS = M / N + 1;
        List<List<Integer>> buckets = new ArrayList<>(NUM_BUCKETS);
        for (int i = 0; i < NUM_BUCKETS; i++) buckets.add(new ArrayList<>());

        for (int i = 0; i < N; i++) {
            int bi = (tab[i] - minVal) / M;
            List<Integer> bucket = buckets.get(bi);
            bucket.add(tab[i]);
        }

        for (int bi = 0, j = 0; bi < NUM_BUCKETS; bi++) {
            List<Integer> bucket = buckets.get(bi);
            if (bucket != null) {
                Collections.sort(bucket);
                for (int k = 0; k < bucket.size(); k++) {
                    tab[j++] = bucket.get(k);
                }
            }
        }
    }
}
