import java.util.Scanner;
public class MergeSort {
  /** The method for sorting the numbers */


  /*
   * Worst Case: O(n log n)
   */
  public static void mergeSort(int[] list) {
    if (list.length > 1) {
      // Merge sort the first half
      //Using Divide and conquer we split the list in half
      //and process recursively until the list is sorted.

      //Split the first first half
      int[] firstHalf = new int[list.length / 2]; // runs n times
      System.arraycopy(list, 0, firstHalf, 0, list.length / 2); //runs n times
      mergeSort(firstHalf); //runs n times

      // Split the second half
      int secondHalfLength = list.length - list.length / 2; //runs n times
      int[] secondHalf = new int[secondHalfLength]; //runs n times
      System.arraycopy(list, list.length / 2,
        secondHalf, 0, secondHalfLength); //runs n times
      mergeSort(secondHalf); //runs n times

      // Merge firstHalf with secondHalf
      //Now that the list has been split to a smaller size
      //then we can try to merge it
      int[] temp = merge(firstHalf, secondHalf); //runs n times
      System.arraycopy(temp, 0, list, 0, temp.length); //runs n times
    }
  }

  /** Merge two sorted lists */
  private static int[] merge(int[] list1, int[] list2) {
    int[] temp = new int[list1.length + list2.length];

    int current1 = 0; // Current index in list1
    int current2 = 0; // Current index in list2
    int current3 = 0; // Current index in temp

    //Loop the elements
    while (current1 < list1.length && current2 < list2.length) { //Runs n - 1
    //Compare the elements in each list and add to the merge list
      if (list1[current1] < list2[current2])
        temp[current3++] = list1[current1++];
      else
        temp[current3++] = list2[current2++];
    }
    //Copy the rest of elements into the list
    while (current1 < list1.length)
      temp[current3++] = list1[current1++];
  //Copy the rest of elements into the list
    while (current2 < list2.length)
      temp[current3++] = list2[current2++];

    return temp;
  }

  /** A test method */
  public static void main(String[] args) {
    int[] list = {5,4,7,28,3,27,327,54,1000};
    mergeSort(list);
    for (int i = 0; i < list.length; i++)
      System.out.print(list[i] + " ");
  }
}
