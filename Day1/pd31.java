import java.util.*;

class seq
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the number of elements in the array: ");
        int n = sc.nextInt();

        int arr[] = new int[n];   // ✅ allocate memory

        System.out.println("Enter the elements of the array: ");
        for(int i = 0; i < n; i++)
        {
            arr[i] = sc.nextInt();
        }

        int maxLen = 1;

        for(int i = 0; i < n; i++)
        {
            int currLen = 1;

            for(int j = i + 1; j < n; j++)
            {
                if(arr[j] == arr[i] + currLen)
                {
                    currLen++;
                }
            }

            if(currLen > maxLen)
            {
                maxLen = currLen;
            }
        }

        System.out.println("Longest consecutive sequence length: " + maxLen);
        sc.close();

    }
}
