package capture_1_stackandqueue;

public class getMaxWindow_main {
	public static void main(String[] args) {
		getMaxWindow test = new getMaxWindow();
		int[] arr = {4, 3, 5, 4, 3, 3, 6, 7};
		int w = 3;
		int[] result = test.GetMaxWindow(arr, w);
		for (int i=0; i < result.length; i++) {
			System.out.println(result[i] + " ");
		}
		System.out.println();
	}
}
