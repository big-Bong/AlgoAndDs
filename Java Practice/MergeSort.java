import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;


class MergeSort {
	
	public static void main(String[] args) {


		try {
			BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
			
			System.out.println("Enter a value: ");
			int n = Integer.parseInt(in.readLine());
			int[] originalArray = new int[n];

			for(int i=0;i<n;i++) {
				System.out.println("Enter a value: ");
				originalArray[i] = Integer.parseInt(in.readLine());
			}
			int l = 0;
			int r = n-1;

			mergeSort(l,r,originalArray);


			System.out.println();
			for(int i=0;i<n;i++) {
				System.out.print(originalArray[i]+" ");
			}

			in.close();
		}
		catch(IOException ex) {
			System.out.println(ex);
		}

	}

	static void mergeSort(int l, int r, int[] originalArray) {
		

		if(r>l) {
			int m = l+(r-l)/2;

			mergeSort(l,m,originalArray);
			mergeSort(m+1,r,originalArray);
			merge(l,m,r,originalArray);
		}
	}

	static void merge(int l, int m, int r, int[] originalArray) {

		int[] tempArr = new int[r-l+1];
		int start1 = l;
		int end1 = m;
		int start2 = m+1;
		int end2 = r;
		int inc = 0;

		while(start1<=end1&&start2<=end2) {
			if(originalArray[start1]<originalArray[start2]) {
				tempArr[inc] = originalArray[start1];
				start1++;
			}
			else {
				tempArr[inc] = originalArray[start2];
				start2++;
			}

			inc++;
		}

		if(start1>end1) {
			for(int i=start2;i<=end2;i++) {
				tempArr[inc] = originalArray[i];
				inc++;
			}
		}
		else if(start2>end2){
			for(int i=start1;i<=end1;i++) {
				tempArr[inc] = originalArray[i];
				inc++;
			}
		}

		inc = 0;

		for(int i=l;i<=r;i++) {
			originalArray[i] = tempArr[inc];
			inc++;
		}
	}
}