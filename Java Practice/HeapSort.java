import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class HeapSort {

	public static void main(String[] args) throws IOException {

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Enter array length: ");
		int n = Integer.parseInt(in.readLine());
		if(n>0) {
			System.out.print("Enter the elements in the array as space separated numbers: ");
			String[] input = in.readLine().split(" ");
			int[] inputArray = new int[n];

			for(int i=0;i<n;i++) {
				inputArray[i] = Integer.parseInt(input[i]);
			}

			System.out.println();
			System.out.println("Building the heap...");

			HeapSort hsObj = new HeapSort();
			hsObj.buildHeap(inputArray);

			System.out.println("Heap after building:");

			for(int i=0;i<n;i++) {
				System.out.print(inputArray[i]+" ");
			}
			System.out.println();

			System.out.println("Sorting...");
			int lastElementPos = n-1;

			for(int i=lastElementPos;i>=1;i--) {
				hsObj.swap(inputArray,0,lastElementPos);
				lastElementPos--;
				hsObj.heapify(inputArray,0,lastElementPos+1);
			}

			for(int i=0;i<n;i++) {
				System.out.print(inputArray[i]+" ");
			}

			System.out.println();
		}
		in.close();
	}

	void buildHeap(int[] inputArray) {
		int n = inputArray.length;

		for(int i = (int)Math.floor(n/2)-1;i>=0;i--) {
			heapify(inputArray,i,n);
		}
	}

	void heapify(int[] inputArray, int loc, int lastElementPos) {
		int n = lastElementPos;
		int maxPos = loc;

		if((2*loc+2)<n) {
			int leftChildPos = 2*loc+1;
			int rightChildPos = 2*loc+2;
			maxPos = compare(inputArray, loc, leftChildPos, rightChildPos);
		}
		else if((2*loc+1)<n) {
			int leftChildPos = 2*loc+1;
			maxPos = compare(inputArray, loc, leftChildPos);
		}

		if(maxPos != loc) {
			swap(inputArray, maxPos, loc);
			heapify(inputArray,maxPos, lastElementPos);
		}
	}

	int compare(int[] inputArray, int parentPos, int leftChildPos, int rightChildPos) {
		int max = parentPos;

		if(inputArray[leftChildPos]>inputArray[max]) {
			max = leftChildPos;
		}

		if(inputArray[rightChildPos]>inputArray[max]) {
			max = rightChildPos;
		}

		return max;
	}

	int compare(int[] inputArray, int parentPos, int leftChildPos) {
		int max = parentPos;

		if(inputArray[leftChildPos]>inputArray[max]) {
			max = leftChildPos;
		}

		return max;
	}

	void swap(int[] inputArray, int pos1, int pos2) {
		int temp = inputArray[pos1];
		inputArray[pos1] = inputArray[pos2];
		inputArray[pos2] = temp;
	}
}