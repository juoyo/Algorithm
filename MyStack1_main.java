package first;

public class MyStack1_main {
	
	public static void main(String[] args){
		MyStack1 stack1 = new MyStack1();
		stack1.push(3);
		System.out.println(stack1.getmin());
		stack1.push(4);
		System.out.println(stack1.getmin());
		stack1.push(1);
		System.out.println(stack1.getmin());
		
		System.out.println(stack1.pop());
		//System.out.println(stack1.getmin());
	}
}
