package capture_1_stackandqueue;

import java.util.Stack;

public class ReverseStack {
	Stack<Integer> stack = new Stack<Integer>();
	//����ջ��Ԫ�ز���ջ��ɾ��
	public static int GetAndRemoveLastElement(Stack<Integer> stack) {
		int result = stack.pop();
		if(stack.isEmpty()) {
			return result;
		} else {
			int last = GetAndRemoveLastElement(stack);
			stack.push(result);
			return last;
		}
	}
	
	//����ջ
	public static void reverse(Stack<Integer> stack) {
		if (stack.isEmpty()) {
			return ;
		} 
		int i = GetAndRemoveLastElement(stack);
		reverse(stack);
		stack.push(i);
	}
}
