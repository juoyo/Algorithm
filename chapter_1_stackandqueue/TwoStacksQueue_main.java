package capture_1_stackandqueue;

public class TwoStacksQueue_main {
	public static void main(String[] args) {
		TwoStacksQueue twostacksqueue = new TwoStacksQueue();
		twostacksqueue.add(1);
		twostacksqueue.add(3);
		twostacksqueue.add(5);
		System.out.println(twostacksqueue.peek());
		System.out.println(twostacksqueue.poll());
		System.out.println(twostacksqueue.peek());
		System.out.println(twostacksqueue.poll());
		System.out.println(twostacksqueue.peek());
		System.out.println(twostacksqueue.poll());
	}
}
